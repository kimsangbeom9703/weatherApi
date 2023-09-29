from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from crud import crud_get

from db.models.areaModel import AreaDataModel
from db.models.incheonAirportDustDataModel import IncheonAirportDustDataModel
from db.models.incheonAirportDustStationModel import IncheonAirportDustStationModel

import json

def getAreaAllData(db):
    return crud_get.getAreaListAllData(db)


def getDustStationAllData(db, page, size):
    total, _list = crud_get.get_all_data(db, IncheonAirportDustStationModel, skip=page * size, limit=size)
    return total,_list


# 시간대 별 6개 측정소 데이터 노출
def getDustStationDataByTime(db, current_tiem=None):
    return_data = crud_get.get_all_station_data_by_time(db, IncheonAirportDustDataModel, current_tiem)
    if return_data == []:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="not Data",
        )
    return return_data

# 해당 측정소 시간대 별 대이터 노출
def getDustStationDataAll(station_name,orderby,db, page, size):
    total, _list = crud_get.get_station_dust_all_data(station_name,orderby,db, IncheonAirportDustDataModel, skip=page * size, limit=size)
    return total,_list

# 해당 측정소 가장 가까운 시간의 데이터
def getDustStationDataFirst(db,station_name):
    return_data = crud_get.get_all_station_data_first(db, IncheonAirportDustDataModel, station_name)
    if return_data is None:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="not Data",
        )
    return return_data