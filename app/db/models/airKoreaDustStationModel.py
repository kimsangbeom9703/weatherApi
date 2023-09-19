from sqlalchemy import Column, VARCHAR, DATETIME, Integer
from db.session import Base


class AirKoreaDustStationModel(Base):
    __tablename__ = "airkorea_dust_station"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    stationName = Column(VARCHAR(45),primary_key=True, nullable=False, comment='측정소')
    addr = Column(VARCHAR(512), nullable=False, comment='주소')
    items = Column(VARCHAR(45), nullable=False, comment='측정값')
    year = Column(VARCHAR(45), nullable=True, comment='설치날짜')
    mangName = Column(VARCHAR(45), nullable=False, comment='측정망')
    dmX = Column(VARCHAR(45), nullable=False, comment='x좌표')
    dmY = Column(VARCHAR(45), nullable=False, comment='y좌표')
    callDate = Column(DATETIME, nullable=False, comment='호출시간')
