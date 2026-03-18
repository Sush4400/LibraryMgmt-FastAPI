from fastapi import FastAPI
from app.routes.api import api_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(api_router)


@app.get("/")
def home():
    return {
        "status": True,
        "message": "Libary Management Backend is Running..."
    }