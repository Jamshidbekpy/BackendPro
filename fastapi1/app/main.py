from fastapi import FastAPI
from .routers.auth import router as auth_router

app = FastAPI()

app.include_router(router=auth_router)
