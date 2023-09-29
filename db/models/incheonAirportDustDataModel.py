from sqlalchemy import Column, VARCHAR, DATETIME, Integer
from db.session import Base


class IncheonAirportDustDataModel(Base):
    __tablename__ = "incheon_airport_fine_dust"

    # id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    uniqueVal = Column(VARCHAR(45),primary_key=True, nullable=False, comment='유니크값')
    dustStationIdx = Column(Integer, nullable=False, comment='측정소 id')
    dustStationName = Column(VARCHAR(45), nullable=False, comment='측정소 이름')

    fcstRealDate = Column(VARCHAR(45), nullable=False, comment='예측일')
    fcstDate = Column(VARCHAR(45), nullable=False, comment='예측일자')
    fcstTime = Column(VARCHAR(45), nullable=False, comment='예측시간')
    callDate = Column(DATETIME, nullable=False, comment='호출시간')

    locationId = Column(VARCHAR(45), nullable=False, comment='위치')
    type = Column(VARCHAR(45), nullable=False, comment='실내 = in / 실외 = out')
    co = Column(VARCHAR(45), nullable=True, comment='일산화탄소')
    co2 = Column(VARCHAR(45), nullable=True, comment='이산화탄소')
    no2 = Column(VARCHAR(45), nullable=True, comment='이산화질소')
    o3 = Column(VARCHAR(45), nullable=True, comment='오존')
    so2 = Column(VARCHAR(45), nullable=True, comment='아황산가스')
    pm10 = Column(VARCHAR(45), nullable=True, comment='미세먼지')
    pm2_5 = Column(VARCHAR(45), nullable=True, comment='초미세먼지')
