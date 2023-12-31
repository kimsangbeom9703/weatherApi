from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import get_db

from apis import area

area_router = APIRouter(
    prefix="/api/area",  # url 앞에 고정적으로 붙는 경로추가
    tags=["area"], # docs tag name
    include_in_schema=False
)  # Route 분리


@area_router.get("/list")  # Route Path
def index(db: Session = Depends(get_db)):
    res = area.listAllData(db=db)  # apis 호출
    return {
        "res": res,
    }  # 결과