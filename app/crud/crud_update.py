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
        return log_entry
    except Exception as e:
        db.rollback()  # 롤백
