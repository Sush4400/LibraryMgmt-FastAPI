from app.routes.endpoints import user, book, category, author, publisher
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(user.router)