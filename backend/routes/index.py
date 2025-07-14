from fastapi import APIRouter
from routes.api.index import api_router

router = APIRouter()
router.include_router(api_router, prefix="/api")