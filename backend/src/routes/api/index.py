from fastapi import APIRouter
from .skill_routes import router as skill_router
from .auth_routes import router as auth_router
# from .user import router as user_router  # For future

api_router = APIRouter()
# Grouped routers
api_router.include_router(skill_router, prefix="/skills", tags=["Skills"])
api_router.include_router(auth_router, tags=["Auth"])
# api_router.include_router(user_router, prefix="/users", tags=["Users"])