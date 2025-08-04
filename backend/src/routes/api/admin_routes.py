from fastapi import APIRouter, Depends
from services.permissions import admin_only

router = APIRouter()


@router.get("/dashboard", dependencies=[Depends(admin_only)])
def get_admin_dashboard():
    """Get dashboard data for admin."""
    return {"message": "Welcome, admin!"}
