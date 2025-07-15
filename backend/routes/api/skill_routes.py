from fastapi import APIRouter, Depends
from models.skill import Skill,SkillIn
from services.auth_service import get_current_user
from controllers.skill_controller import get_skills, add_skills
from models.user import User

router = APIRouter() #The tags parameter is used for grouping related API endpoints in the automatically generated interactive API documentation (Swagger UI / OpenAPI UI).

@router.get("/",response_model=list[Skill])
def list_skills():
    return get_skills()

@router.post("/",response_model=Skill)
def create_skill(skill:SkillIn , user:User = Depends(get_current_user) ): #Request Body Validation: This is where FastAPI's magic for incoming data happens. When a POST request comes in
    return add_skills(skill)