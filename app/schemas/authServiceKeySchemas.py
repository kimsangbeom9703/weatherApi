from typing import Optional
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from enum import Enum


class ServiceKeyList(BaseModel):
    serviceKey: str = Field(..., example="a4090fda-199c-4888-a23d-fea58a82bbf5")
    serviceType: str = Field(..., example="ALL")
    description: Optional[str] = Field(None, example='채용학습솔루션 Service key Call')
    created_at: datetime = Field(None, example='2023-09-26 15:52:19')
    expires_at: datetime = Field(None, example='2023-10-05 18:00:00')


class ServiceKeyBase(BaseModel):
    deviceId: str = Field(..., example="0002db70ff9d9f04892e364db2298915")
    description: Optional[str] = Field(None, example='인천공항 대기질 데이터 요청합니다.')
    expires_at: Optional[datetime] = Field(None, example='2025-09-21 18:00:00')
    referer: Optional[str] = Field(None, example="http://www.test.com/")


class ServiceKeyCreate(ServiceKeyBase):
    serviceTypeId: int = Field(..., example=2)
    serviceType: str = Field(..., example="INCHEON")
    referer: str = Field(..., example="http://www.test.com/")


class ServiceKeyUpdate(ServiceKeyBase):
    serviceKey: UUID = Field(..., example='a4090fda-199c-4888-a23d-fea58a82bbf5')
    status: int = Field(..., example="0")


class ServiceKeyCreateOut(ServiceKeyBase):
    id: int
    serviceKey: UUID
    created_at: datetime
    updated_at: datetime = Field(None)


class ResponseModel(BaseModel):
    status: str
    statusCode: int
    errorMsg: Optional[str] = None
    data: ServiceKeyCreateOut
