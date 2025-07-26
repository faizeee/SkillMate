from fastapi import APIRouter, Depends
from sqlmodel import Session
from data.db import get_session
from models.skill import SkillRead, SkillIn
from models.skill_level import SkillLevel
from services.auth_service import get_current_user
from controllers.skill_controller import (
    get_skills,
    add_skills,
    get_skill_levels,
    get_skill_by_id,
    delete_skill_by_id,
)
from models.user import User
from models.base.response_schemas import ResponseMessage
from fastapi_cache.decorator import cache


router = (
    APIRouter()
)  # The tags parameter is used for grouping related API endpoints in the automatically generated interactive API documentation (Swagger UI / OpenAPI UI).


@router.get("/", response_model=list[SkillRead])
def list_skills(db: Session = Depends(get_session)):
    """Fetch all skills."""
    return get_skills(db)


@router.post("/", response_model=SkillRead)
def create_skill(
    skill: SkillIn,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):  # Request Body Validation: This is where FastAPI's magic for incoming data happens. When a POST request comes in
    """Create a new skill."""
    return add_skills(skill, db)


@router.get("/levels", response_model=list[SkillLevel])
@cache(
    expire=60 * 60 * 24,
    key_builder=lambda f, *args, **kwargs: "skillmate-cache:skill-levels",
)
def get_levels(db: Session = Depends(get_session)):
    """Get all skill levels.

    We have implemented the redis cache for this root so when data will be
    fetched from db or from cache.
    """
    return get_skill_levels(db)


@router.get("/{skill_id}", response_model=SkillRead)
def get_a_skill(
    skill_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):
    """Fetch a skill using id."""
    return get_skill_by_id(skill_id, db)


@router.delete("/{skill_id}", response_model=ResponseMessage)
def delete_a_skill(
    skill_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):
    """Delete a skill using id."""
    return delete_skill_by_id(skill_id, db)
