from fastapi import APIRouter
from models.skill import Skill
from services.skill_service import check_duplicate_skill_name
from data.fake_skills import fake_skills

router = APIRouter()

@router.get("/skills")
def get_skills():
    return fake_skills

@router.post("/skills")
def add_skills(skill:Skill):
    check_duplicate_skill_name(skill.name)
    new_skill = {
        "id":(len(fake_skills)+1),
        "name":skill.name,
        "level":skill.level   
    }
    fake_skills.append(new_skill)
    return new_skill