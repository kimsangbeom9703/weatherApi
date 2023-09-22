from sqlalchemy.orm import Session
from typing import Type


def get_all_data(db: Session, model, skip: int = 0, limit: int = 10):
    _list = db.query(model).order_by(model.id.asc())

    total = _list.count()
    list = _list.offset(skip).limit(limit).all()
    return total, list  # (전체 건수, 페이징 적용된 질문 목록)
