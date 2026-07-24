from fastapi import APIRouter

from routers import metrics, items

api_router = APIRouter()
api_router.include_router(metrics.router)
api_router.include_router(items.router)