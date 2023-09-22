from sqlalchemy import Column, VARCHAR, DATETIME, Integer
from db.session import Base


class WeatherVersionModel(Base):
    __tablename__ = "weather_version"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    status = Column(Integer, nullable=False, comment='상태값 / success 00')
    status_str = Column(VARCHAR(45), nullable=False, comment='상태값 설명')
    type = Column(VARCHAR(45), nullable=False, comment='VSRT : 초단기예보 , ODAM : 초단기실황 , SHRT : 단기예보')
    version = Column(VARCHAR(45), nullable=False, comment='버전 정보')
    call_datetime = Column(DATETIME, nullable=False, comment='호출 시간')
    datetime = Column(VARCHAR(45), nullable=False, comment='api 입력시간')
    used = Column(Integer, nullable=False, comment='수집시 체크',default=0)
