import pprint
import time
import asyncio, aiohttp
import pandas as pd
from datetime import datetime, timedelta

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.config import settings

from db.session import SessionLocal

from db.models.incheonAirportDustStationModel import IncheonAirportDustStationModel
from db.models.incheonAirportDustDataModel import IncheonAirportDustDataModel


class IncheonAirPortDustDataCollector:
    def __init__(self, call_type):
        self.call_type = call_type
        self.service_key = settings.SERVICE_KEY
        self.url = self.get_api_url()
        self.numOfRows = '10'
        self.pageNo = '1'
        self.type = 'json'

    def get_api_url(self):  # API URL 설정을 가져오는 함수
        if self.call_type == 'IN':
            _URL = settings.GET_INCHEON_IN_API_URL
        else:
            _URL = settings.GET_INCHEON_OUT_API_URL
        return _URL

    async def fetch_data_with_retry(self, session, max_retries=3):
        params = {
            'serviceKey': self.service_key,
            'numOfRows': self.numOfRows,
            'pageNo': self.pageNo,
            'type': self.type,
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }
        retry_count = 0
        while retry_count < max_retries:
            try:
                async with session.get(self.url, params=params, headers=headers) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        status = response_data['response']['header']['resultCode']
                        if (status == '00'):
                            df = pd.DataFrame(response_data['response']['body']['items'])
                            self.save_dust_data(df)
                        await asyncio.sleep(1)
                        break
                    else:
                        print(f"Status code: {response.status}")

            except aiohttp.ClientError as e:  # aiohttp 예외로 변경
                print(f"Request failed: {str(e)}")
                retry_count += 1
                wait_time = 2 ** retry_count  # 지수 백오프를 사용한 재시도 간격 설정
                await asyncio.sleep(wait_time)

    def save_dust_data(self, dust_data):
        db = SessionLocal()
        if self.call_type == 'IN':
            self.in_data_save(db, dust_data)
        else:
            self.out_data_save(db,dust_data)
        db.close()

    def time_change(self, rtime):
        now = datetime.now()
        fcstRealDateFormat = f"{rtime}0000"
        fcstRealDate = datetime.strptime(fcstRealDateFormat, '%Y%m%d%H%M%S')
        fcstDateBasic = rtime[0:8]
        fcstDate = f"{fcstDateBasic[:4]}-{fcstDateBasic[4:6]}-{fcstDateBasic[6:]}"
        fcstTime = f"{rtime[8:]}:00:00"
        callDate = now.strftime('%Y-%m-%d %H:%M:%S')
        return fcstRealDate, fcstDate, fcstTime, callDate

    def in_data_save(self, db, data):
        for index, row in data.iterrows():
            dustStationIdx, dustStationName, type = self.get_station_data(row['terminalid'])
            fcstRealDate, fcstDate, fcstTime, callDate = self.time_change(row['rtime'])
            locationId = row['terminalid']
            co2 = row['co2']
            pm10 = row['pm10']
            pm2_5 = row['pm2_5']
            co = row['co']
            no2 = row['no2']
            uniqueVal = f"{fcstRealDate}_{dustStationIdx}"

            check_data = (
                db.query(IncheonAirportDustDataModel).filter(
                    IncheonAirportDustDataModel.uniqueVal == uniqueVal).first()
            )
            if not check_data:
                IncheonAirportDustData = IncheonAirportDustDataModel(
                    uniqueVal=uniqueVal,
                    dustStationIdx=dustStationIdx,
                    dustStationName=dustStationName,
                    fcstRealDate=fcstRealDate,
                    fcstDate=fcstDate,
                    fcstTime=fcstTime,
                    callDate=callDate,
                    locationId=locationId,
                    type=type,
                    co=co,
                    co2=co2,
                    no2=no2,
                    pm10=pm10,
                    pm2_5=pm2_5
                )
                db.add(IncheonAirportDustData)
            else:
                check_data.uniqueVal = uniqueVal,
                check_data.dustStationIdx = dustStationIdx,
                check_data.dustStationName = dustStationName,
                check_data.fcstRealDate = fcstRealDate,
                check_data.fcstDate = fcstDate,
                check_data.fcstTime = fcstTime,
                check_data.callDate = callDate,
                check_data.locationId = locationId,
                check_data.type = type,
                check_data.co = co,
                check_data.co2 = co2,
                check_data.no2 = no2,
                check_data.pm10 = pm10,
                check_data.pm2_5 = pm2_5
            db.commit()

    def out_data_save(self, db, data):
        for index, row in data.iterrows():
            dustStationIdx, dustStationName, type = self.get_station_data(row['locationid'])
            fcstRealDate, fcstDate, fcstTime, callDate = self.time_change(row['rtime'])
            locationId = row['locationid']
            so2 = row['so2']
            no2 = row['no2']
            pm10 = row['pm10']
            pm2_5 = row['pm2_5']
            co = row['co']
            o3 = row['o3']

            uniqueVal = f"{fcstRealDate}_{dustStationIdx}"

            check_data = (
                db.query(IncheonAirportDustDataModel).filter(
                    IncheonAirportDustDataModel.uniqueVal == uniqueVal).first()
            )
            if not check_data:
                IncheonAirportDustData = IncheonAirportDustDataModel(
                    uniqueVal=uniqueVal,
                    dustStationIdx=dustStationIdx,
                    dustStationName=dustStationName,
                    fcstRealDate=fcstRealDate,
                    fcstDate=fcstDate,
                    fcstTime=fcstTime,
                    callDate=callDate,
                    locationId=locationId,
                    type=type,
                    co=co,
                    no2=no2,
                    pm10=pm10,
                    pm2_5=pm2_5,
                    so2=so2,
                    o3=o3,
                )
                db.add(IncheonAirportDustData)
            else:
                check_data.uniqueVal = uniqueVal,
                check_data.dustStationIdx = dustStationIdx,
                check_data.dustStationName = dustStationName,
                check_data.fcstRealDate = fcstRealDate,
                check_data.fcstDate = fcstDate,
                check_data.fcstTime = fcstTime,
                check_data.callDate = callDate,
                check_data.locationId = locationId,
                check_data.type = type,
                check_data.co = co,
                check_data.no2 = no2,
                check_data.pm10 = pm10,
                check_data.pm2_5 = pm2_5
                check_data.so2 = so2,
                check_data.o3 = o3,
            db.commit()

    def get_station_data(self, stationName):
        db = SessionLocal()
        check_data = db.query(IncheonAirportDustStationModel).filter_by(stationName=stationName).first()
        db.close()
        return check_data.id, check_data.stationName, check_data.stationType

    async def main_async(self):  # 비동기 메인 함수
        tasks = []
        connector = aiohttp.TCPConnector(limit=2, ssl=False)  # 연결 수를 조정
        async with aiohttp.ClientSession(connector=connector) as session:  # 클라이언트 세션 재사용
            task = asyncio.ensure_future(self.fetch_data_with_retry(session))
            tasks.append(task)
            await asyncio.gather(*tasks)

def delete_old_dust_data():
    db = SessionLocal()
    # 3일 이전의 날짜 계산
    three_days_ago = datetime.now() - timedelta(days=3)
    # 삭제 쿼리 실행
    db.query(IncheonAirportDustDataModel).filter(IncheonAirportDustDataModel.fcstRealDate < three_days_ago).delete()
    db.commit()
    db.close()


if __name__ == "__main__":
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)

    # 실내 대기질 정보
    start = time.time()
    collector = IncheonAirPortDustDataCollector('IN')
    loop.run_until_complete(collector.main_async())
    end = time.time()
    print(f"실내 대기질 time = {end - start}s")

    # 실외 대기질 정보
    start = time.time()
    collector = IncheonAirPortDustDataCollector('OUT')
    loop.run_until_complete(collector.main_async())
    end = time.time()
    print(f"실외 대기질 time = {end - start}s")

    loop.close()

    start = time.time()
    delete_old_dust_data()
    end = time.time()
    print(f"예전데이터 삭제 time = {end - start}s")
