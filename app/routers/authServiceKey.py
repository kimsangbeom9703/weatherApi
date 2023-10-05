import pprint

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db.connection import get_db

from apis.authServiceKeyApi import AuthServiceKeyManager

from schemas import authServiceKeySchemas

from core.common_utils import new_common_parameters

from typing import  List
auth_service_key_router = APIRouter(
    prefix="/api/auth/service",  # url 앞에 고정적으로 붙는 경로추가
    tags=["서비스인증"],  # docs tag name
)  # Route 분리



#@auth_service_key_router.get("/list", status_code=200)  # 키 생성
@auth_service_key_router.get("/list", response_model=List[authServiceKeySchemas.ServiceKeyList],status_code=200)  # 키 생성
async def list_key(commons: dict = Depends(new_common_parameters), db: Session = Depends(get_db)):
    authServiceManager = AuthServiceKeyManager(db=db)
    authServiceList = authServiceManager.getListData(commons)
    return authServiceList


@auth_service_key_router.post("/create/key", response_model=authServiceKeySchemas.ResponseModel,
                              status_code=200)  # 키 생성
async def create_key(req: authServiceKeySchemas.ServiceKeyCreate, db: Session = Depends(get_db)):
    authServiceManager = AuthServiceKeyManager(db=db)
    authServicekeyStatus = authServiceManager.createAuthServiceKey(req)
    return authServicekeyStatus
