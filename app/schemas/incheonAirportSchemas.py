from typing import Optional, List
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from enum import Enum


class IncheonAirportBase(BaseModel):
    # id: int = Field(..., example="1")
    stationName: str = Field(..., example="T1/T2/탑승동/자유무역지역/남북동/을왕동")
    stationType: str = Field(..., example="IN/OUT")


class IncheonAirPortDustBase(BaseModel):
    # uniqueVal: str = Field(..., example="유니크 값")
    # dustStationIdx: int = Field(..., example="측정소 id")
    dustStationName: str = Field(..., example="측정소 이름")
    fcstRealDate: str = Field(..., example="예측일")
    fcstDate: str = Field(..., example="예측일자")
    fcstTime: str = Field(..., example="예측시간")
    callDate: datetime = Field(..., example="호출시간")
    # locationId: str = Field(..., example="위치")
    type: str = Field(..., example="실내 = in / 실외 = out")
    co: str = Field(..., example="일산화탄소")
    co2: Optional[str] = Field(None, example="이산화탄소")
    no2: str = Field(..., example="이산화질소")
    o3: Optional[str] = Field(None, example="오존")
    so2: Optional[str] = Field(None, example="아황산가스")
    pm10: str = Field(..., example="미세먼지")
    pm2_5: str = Field(..., example="초미세먼지")


class ResponseFirstDataModel(BaseModel):
    status: str
    statusCode: int
    errorMsg: Optional[str] = None
    data: IncheonAirPortDustBase


class ResponseDataModel(BaseModel):
    status: str
    statusCode: int
    errorMsg: Optional[str] = None
    data: List[IncheonAirPortDustBase]


class ResponseStationDataModel(BaseModel):
    status: str
    statusCode: int
    total: int
    errorMsg: Optional[str] = None
    data: List[IncheonAirPortDustBase]

class ResponseStationModel(BaseModel):
    status: str
    statusCode: int
    total: int
    errorMsg: Optional[str] = None
    data: List[IncheonAirportBase]
