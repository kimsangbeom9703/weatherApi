from sqlalchemy import Column, Integer, TEXT, TIMESTAMP , VARCHAR
from db.session import Base
class WeatherAreaModel(Base):
    __tablename__ = "weather_area_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    grid_x = Column(Integer,nullable=False,comment='격자 x 좌표')
    grid_y = Column(Integer,nullable=False,comment='격자 y 좌표')
    level_1 = Column(VARCHAR(45), nullable=True, comment='격자 y 좌표')
    area_cnt = Column(Integer, nullable=True, comment='지역 갯수')
    memo = Column(TEXT, nullable=True,comment='메모')
    used = Column(Integer, nullable=False, comment='임시 상태값 개발계정 승인시 제거 1 이 호출')
    created_at = Column(TIMESTAMP, nullable=True,comment='생성 시간')
    updated_at = Column(TIMESTAMP, nullable=True,comment='업데이트 시간')
    deleted_at = Column(TIMESTAMP, nullable=True,comment='삭제 시간')
