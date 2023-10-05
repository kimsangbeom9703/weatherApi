from fastapi import Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from db.connection import get_db
from typing import Optional, Union

from apis import authServiceKeyApi
from datetime import datetime

from pydantic import Field


def serviceKeyLogUpdate(db, serviceKeyData, path):
    authServiceManager = authServiceKeyApi.AuthServiceKeyManager(db=db)
    return authServiceManager.serviceKeyLogUpdate(serviceKeyData, path)


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


async def common_parameters(
        # q: Union[str, None] = None, skip: int = 0, limit: int = 10
        skip: int = 0, limit: int = 10
):
    return {"skip": skip, "limit": limit}


async def new_common_parameters(
        _end: int = None,
        _order: str = 'asc',
        _sort: str = None,
        _start: int = None,
):
    return {"_end": _end, "_order": _order, "_sort": _sort, "_start": _start }
