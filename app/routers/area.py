from fastapi import APIRouter

area_router = APIRouter(
    prefix="/area",  # url 앞에 고정적으로 붙는 경로추가
    tags=["area"], # docs tag name
)  # Route 분리


@area_router.get("/")  # Route Path
def index ():
    res = 'area'
    return {
        "res": res,
    }  # 결과