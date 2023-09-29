from sqlalchemy import Column, VARCHAR, DATETIME
from db.session import Base


class CollectionWeatherModel(Base):
    __tablename__ = "collection_weather_data"

    # id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    uniqueVal = Column(VARCHAR(45),primary_key=True, nullable=False, comment='유니크값')
    baseDate = Column(VARCHAR(45), nullable=False, comment='예보 생성일자')
    baseTime = Column(VARCHAR(45), nullable=False, comment='예보 생성시간')
    fcstRealDate = Column(VARCHAR(45), nullable=False, comment='예측일')
    fcstDate = Column(VARCHAR(45), nullable=False, comment='예측일자')
    fcstTime = Column(VARCHAR(45), nullable=False, comment='예측시간')
    callDate = Column(DATETIME, nullable=False, comment='호출시간')
    nx = Column(VARCHAR(45), nullable=False, comment='예보지점X좌표')
    ny = Column(VARCHAR(45), nullable=False, comment='예보지점Y좌표')
    icon = Column(VARCHAR(45), nullable=True, comment='아이콘')
    popVal = Column(VARCHAR(45), nullable=True, comment='강수확률')
    ptyVal = Column(VARCHAR(45), nullable=True, comment='강수형태')
    pcpVal = Column(VARCHAR(45), nullable=True, comment='강수량')
    skyVal = Column(VARCHAR(45), nullable=True, comment='하늘상태')
    rehVal = Column(VARCHAR(45), nullable=True, comment='습도')
    snoVal = Column(VARCHAR(45), nullable=True, comment='신적설')
    tmpVal = Column(VARCHAR(45), nullable=True, comment='기온')
    tmnVal = Column(VARCHAR(45), nullable=True, comment='최저기온')
    tmxVal = Column(VARCHAR(45), nullable=True, comment='최고기온')
    uuuVal = Column(VARCHAR(45), nullable=True, comment='풍속(동서)')
    vvvVal = Column(VARCHAR(45), nullable=True, comment='풍속(남북)')
    wavVal = Column(VARCHAR(45), nullable=True, comment='파고')
    vecVal = Column(VARCHAR(45), nullable=True, comment='풍향')
    wsdVal = Column(VARCHAR(45), nullable=True, comment='풍속')
    lgtVal = Column(VARCHAR(45), nullable=True, comment='낙뢰')
