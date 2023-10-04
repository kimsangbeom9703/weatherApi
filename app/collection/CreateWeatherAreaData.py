##
# area_code 중 날씨 정보를 수집할 지역을 weather_area_data 에 삽입
# 삽입시 같은 x,y 좌표가 있을 경우 메모에 , 업데이트
# ex x = 30 , y = 120 , memo = 경기도 부천시 소사구 , 경기도 부천시 원미구
# ##
import pprint

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import case, func
import time
import sys
import requests
from requests.exceptions import RequestException
from os import path
from datetime import datetime, timedelta

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.config import settings

from db.session import SessionLocal

from db.models.areaModel import AreaDataModel
from db.models.weatherAreaModel import WeatherAreaModel


class WeatherAreaDataSave:
    def __init__(self):
        self.get_area_data()
        pass

    def get_area_data(self):
        db = SessionLocal()
        combined_levels = func.concat_ws('>',
                                         case((AreaDataModel.level1.isnot(None), AreaDataModel.level1)),
                                         case((AreaDataModel.level2.isnot(None), AreaDataModel.level2)),
                                         case((AreaDataModel.level3.isnot(None), AreaDataModel.level3))
                                         )
        area_data = (
            db.query(
                case(
                    (AreaDataModel.level2.is_(None) & AreaDataModel.level3.is_(None), AreaDataModel.level1),
                    else_=None
                ).label('is_level_1'),combined_levels.label('combined_levels'), AreaDataModel.grid_x,AreaDataModel.grid_y)
            .all()
        )

        db.close()
        print(area_data)
        self.save_weather_area_data(area_data)

    def save_weather_area_data(self, area_data):
        db = SessionLocal()
        for item in area_data:
            now = datetime.now()
            combined_levels = item.combined_levels
            gridX = item.grid_x
            gridY = item.grid_y
            level_1 = item.is_level_1
            print(combined_levels)
            check_data = (
                db.query(WeatherAreaModel).filter(WeatherAreaModel.grid_x == gridX,
                                                  WeatherAreaModel.grid_y == gridY).first()
            )
            if not check_data:
                if item.is_level_1 is not None:
                    WeatherAreaData = WeatherAreaModel(
                        grid_x=gridX,
                        grid_y=gridY,
                        level_1=level_1,
                        memo=combined_levels,
                        created_at=now.strftime('%Y-%m-%d %H:%M:%S'),
                        area_cnt=1,
                        used=0
                    )
                else:
                    WeatherAreaData = WeatherAreaModel(
                        grid_x=gridX,
                        grid_y=gridY,
                        memo=combined_levels,
                        created_at=now.strftime('%Y-%m-%d %H:%M:%S'),
                        area_cnt=1,
                        used=0
                    )
                db.add(WeatherAreaData)
            else:
                combined_value = f"{check_data.memo}, {combined_levels}"
                check_data.area_cnt = (check_data.area_cnt + 1)
                check_data.memo = combined_value
                check_data.updated_at = now.strftime('%Y-%m-%d %H:%M:%S')
            db.commit()
        db.close()
        self.update_weather_area_data()
    def update_weather_area_data(self):
        db = SessionLocal()
        db.query(WeatherAreaModel).filter(WeatherAreaModel.area_cnt > 1).update({WeatherAreaModel.used: 1})
        db.commit()
        db.close()


if __name__ == "__main__":
    WeatherAreaDataSave()
