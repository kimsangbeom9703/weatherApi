from sqlalchemy import Column, VARCHAR, Integer , DATETIME,TEXT,ForeignKey
from db.session import Base


class CollectionWeatherModel(Base):
    __tablename__ = "auth_api_service_log"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    serviceKey = Column(VARCHAR(90),ForeignKey("auth_api_service_key.serviceKey"), nullable=False, comment='서비스키 ')
    serviceTypeId = Column(Integer, nullable=False, comment='서비스타입 ID')
    serviceType = Column(VARCHAR(90), nullable=False, comment='서비스타입 / all / incheon / weather / airkorea ')
    endpoint = Column(VARCHAR(255), nullable=False, comment='url')
    request_count = Column(Integer, nullable=False, comment='요청 횟수')
    last_used_at = Column(DATETIME, nullable=False, comment='마지막 사용 날짜')
