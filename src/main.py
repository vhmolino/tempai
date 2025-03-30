from fastapi import FastAPI

from api.router import api_router

app = FastAPI(title='TempAI')

app.include_router(api_router, prefix='/ai')
