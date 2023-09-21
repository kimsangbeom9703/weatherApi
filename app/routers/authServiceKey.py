from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from schemas import authServiceKey

auth_service_key_router = APIRouter(
    prefix="/api/auth/service",  # url 앞에 고정적으로 붙는 경로추가
    tags=["AuthServiceKey"],  # docs tag name
)  # Route 분리

@auth_service_key_router.post("/create/key",response_model=authServiceKey.ServiceKeyCreateOut)  # 키 생성
def index(item:authServiceKey.ServiceKeyCreate):
    item.serviceKey='1'
    return item
