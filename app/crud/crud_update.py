from sqlalchemy import update
from sqlalchemy.orm import Session

from datetime import datetime, timedelta


def update_service_key_endpoint_log(db: Session, model, apiKeyData, endPoint):
    try:
        now = datetime.now()
        callDate = now.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = db.query(model).filter(
            model.serviceKey == apiKeyData.serviceKey,
            model.serviceTypeId == apiKeyData.serviceTypeId,
            model.serviceType == apiKeyData.serviceType,
            model.endpoint == endPoint
        ).first()
        if log_entry is None:
            # 로그 엔트리가 없으면 새로 생성합니다.
            log_entry = model(
                serviceKey=apiKeyData.serviceKey,
                serviceTypeId=apiKeyData.serviceTypeId,
                serviceType=apiKeyData.serviceType,
                endpoint=endPoint,
                request_count=1,
            )
            db.add(log_entry)
        else:
            # 로그 엔트리가 이미 존재하면 request_count를 증가시킵니다.
            log_entry.request_count += 1
        log_entry.last_used_at = callDate
        db.commit()
        db.close()
        return log_entry
    except Exception as e:
        db.rollback()  # 롤백

def update_service_key_data(db: Session, model, oldData, updateData):
    try:
        now = datetime.now()
        callDate = now.strftime('%Y-%m-%d %H:%M:%S')
        # 업데이트할 열 및 조건을 정의
        update_condition = model.id == oldData.id  # 업데이트 조건을 정의
        update_values = {
            'expires_at': updateData.expires_at,
            'updated_at': callDate,
            'description': updateData.description,
            'referer': updateData.referer,
            'is_active': updateData.status
        }
        db.execute(update(model).values(update_values).where(update_condition))
        db.commit()
        updated_record = db.query(model).filter(model.id == oldData.id).first()
        db.close()
        return updated_record
    except Exception as e:
        db.rollback()  # 롤백
