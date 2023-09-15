from sqlalchemy import Column, VARCHAR, DECIMAL, Integer, BigInteger, DATE, ForeignKey
from db.session import Base
class AreaData(Base):
    __tablename__ = "a rea_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    area_code = Column(BigInteger,primary_key=True,nullable=False,comment='행정구역 코드')
    level1 = Column(VARCHAR(255),nullable=False,comment='1단계')
    level2 = Column(VARCHAR(255),nullable=False,comment='2단계')
    level3 = Column(VARCHAR(255),nullable=False,comment='3단계')
    grid_x = Column(Integer,nullable=False,comment='격자 x 좌표')
    grid_y = Column(Integer,nullable=False,comment='격자 y 좌표')
    longitude_hour = Column(Integer, nullable=True,comment='경도(시)')
    longitude_minute = Column(Integer, nullable=True,comment='경도(분)')
    longitude_second = Column(Integer, nullable=True,comment='경도(초)')
    latitude_hour = Column(Integer, nullable=True,comment='위도(시)')
    latitude_minute = Column(Integer, nullable=True,comment='위도(분)')
    latitude_second = Column(Integer, nullable=True, comment='위도(초)')
    longitude_second_div100 = Column(DECIMAL(6, 2), nullable=True,comment='경도(초/100)')
    latitude_second_div100 = Column(DECIMAL(6, 2), nullable=True,comment='위도(초/100)')
    document_update_time = Column(DATE, nullable=True,comment='문서 업데이트 시간')
