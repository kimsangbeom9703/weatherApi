from typing import Optional
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel


class ServiceKeyBase(BaseModel):
    serviceTypeId: int
    serviceType: str
    description: Optional[str] = None
    expires_at: Optional[datetime] = None

    # serviceKey : UUID
    # serviceTypeId: int
    # serviceType: str
    # description: Optional[str] = None
    # created_at: Optional[datetime] = None
    # expires_at: Optional[datetime] = None
    # is_active: Optional[int] = None
    # class Config:
    #     orm_mode = True
    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "serviceTypeId": '1',
    #             "serviceType": 'ALL/INCHEON/WEATHER/AIRKOREA',
    #         }
    #     }


class ServiceKeyCreate(ServiceKeyBase):
    pass


class ServiceKeyCreateOut(ServiceKeyBase):
    serviceType: str
    serviceKey: UUID
    created_at: datetime


