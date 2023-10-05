from sqlalchemy import or_, func
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
    api_key_data = db.query(model).filter(
        model.serviceKey == service_key,
        model.expires_at >= current_date,
        model.is_active == '0',
        or_(model.serviceType == "ALL", model.serviceType == key_type)
    ).first()
    return api_key_data


def get_all_station_data_by_time(db: Session, model, current_tiem):
    subquery = db.query(
        func.max(model.fcstRealDate).label('max_fcstRealDate'),
        model.dustStationIdx
    ).filter(
        model.fcstRealDate <= current_tiem
    ).group_by(
        model.dustStationIdx
    ).subquery()
    # 메인 쿼리 생성
    main_query = db.query(model).join(
        subquery,
        (model.dustStationIdx == subquery.c.dustStationIdx) &
        (model.fcstRealDate == subquery.c.max_fcstRealDate)
    )
    # 결과 가져오기
    results = main_query.all()

    return results


def get_station_dust_all_data(station_name, orderby, db: Session, model, skip: int = 0, limit: int = 10):
    if orderby == 'asc':
        _list = db.query(model).filter(model.dustStationName == station_name).order_by(model.fcstRealDate.asc())
    else:
        _list = db.query(model).filter(model.dustStationName == station_name).order_by(model.fcstRealDate.desc())
    total = _list.count()
    list = _list.offset(skip).limit(limit).all()
    return total, list


def get_all_station_data_first(db: Session, model, station_name):
    results = db.query(model).where(model.dustStationName == station_name).order_by(model.fcstRealDate.desc()).first()
    return results


##2023-10-05==================================================================================================


##
# # 조회할 레코드 범위 설정
# skip = 25  # 건너뛸 레코드 수
# limit = 50  # 최대로 가져올 레코드 수
#
# # ORM을 사용하여 데이터 조회
# query = session.query(YourModel)  # YourModel은 실제로 사용하려는 SQLAlchemy 모델입니다.
# query = query.order_by(YourModel.id.desc())  # id 역순으로 정렬
# query = query.offset(skip).limit(limit)  # 건너뛰기와 제한 설정##
def list(db: Session, model, common):
    _order = common['_order']
    _sort = common['_sort']
    _start = common['_start']
    _end = common['_end']
    query = db.query(model)
    if _sort:
        if _order == 'asc':
            query = query.order_by(getattr(model, _sort))
        elif _order == 'desc':
            query = query.order_by(getattr(model, _sort).desc())
    # ORM을 사용하여 데이터 조회
    result = query.offset(_start).limit(_end)
    return result
