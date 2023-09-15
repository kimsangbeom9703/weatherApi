from fastapi import APIRouter

area_router = APIRouter(
    prefix="/api/test",  # url 앞에 고정적으로 붙는 경로추가
    tags=["test"], # docs tag name
)  # Route 분리
