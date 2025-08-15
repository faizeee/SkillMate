from fastapi import APIRouter
from .skill_routes import router as skill_router
from .auth_routes import router as auth_router
from .admin_routes import router as admin_router

# from .user_routes import  user_router  # For future

api_router = APIRouter()
# Grouped routers
api_router.include_router(skill_router, prefix="/skills", tags=["Skills"])
api_router.include_router(auth_router, tags=["Auth"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])


# api_router.include_router(user_router,prefix="/user",tags=["User"])
# api_router.include_router(user_router, prefix="/users", tags=["Users"])
@api_router.options("/{rest_of_path:path}")
async def preflight_handler():
    """Handel OPTIONS request."""
    return {}
