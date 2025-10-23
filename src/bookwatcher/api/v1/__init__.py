from fastapi import APIRouter

from .endpoints import author_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(author_router)