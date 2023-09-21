from sqlalchemy import Column, VARCHAR, Integer
from db.session import Base


class CollectionWeatherModel(Base):
    __tablename__ = "auth_api_service_type"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    serviceType = Column(VARCHAR(45), nullable=False, comment='서비스타입 / all / incheon / weather / airkorea ')

