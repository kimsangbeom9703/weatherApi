from sqlalchemy import or_
from sqlalchemy.orm import Session

from typing import Type
from datetime import date


def get_all_data(db: Session, model, skip: int = 0, limit: int = 10):
    _list = db.query(model).order_by(model.id.asc())

    total = _list.count()
    list = _list.offset(skip).limit(limit).all()
    return total, list  # (전체 건수, 페이징 적용된 질문 목록)


def check_service_api_key(db: Session, model, service_key, key_type):
    current_date = date.today()
    print(service_key)
    api_key_data = db.query(model).filter(
        model.serviceKey == service_key,
        model.expires_at >= current_date,
        model.is_active == '0',
        or_(model.serviceType == "ALL", model.serviceType == key_type)
    ).first()
    return api_key_data

