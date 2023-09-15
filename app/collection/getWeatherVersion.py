##
# 단기예보정보조회서비스 각각의 오퍼레이션(초단기실황, 초단기예보, 단기예보)들의 수정된 예보 버전을 파악하기 위해 예보버전을 조회하는 기능
# URL : http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getFcstVersion
# -ODAM: 초단기실황
# -VSRT: 초단기예보
# -SHRT: 단기예보
# ##
import pprint
import sys
import requests

from os import path
from datetime import datetime, timedelta

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.config import settings

from db.session import SessionLocal
from db.models.weatherVersionModel import WeatherVersion


class WeatherVersionDataCollector:
    def __init__(self, call_type):
        self.url = settings.GET_VERSION_URL
        self.service_key = settings.SERVICE_KEY
        self.call_type = call_type
        self.base_date_time = self.calculate_base_date_time()
        self.call_api_data()

    def calculate_base_date_time(self):
        now = datetime.now()
        if self.call_type == 'VSRT':
            if now.minute <= 45:
                if now.hour == 0:
                    base_date = (now - timedelta(days=1)).strftime('%Y%m%d')
                    base_time = '2300'
                else:
                    base_date = now.strftime('%Y%m%d')
                    base_time = (now - timedelta(hours=1)).strftime('%H30')
            else:
                base_date = now.strftime('%Y%m%d')
                base_time = now.strftime('%H30')
        else:
            base_times = ['0210', '0510', '0810', '1110', '1410', '1710', '2010', '2310']
            current_time = now.time()
            closest_time = min(base_times, key=lambda x: (current_time.hour - int(x[:2])) ** 2 + (
                    current_time.minute - int(x[2:])) ** 2)
            base_date = now.strftime('%Y%m%d')
            base_time = closest_time
        return base_date + base_time

    def call_api_data(self):
        params = {
            'serviceKey': self.service_key,
            'basedatetime': self.base_date_time,
            'ftype': self.call_type,
            'pageNo': '1',
            'numOfRows': '10',
            'dataType': 'JSON'
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        response = requests.get(self.url, params=params, verify=False, headers=headers)
        res_data = response.json()
        self.data_save(res_data)

    def data_save(self, res):
        status = res['response']['header']['resultCode']
        status_str = res['response']['header']['resultMsg']
        items = res['response']['body']['items']['item']
        if not items:
            version = '00000000000'
        else:
            item = items[0]
            version = item['version']
        db = SessionLocal()
        try:
            if status == '00':
                existing_version = db.query(WeatherVersion).filter_by(used=1, type=self.call_type, version=version).first()
                if not existing_version:
                    weather_version = WeatherVersion(
                        status=status,
                        status_str=status_str,
                        type=self.call_type,
                        version=version,
                        call_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                        datetime=self.base_date_time,
                        used=0
                    )
                    db.add(weather_version)
                    db.commit()
            else:
                weather_version = WeatherVersion(
                    status=status,
                    status_str=status_str,
                    type=self.call_type,
                    version='00000000000',
                    call_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                    datetime=self.base_date_time,
                    used=0
                )
                db.add(weather_version)
                db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()

if __name__ == "__main__":
    WeatherVersionDataCollector('VSRT')
    WeatherVersionDataCollector('SHRT')