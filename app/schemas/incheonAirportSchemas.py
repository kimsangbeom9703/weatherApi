from typing import Optional
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from enum import Enum


class IncheonAirportBase(BaseModel):
    dustStationName: str = Field(..., example="T1/T2/탑승동/자유무역지역/남북동/을왕동")

class ResponseModel(BaseModel):
    status: str
    statusCode: int
    errorMsg: Optional[str] = None
    data: IncheonAirportBase

