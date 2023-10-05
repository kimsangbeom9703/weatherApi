from typing import Optional
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from enum import Enum


class ServiceKeyList(BaseModel):
    serviceKey: str = Field(..., example="testa78e-3b13-422f-8695-9bb2106e5c35")
    serviceType: str = Field(..., example="ALL")
    description: Optional[str] = Field(None, example='채용학습솔루션 Service key Call')
    created_at: datetime = Field(None, example='2023-09-26 15:52:19')
    expires_at: datetime = Field(None, example='2023-10-05 18:00:00')


class ServiceKeyBase(BaseModel):
    serviceTypeId: int = Field(..., example=2)
    serviceType: str = Field(..., example="INCHEON")
    description: Optional[str] = Field(None, example='인천공항 대기질 데이터 요청합니다.')
    expires_at: Optional[datetime] = Field(None, example='2023-09-21 18:00:00')


class ServiceKeyCreate(ServiceKeyBase):
    pass


class ServiceKeyCreateOut(ServiceKeyBase):
    id: int
    serviceKey: UUID
    created_at: datetime


class ResponseModel(BaseModel):
    status: str
    statusCode: int
    errorMsg: Optional[str] = None
    data: ServiceKeyCreateOut
