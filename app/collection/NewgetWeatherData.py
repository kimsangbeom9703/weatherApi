import pprint
import sys
from os import path
import time
import requests
from requests.exceptions import RequestException
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

###
# # -VSRT: 초단기예보
# # -SHRT: 단기예보
# ##
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.config import settings

from db.session import SessionLocal
from db.models.weatherVersionModel import WeatherVersion
from db.models.areaModel import AreaData
from db.models.collectionWeatherModel import CollectionWeatherModel


class WeatherDataCollector:
    def __init__(self, call_type):
        self.call_type = call_type
        self.url = self.get_api_url()
        self.service_key = settings.SERVICE_KEY
        self.base_date, self.base_time ,self.version = self.calculate_base_date_time()
        self.get_area_data()

    def get_api_url(self):
        if self.call_type == 'VSRT':
            _URL = settings.GET_ULTRA_URL
        else:
            _URL = settings.GET_VILAGE_URL
        return _URL

    def calculate_base_date_time(self):
        db = SessionLocal()
        weather_version = db.query(WeatherVersion).filter_by(type=self.call_type, status='00', used=0).order_by(
            WeatherVersion.id.desc()).first()
        if not weather_version:
            print("No weather version found. Exiting gracefully...")
            return None, None, None
        date = weather_version.datetime[0:8]
        time = weather_version.datetime[8:]
        version = weather_version.version
        db.close()
        return date, time, version

    def get_area_data(self):
        if self.base_date != None:
            db = SessionLocal()
            area_data = (
                db.query(AreaData.grid_x, AreaData.grid_y)
                .filter(AreaData.level3.is_(None))
                .distinct()
                .all()
            )
            for item in area_data:
                now = datetime.now()
                print(f"시간: {now.strftime('%Y-%m-%d %H:%M:%S')}, nx:{item.grid_x}, ny:{item.grid_y}")
                self.call_api_data(item.grid_x, item.grid_y)
                time.sleep(1)
            db.close()
            self.version_update()

        #return area_data

    def call_api_data(self, nx, ny, max_retries=3):
        params = {
            'serviceKey': self.service_key,
            'base_date': self.base_date,
            'base_time': self.base_time,
            'nx': nx,
            'ny': ny,
            'pageNo': '1',
            'numOfRows': '1000',
            'dataType': 'JSON'
        }
        retry_count = 0
        while retry_count < max_retries:
            try:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
                response = requests.get(self.url, params=params, verify=False, headers=headers)
                if response.status_code == 200:
                    weather_data, nx, ny = self.process_api_response(response.json(), nx, ny)
                    # pprint.pp(nx)
                    self.save_weather_data(weather_data, nx, ny)
                    break
                else:
                    print(f"Status code: {response.status_code}")
            except RequestException as e:
                print(f"Request failed: {str(e)}")
                retry_count += 1
                wait_time = 2 ** retry_count  # 지수 백오프를 사용한 재시도 간격 설정
                time.sleep(wait_time)

    def process_api_response(self, response_data, nx, ny):
        df = pd.DataFrame(response_data['response']['body']['items']['item'])
        df['factDateTime'] = pd.to_datetime(df['fcstDate'] + ' ' + df['fcstTime'])
        df_pivot = df.pivot(index=['factDateTime'], columns='category', values='fcstValue')
        df_pivot = df_pivot.fillna(0)
        return df_pivot, nx, ny

    def save_weather_data(self, weather_data, nx, ny):
        db = SessionLocal()
        if self.call_type == 'SHRT':
            self.shrt_data_save(db,weather_data,nx,ny)
        else:
            self.vsrt_data_save(db,weather_data,nx,ny)
        db.close()
    def vsrt_data_save(self,db,weather_data,nx,ny):
        for index, row in weather_data.iterrows():
            now = datetime.now()
            factDateTime = index
            factDateSplit = str(factDateTime).split(' ')
            factDate = factDateSplit[0]
            factTime = factDateSplit[1]
            LGT = row['LGT']
            PTY = row['PTY']
            REH = row['REH']
            PCP = row['RN1']
            SKY = row['SKY']
            TMP = row['T1H']
            UUU = row['UUU']
            VEC = row['VEC']
            VVV = row['VVV']
            WSD = row['WSD']
            ICON = f"DB0{SKY}_{'N_B.svg' if factTime > '1800' or factTime <= '0600' else 'B.svg'}"
            uniqueVal = f"{factDateTime}_{nx}_{ny}"
            check_data = (
                db.query(CollectionWeatherModel).filter(CollectionWeatherModel.uniqueVal == uniqueVal).first()
            )
            if not check_data:
                CollectionWeatherData = CollectionWeatherModel(
                    uniqueVal=uniqueVal,
                    baseDate=self.base_date,
                    baseTime=self.base_time,
                    fcstRealDate=factDateTime,
                    fcstDate=factDate,
                    fcstTime=factTime,
                    callDate=now.strftime('%Y-%m-%d %H:%M:%S'),
                    nx=nx,
                    ny=ny,
                    icon=ICON,
                    ptyVal=PTY,
                    pcpVal=PCP,
                    skyVal=SKY,
                    rehVal=REH,
                    tmpVal=TMP,
                    uuuVal=UUU,
                    vvvVal=VVV,
                    vecVal=VEC,
                    wsdVal=WSD,
                    lgtVal=LGT,
                )
                db.add(CollectionWeatherData)
            else:
                check_data.uniqueVal = uniqueVal,
                check_data.baseDate = self.base_date,
                check_data.baseTime = self.base_time,
                check_data.fcstRealDate = factDateTime,
                check_data.fcstDate = factDate,
                check_data.fcstTime = factTime,
                check_data.callDate = now.strftime('%Y-%m-%d %H:%M:%S'),
                check_data.nx = nx,
                check_data.ny = ny,
                check_data.icon = ICON,
                check_data.ptyVal = PTY,
                check_data.pcpVal = PCP,
                check_data.skyVal = SKY,
                check_data.rehVal = REH,
                check_data.tmpVal = TMP,
                check_data.uuuVal = UUU,
                check_data.vvvVal = VVV,
                check_data.vecVal = VEC,
                check_data.wsdVal = WSD,
                check_data.lgtVal = LGT
            db.commit()
    def shrt_data_save(self,db,weather_data,nx,ny):
        for index, row in weather_data.iterrows():
            now = datetime.now()
            factDateTime = index
            factDateSplit = str(factDateTime).split(' ')
            factDate = factDateSplit[0]
            factTime = factDateSplit[1]
            POP = row['POP']
            PTY = row['PTY']
            PCP = row['PCP']
            REH = row['REH']
            SNO = row['SNO']
            SKY = row['SKY']
            TMP = row['TMP']
            TMN = row['TMN']
            TMX = row['TMX']
            UUU = row['UUU']
            VVV = row['VVV']
            WAV = row['WAV']
            VEC = row['VEC']
            WSD = row['WSD']
            ICON = f"DB0{SKY}_{'N_B.svg' if factTime > '1800' or factTime <= '0600' else 'B.svg'}"
            uniqueVal = f"{factDateTime}_{nx}_{ny}"
            check_data = (
                db.query(CollectionWeatherModel).filter(CollectionWeatherModel.uniqueVal == uniqueVal).first()
            )
            if not check_data:
                CollectionWeatherData = CollectionWeatherModel(
                    uniqueVal=uniqueVal,
                    baseDate=self.base_date,
                    baseTime=self.base_time,
                    fcstRealDate=factDateTime,
                    fcstDate=factDate,
                    fcstTime=factTime,
                    callDate=now.strftime('%Y-%m-%d %H:%M:%S'),
                    nx=nx,
                    ny=ny,
                    icon=ICON,
                    popVal=POP,
                    ptyVal=PTY,
                    pcpVal=PCP,
                    skyVal=SKY,
                    rehVal=REH,
                    snoVal=SNO,
                    tmpVal=TMP,
                    tmnVal=TMN,
                    tmxVal=TMX,
                    uuuVal=UUU,
                    vvvVal=VVV,
                    wavVal=WAV,
                    vecVal=VEC,
                    wsdVal=WSD
                )
                db.add(CollectionWeatherData)
            else:
                check_data.uniqueVal = uniqueVal,
                check_data.baseDate = self.base_date,
                check_data.baseTime = self.base_time,
                check_data.fcstRealDate = factDateTime,
                check_data.fcstDate = factDate,
                check_data.fcstTime = factTime,
                check_data.callDate = now.strftime('%Y-%m-%d %H:%M:%S'),
                check_data.nx = nx,
                check_data.ny = ny,
                check_data.icon = ICON,
                check_data.popVal = POP,
                check_data.ptyVal = PTY,
                check_data.pcpVal = PCP,
                check_data.skyVal = SKY,
                check_data.rehVal = REH,
                check_data.snoVal = SNO,
                check_data.tmpVal = TMP,
                check_data.tmnVal = TMN,
                check_data.tmxVal = TMX,
                check_data.uuuVal = UUU,
                check_data.vvvVal = VVV,
                check_data.wavVal = WAV,
                check_data.vecVal = VEC,
                check_data.wsdVal = WSD
            db.commit()
    def version_update(self):
        db = SessionLocal()
        weather_version = (
            db.query(WeatherVersion).filter_by(type=self.call_type,version=self.version,used=0).first()
        )
        weather_version.used = 1
        db.commit()
        db.close()

if __name__ == "__main__":
    WeatherDataCollector('SHRT')
    WeatherDataCollector('VSRT')
