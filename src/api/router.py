from fastapi import APIRouter

from api.routes import model

api_router = APIRouter()
api_router.include_router(model.router)