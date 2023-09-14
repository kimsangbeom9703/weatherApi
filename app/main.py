from fastapi import FastAPI
from app.routers.area import area_router
app = FastAPI()
app.include_router(area_router) # 다른 route파일들을 불러와 포함시킴
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
