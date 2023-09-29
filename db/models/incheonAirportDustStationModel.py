from sqlalchemy import Column, VARCHAR, DATETIME, Integer
from db.session import Base


class IncheonAirportDustStationModel(Base):
    __tablename__ = "incheon_airport_fine_dust_station"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    stationName = Column(VARCHAR(45), nullable=False, comment='측정소 이름')
    stationType = Column(VARCHAR(45), nullable=False, comment='실내 / 실외')
