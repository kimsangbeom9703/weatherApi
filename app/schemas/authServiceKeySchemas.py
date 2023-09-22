from typing import Optional
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from enum import Enum




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
