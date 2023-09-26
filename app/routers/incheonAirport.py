import pprint

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from sqlalchemy.orm import Session
from db.connection import get_db

from uuid import UUID

from apis import incheonAirportApi, authServiceKeyApi

incheon_airport_router = APIRouter(
    prefix="/api/airport",  # url 앞에 고정적으로 붙는 경로추가
    tags=["IncheonAirPortDust"],  # docs tag name
    # include_in_schema=False
)  # Route 분리


# @incheon_airport_router.get("/")  # Route Path
# def index(db: Session = Depends(get_db)):
#     res = incheonAirportApi.getDustAllData(db=db)  # apis 호출
#     return {
#         "res": res,
#     }  # 결과
def get_api_key(api_key_header: str = Depends(APIKeyHeader(name="API-KEY")), db: Session = Depends(get_db)):
    authServiceManager = authServiceKeyApi.AuthServiceKeyManager(db=db)
    api_key_header = authServiceManager.checkServiceKey(api_key_header, 'INCHEON')
    return api_key_header


@incheon_airport_router.get("/station")  # Route Path
def read_station(serviceKeyData: str = Depends(get_api_key), page: int = 0, size: int = 10,
                 db: Session = Depends(get_db)):
    authServiceManager = authServiceKeyApi.AuthServiceKeyManager(db=db)
    logSave = authServiceManager.serviceKeyLogUpdate(serviceKeyData, '/api/airport/station')
    print(logSave.request_count)
    total, _list = incheonAirportApi.getDustStationAllData(db=db, page=page, size=size)  # apis 호출
    return {
        "status": 'success',
        "total": total,
        "data": _list,
    }  # 결과
