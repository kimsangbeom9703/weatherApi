from sqlalchemy import Column, VARCHAR, DATETIME, Integer
from db.session import Base


class AirKoreaDustDataModel(Base):
    __tablename__ = "airkorea_dust_data"

    uniqueVal = Column(VARCHAR(45), primary_key=True, index=True, comment='유니크값')
    dustStationIdx = Column(Integer,primary_key=True, nullable=False, comment='측정소 id')
    dustStationName = Column(VARCHAR(45), nullable=False, comment='측정소 이름')
    dustStationCode = Column(VARCHAR(45), nullable=False, comment='api에서 제공되는 코드')

    fcstRealDate = Column(VARCHAR(45), nullable=True, comment='예측일')
    fcstDate = Column(VARCHAR(45), nullable=False, comment='예측일자')
    fcstTime = Column(VARCHAR(45), nullable=False, comment='예측시간')
    callDate = Column(VARCHAR(45), nullable=False, comment='호출시간')

    mangName = Column(VARCHAR(45), nullable=False, comment='측정망 정보')
    sidoName = Column(VARCHAR(45), nullable=False, comment='시도 이름')
    so2Value = Column(VARCHAR(45), nullable=False, comment='아황산가스')
    coValue = Column(VARCHAR(45), nullable=False, comment='일산화탄소 농도')
    o3Value = Column(VARCHAR(45), nullable=False, comment='오존 농도')
    no2Value = Column(VARCHAR(45), nullable=False, comment='이산화질소 농도')
    pm10Value = Column(VARCHAR(45), nullable=False, comment='미세먼지(pm10)')
    pm10Value24 = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM10)24시간예측이동농도')
    pm25Value = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM2.5)')
    pm25Value24 = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM2.5)24시간예측이동농도')
    khaiValue = Column(VARCHAR(45), nullable=False, comment='통합대기환경수치')
    khaiGrade = Column(VARCHAR(45), nullable=False, comment='통합대기환경지수')
    so2Grade = Column(VARCHAR(45), nullable=False, comment='아황산가스 지수')
    o3Grade = Column(VARCHAR(45), nullable=False, comment='오존 지수')
    no2Grade = Column(VARCHAR(45), nullable=False, comment='이산화질소 지수')
    pm10Grade = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM10) 24시간 등급자료')
    pm25Grade = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM2.5) 24시간 등급자료')
    pm10Grade1h = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM10) 1시간 등급자료')
    pm25Grade1h = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM2.5) 1시간 등급자료')
    so2Flag = Column(VARCHAR(45), nullable=False, comment='아황산가스 플래그')
    coFlag = Column(VARCHAR(45), nullable=False, comment='일산화탄소 플래그')
    o3Flag = Column(VARCHAR(45), nullable=False, comment='오존 플래그')
    no2Flag = Column(VARCHAR(45), nullable=False, comment='이산화질소 플래그')
    pm10Flag = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM10) 플래그')
    pm25Flag = Column(VARCHAR(45), nullable=False, comment='미세먼지(PM2.5) 플래그')


