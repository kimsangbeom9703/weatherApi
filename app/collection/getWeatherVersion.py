##
# 단기예보정보조회서비스 각각의 오퍼레이션(초단기실황, 초단기예보, 단기예보)들의 수정된 예보 버전을 파악하기 위해 예보버전을 조회하는 기능
# URL : http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getFcstVersion
# -ODAM: 초단기실황
# -VSRT: 초단기예보
# -SHRT: 단기예보
# ##
import pprint
import sys
from os import path
from datetime import datetime, timedelta

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.config import settings

import requests


class WeatherVersionDataCollector:
    def __init__(self, type):
        self.url = settings.GET_VERSION_URL
        self.serviceKey = settings.SERVICE_KEY
        self.callType = type
        self.baseDateTime = self.calculate_base_date_time()
        print(self.baseDateTime)
        self.call_api_data()

    def calculate_base_date_time(self):
        now = datetime.now()
        print(now)
        if (self.callType == 'VSRT'):
            if now.minute <= 45:
                if now.hour == 0:
                    base_date = (now - timedelta(days=1)).strftime('%Y%m%d')
                    base_time = '2300'
                    base_datetime = base_date + base_time
                else:
                    base_date = now.strftime('%Y%m%d')
                    base_time = (now - timedelta(hours=1)).strftime('%H30')
                    base_datetime = base_date + base_time
            else:
                base_datetime = now.strftime('%Y%m%d%H30')
        else:
            base_datetime = now.strftime('%Y%m%d%H%M')
        return base_datetime

    def call_api_data(self):
        params = {
            'serviceKey': self.serviceKey,
            'basedatetime': self.baseDateTime,
            'ftype': self.callType,
            'pageNo': '1',
            'numOfRows': '10',
            'dataType': 'JSON'
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        response = requests.get(self.url, params=params, verify=False, headers=headers)
        pprint.pp(response.json())


if __name__ == "__main__":
    WeatherVersionDataCollector('VSRT')
    WeatherVersionDataCollector('SHRT')
