import pprint
import time
import sys
from os import path
import pandas as pd

from datetime import datetime, timedelta

import requests
from requests.exceptions import RequestException

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.config import settings
from db.session import SessionLocal
from db.models.airKoreaDustDataModel import AirKoreaDustDataModel
from db.models.airKoreaDustStationModel import AirKoreaDustStationModel


class AirKoreaDustDataColletor:

    def __init__(self):
        self.url = settings.AIR_KOREA_DUST_DATA_URL
        self.serviceKey = settings.SERVICE_KEY
        self.returnType = 'json'
        self.pageNo = '1'
        self.numOfRows = '1000'
        self.sidoName = settings.AIR_KOREA_SIDO_NAME
        self.ver = settings.AIR_KOREA_VERSION

        self.call_api_data()

    def call_api_data(self, max_retries=3):
        params = {
            'serviceKey': self.serviceKey,
            'returnType': self.returnType,
            'pageNo': self.pageNo,
            'numOfRows': self.numOfRows,
            'sidoName': self.sidoName,
            'ver': self.ver,
        }
        retry_count = 0
        while retry_count < max_retries:
            try:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
                response = requests.get(self.url, params=params, verify=False, headers=headers)
                if response.status_code == 200:
                    res_data = response.json()
                    status = res_data['response']['header']['resultCode']
                    if (status == '00'):
                        df = pd.DataFrame(res_data['response']['body']['items'])
                        self.save_dust_station_data(df)
                    break
                else:
                    print(f"Status code: {response.status_code}")
            except RequestException as e:
                print(f"Request failed: {str(e)}")
                retry_count += 1
                wait_time = 2 ** retry_count  # 지수 백오프를 사용한 재시도 간격 설정
                time.sleep(wait_time)

    def save_dust_station_data(self, data):
        db = SessionLocal()
        for index, row in data.iterrows():
            dustStationIdx, dustStationName = self.get_station_data(row['stationName'])
            if (row['dataTime'] is None):
                continue
            fcstRealDate, fcstDate, fcstTime, callDate = self.time_change(row['dataTime'])
            dustStationCode = row['stationCode']
            uniqueVal = f"{fcstRealDate}_{dustStationIdx}"
            mangName = row['mangName']
            sidoName = row['sidoName']
            so2Value = row['so2Value']
            coValue = row['coValue']
            o3Value = row['o3Value']
            no2Value = row['no2Value']
            pm10Value = row['pm10Value']
            pm10Value24 = row['pm10Value24']
            pm25Value = row['pm25Value']
            pm25Value24 = row['pm25Value24']
            khaiValue = row['khaiValue']
            khaiGrade = row['khaiGrade']
            so2Grade = row['so2Grade']
            o3Grade = row['o3Grade']
            no2Grade = row['no2Grade']
            pm10Grade = row['pm10Grade']
            pm25Grade = row['pm25Grade']
            pm10Grade1h = row['pm10Grade1h']
            pm25Grade1h = row['pm25Grade1h']
            so2Flag = row['so2Flag']
            coFlag = row['coFlag']
            o3Flag = row['o3Flag']
            no2Flag = row['no2Flag']
            pm10Flag = row['pm10Flag'],
            pm25Flag = row['pm25Flag']
            check_data = (
                db.query(AirKoreaDustDataModel).filter(
                    AirKoreaDustDataModel.uniqueVal == uniqueVal).first()
            )
            if not check_data:
                AirKoreaDustData = AirKoreaDustDataModel(
                    uniqueVal=uniqueVal,
                    dustStationIdx=dustStationIdx,
                    dustStationName=dustStationName,
                    dustStationCode=dustStationCode,
                    fcstRealDate=fcstRealDate,
                    fcstDate=fcstDate,
                    fcstTime=fcstTime,
                    callDate=callDate,
                    mangName = mangName,
                    sidoName = sidoName,
                    so2Value = so2Value,
                    coValue = coValue,
                    o3Value = o3Value,
                    no2Value = no2Value,
                    pm10Value = pm10Value,
                    pm10Value24 = pm10Value24,
                    pm25Value = pm25Value,
                    pm25Value24 = pm25Value24,
                    khaiValue = khaiValue,
                    khaiGrade = khaiGrade,
                    so2Grade = so2Grade,
                    o3Grade = o3Grade,
                    no2Grade = no2Grade,
                    pm10Grade = pm10Grade,
                    pm25Grade = pm25Grade,
                    pm10Grade1h = pm10Grade1h,
                    pm25Grade1h = pm25Grade1h,
                    so2Flag = so2Flag,
                    coFlag = coFlag,
                    o3Flag = o3Flag,
                    no2Flag = no2Flag,
                    pm10Flag = pm10Flag,
                    pm25Flag = pm25Flag,
                )
                db.add(AirKoreaDustData)
            else:
                check_data.uniqueVal = uniqueVal,
                check_data.dustStationIdx = dustStationIdx,
                check_data.dustStationName = dustStationName,
                check_data.dustStationCode = dustStationCode,
                check_data.fcstRealDate = fcstRealDate,
                check_data.fcstDate = fcstDate,
                check_data.fcstTime = fcstTime,
                check_data.callDate = callDate,
                check_data.mangName = mangName,
                check_data.sidoName = sidoName,
                check_data.so2Value = so2Value,
                check_data.coValue = coValue,
                check_data.o3Value = o3Value,
                check_data.no2Value = no2Value,
                check_data.pm10Value = pm10Value,
                check_data.pm10Value24 = pm10Value24,
                check_data.pm25Value = pm25Value,
                check_data.pm25Value24 = pm25Value24,
                check_data.khaiValue = khaiValue,
                check_data.khaiGrade = khaiGrade,
                check_data.so2Grade = so2Grade,
                check_data.o3Grade = o3Grade,
                check_data.no2Grade = no2Grade,
                check_data.pm10Grade = pm10Grade,
                check_data.pm25Grade = pm25Grade,
                check_data.pm10Grade1h = pm10Grade1h,
                check_data.pm25Grade1h = pm25Grade1h,
                check_data.so2Flag = so2Flag,
                check_data.coFlag = coFlag,
                check_data.o3Flag = o3Flag,
                check_data.no2Flag = no2Flag,
                check_data.pm10Flag = pm10Flag,
                check_data.pm25Flag = pm25Flag,
            db.commit()
        db.close()
    def time_change(self, dateTime):
        now = datetime.now()
        fcstRealDate = f"{dateTime}:00"
        fcstDate = dateTime[0:11]
        fcstTime = f"{dateTime[11:]}:00"
        callDate = now.strftime('%Y-%m-%d %H:%M:%S')
        return fcstRealDate, fcstDate, fcstTime, callDate

    def get_station_data(self, stationName):
        db = SessionLocal()
        check_data = db.query(AirKoreaDustStationModel).filter_by(stationName=stationName).first()
        db.close()
        return check_data.id, check_data.stationName
def delete_old_dust_data():
    db = SessionLocal()
    # 3일 이전의 날짜 계산
    three_days_ago = datetime.now() - timedelta(days=3)
    # 삭제 쿼리 실행
    db.query(AirKoreaDustDataModel).filter(AirKoreaDustDataModel.fcstRealDate < three_days_ago).delete()
    db.commit()
    db.close()

if __name__ == "__main__":
    start = time.time()
    AirKoreaDustDataColletor()
    end = time.time()
    print(f"에어코리아 전국 대기질 정보 time = {end - start}s")

    start = time.time()
    delete_old_dust_data()
    end = time.time()
    print(f"예전데이터 삭제 time = {end - start}s")