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
from db.models.airKoreaDustStationModel import AirKoreaDustStationModel


class AirKoreaDustStationColletor:
    def __init__(self):
        self.url = settings.AIR_KOREA_DUST_STATION_URL
        self.service_key = settings.SERVICE_KEY
        self.returnType = 'json'
        self.pageNo = '1'
        self.numOfRows = '1000'

        self.call_api_data()

    def call_api_data(self, max_retries=3):
        params = {
            'serviceKey': self.service_key,
            'returnType': self.returnType,
            'pageNo': self.pageNo,
            'numOfRows': self.numOfRows,
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
        now = datetime.now()
        for index, row in data.iterrows():
            stationName = row['stationName']
            addr = row['addr']
            year = row['year']
            items = row['item']
            mangName = row['mangName']
            dmX = row['dmX']
            dmY = row['dmY']
            callDate = now.strftime('%Y-%m-%d %H:%M:%S')
            check_data = (
                db.query(AirKoreaDustStationModel).filter(
                    AirKoreaDustStationModel.stationName == stationName).first()
            )
            if not check_data:
                AirKoreaDustStationData = AirKoreaDustStationModel(
                    stationName=stationName,
                    addr=addr,
                    year=year,
                    items=items,
                    mangName=mangName,
                    dmX=dmX,
                    dmY=dmY,
                    callDate=callDate,
                )
                db.add(AirKoreaDustStationData)
            else:
                check_data.stationName = stationName,
                check_data.addr = addr,
                check_data.year = year,
                check_data.items = items,
                check_data.mangName = mangName,
                check_data.dmX = dmX,
                check_data.dmY = dmY,
                check_data.callDate = callDate,
            db.commit()
        db.close()


if __name__ == "__main__":
    start = time.time()
    AirKoreaDustStationColletor()
    end = time.time()
    print(f"에어코리아 측정소 정보 time = {end - start}s")
