from fastapi import APIRouter
from models.skill import Skill,SkillIn
from services.skill_service import check_duplicate_skill_name
from controllers.skill_controller import get_skills, add_skills

router = APIRouter() #The tags parameter is used for grouping related API endpoints in the automatically generated interactive API documentation (Swagger UI / OpenAPI UI).

@router.get("/",response_model=list[Skill])
def list_skills():
    return get_skills()

@router.post("/",response_model=Skill)
def create_skill(skill:SkillIn): #Request Body Validation: This is where FastAPI's magic for incoming data happens. When a POST request comes in
    return add_skills(skill)