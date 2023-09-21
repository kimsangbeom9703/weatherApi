from fastapi import FastAPI
import routers as rt
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
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
