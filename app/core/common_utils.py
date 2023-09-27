from fastapi import Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from db.connection import get_db

from apis import authServiceKeyApi
from datetime import datetime
from typing import Union


def serviceKeyLogUpdate(db, serviceKeyData, path):
    authServiceManager = authServiceKeyApi.AuthServiceKeyManager(db=db)
    return authServiceManager.serviceKeyLogUpdate(serviceKeyData, path)


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
async def common_parameters(
        # q: Union[str, None] = None, skip: int = 0, limit: int = 10
    skip: int = 0, limit: int = 10
):
    return { "skip": skip, "limit": limit}