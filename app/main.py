from fastapi import FastAPI ,HTTPException, Request, status

import routers as rt
from fastapi.openapi.utils import get_openapi

app = FastAPI()
app.include_router(rt.area_router)
app.include_router(rt.incheon_airport_router)
app.include_router(rt.auth_service_key_router)


#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="환경정보 데이터 제공",
        version="0.0.1",
        # summary="This is a very custom OpenAPI schema",
        description="기상청 ( 예보버전 , 단기예보 , 초단기예보 ) / 에어코리아 대기질 ( 전국 대기질 정보) / 인천국제공항공사 (실내,실외) 미세먼지 데이터 ",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
