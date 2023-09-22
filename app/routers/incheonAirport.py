from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import get_db

from uuid import UUID

from apis import incheonAirportApi

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

@incheon_airport_router.get("/station")  # Route Path
def read_station(serviceKey:UUID,page: int = 0, size: int = 10,db: Session = Depends(get_db)):
    total,_list = incheonAirportApi.getDustStationAllData(db=db,page=page,size=size)  # apis 호출
    return {
        "total": total,
        "data": _list,
    }  # 결과
