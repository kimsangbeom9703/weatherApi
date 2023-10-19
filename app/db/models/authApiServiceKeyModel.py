from sqlalchemy import Column, VARCHAR, Integer, DATETIME, TEXT, ForeignKey
from db.session import Base


class AuthApiServiceKeyModel(Base):
    __tablename__ = "auth_api_service_key"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='')
    serviceKey = Column(VARCHAR(90), nullable=False, comment='서비스키 ')
    serviceTypeId = Column(Integer, ForeignKey("auth_api_service_type.id"), nullable=False, comment='서비스타입 ID')
    serviceType = Column(VARCHAR(90), nullable=False, comment='서비스타입 / all / incheon / weather / airkorea ')
    deviceId = Column(VARCHAR(45), nullable=False, comment='디바이스id')
    referer = Column(VARCHAR(45), nullable=False, comment='요청 referer')
    description = Column(TEXT, nullable=True, comment='설명 ')
    created_at = Column(DATETIME, nullable=True, comment='생성 시간')
    updated_at = Column(DATETIME, nullable=True, comment='업데이트 시간')
    expires_at = Column(DATETIME, nullable=True, comment='만료 시간')
    is_active = Column(Integer, nullable=True, comment='활성화 여부 / 활성화 0 / 비활성화 1')
