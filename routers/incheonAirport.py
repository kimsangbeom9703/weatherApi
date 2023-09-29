from fastapi import APIRouter, Depends, Body
from fastapi.security import APIKeyHeader

from sqlalchemy.orm import Session
from db.connection import get_db

from apis import incheonAirportApi, authServiceKeyApi

from schemas import incheonAirportSchemas

from core.common_utils import serviceKeyLogUpdate, get_current_time, common_parameters
import json

incheon_airport_router = APIRouter(
    prefix="/api/incheon-airport",  # url 앞에 고정적으로 붙는 경로추가
    tags=["인천공항 대기질 정보"],  # docs tag name
    # include_in_schema=False
)  # Route 분리

AUTH_KEY_PATH = 'INCHEON'


def get_api_key(api_key_header: str = Depends(APIKeyHeader(name="API-KEY")), db: Session = Depends(get_db)):
    authServiceManager = authServiceKeyApi.AuthServiceKeyManager(db=db)
    api_key_header = authServiceManager.checkServiceKey(api_key_header, AUTH_KEY_PATH)
    return api_key_header


@incheon_airport_router.get("/station", response_model=incheonAirportSchemas.ResponseStationModel)
def read_station(serviceKeyData: str = Depends(get_api_key), commons: dict = Depends(common_parameters),
                 db: Session = Depends(get_db)):
    serviceKeyLogUpdate(db, serviceKeyData, '/api/airport/station')
    total, _list = incheonAirportApi.getDustStationAllData(db=db, page=commons['skip'],
                                                           size=commons['limit'])  # apis 호출
    return {
        "status": 'success',
        "statusCode": 200,
        "total": total,
        "data": _list,
    }  # 결과


# 시간대 별 6개 측정소 데이터 노출 ( 시간 값이 없다면 현재 시간과 가장 가까운 시간의 데이터)
@incheon_airport_router.get("/air-quality", response_model=incheonAirportSchemas.ResponseDataModel)
def read_dust_all(current_time: str = get_current_time(), serviceKeyData: str = Depends(get_api_key),
                  db: Session = Depends(get_db)):
    serviceKeyLogUpdate(db, serviceKeyData, '/api/airport/air-quality')
    results = incheonAirportApi.getDustStationDataByTime(db, current_time)
    return {
        "status": 'success',
        "statusCode": 200,
        "data": results,
    }  # 결과


# 해당 측정소 시간대 별 대이터 노출
@incheon_airport_router.get("/air-quality-all-data", response_model=incheonAirportSchemas.ResponseStationDataModel)
def read_dust_station_all(station_name: str,orderby : str = 'desc', serviceKeyData: str = Depends(get_api_key),
                          commons: dict = Depends(common_parameters), db: Session = Depends(get_db)):
    serviceKeyLogUpdate(db, serviceKeyData, '/api/airport/air-quality-all-data')
    total, _list = incheonAirportApi.getDustStationDataAll(station_name,orderby,db=db, page=commons['skip'],size=commons['limit'])  # apis 호출
    return {
        "status": 'success',
        "statusCode": 200,
        "total": total,
        "data": _list,
    }  # 결과

# 해당 측정소 가장 가까운 시간의 데이터
@incheon_airport_router.get("/air-quality-first", response_model=incheonAirportSchemas.ResponseFirstDataModel)
def read_dust_station_first(station_name: str, serviceKeyData: str = Depends(get_api_key), db: Session = Depends(get_db)):
    serviceKeyLogUpdate(db, serviceKeyData, '/api/airport/air-quality-first')
    results = incheonAirportApi.getDustStationDataFirst(db,station_name)
    return {
        "status": 'success',
        "statusCode": 200,
        "data": results,
    }  # 결과