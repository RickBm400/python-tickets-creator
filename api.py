from fastapi import APIRouter

from routers.items import router as items_router
from routers.metrics import router as metrics_router

api_router = APIRouter()
api_router.include_router(items_router)
api_router.include_router(metrics_router)