import pprint

from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from crud import crud_get ,crud_create , crud_update


from db.models.authApiServiceKeyModel import AuthApiServiceKeyModel
from db.models.authApiServiceLogModel import AuthApiServiceLogModel
from db.models.authApiServiceTypeModel import AuthApiServiceTypeModel

from datetime import datetime, timedelta

import uuid
import json


class AuthServiceKeyManager:
    def __init__(self, db):
        self.db = db

    def nowDate(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def expiresDate(self):
        now = datetime.now() + timedelta(weeks=12)
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def checkServiceKey(self, api_key_header, key_type):
        if api_key_header is None:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="API Key header is missing"
            )

        # 데이터베이스에서 서비스 키를 조회합니다.
        api_key = crud_get.check_service_api_key(self.db, AuthApiServiceKeyModel, api_key_header, key_type)

        if api_key is None:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )

        return api_key

    def serviceKeyLogUpdate(self, apiKeyData, endpoint):
        if apiKeyData is None:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="API Key Data is missing"
            )
        updateServiceKeyLog = crud_update.update_service_key_endpoint_log(self.db,AuthApiServiceLogModel,apiKeyData,endpoint)
        if updateServiceKeyLog is None:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="Api Log Not Save.",
            )

        return updateServiceKeyLog

    def createAuthServiceKey(self, req):
        req_dict = req.dict()
        # 새로운 값을 추가
        req_dict['is_active'] = 0
        req_dict['serviceKey'] = uuid.uuid4()
        req_dict['expires_at'] = req_dict['expires_at'] if req_dict['expires_at'] else self.expiresDate()
        req_dict['created_at'] = self.nowDate()
        try:
            created_data = crud_create.createData(self.db, AuthApiServiceKeyModel, req_dict)
            statusCode = 200
            status = 'success'
            auth_service_key_dict = {
                "serviceTypeId": created_data.serviceTypeId,
                "serviceType": created_data.serviceType,
                "description": created_data.description,
                "expires_at": created_data.expires_at,
                "id": created_data.id,
                "serviceKey": created_data.serviceKey,
                "created_at": created_data.created_at,
            }
        except Exception as e:
            errorMsg = str(e)
            statusCode = 400
            status = 'fail'
            auth_service_key_dict = {}
        else:
            errorMsg = None  # 오류가 발생하지 않을 때는 errorMsg를 None으로 설정

        # auth_service_key_dict = json.dumps(auth_service_key_dict, default=str, indent=2)
        response_dict = {
            "statusCode": statusCode,
            "status": status,
            "data": auth_service_key_dict,
            "errorMsg": errorMsg if errorMsg else None
        }
        return response_dict
        # return crud_create.createData(db,AuthApiServiceKeyModel,req)
