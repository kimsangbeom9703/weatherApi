from sqlalchemy.orm import Session


# from db.models.authApiServiceKeyModel import AuthApiServiceKeyModel
# from db.models.authApiServiceLogModel import AuthApiServiceLogModel
# from db.models.authApiServiceTypeModel import AuthApiServiceTypeModel
#
#
# def createAuthApiServiceKey(db: Session, req):
#     insertData = AuthApiServiceKeyModel(**req.dict())
#     db.add(insertData)
#     db.commit()
#     return insertData

def createData(db: Session, model, req):
    try:
        insertData = model(**req)
        db.add(insertData)
        db.commit()
        return insertData  # 값을 반환
    except Exception as e:
        db.rollback()  # 롤백
