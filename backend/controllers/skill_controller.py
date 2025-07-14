from fastapi import HTTPException
from models.skill import Skill, SkillIn
from data.db import fake_skills
from services.skill_service import check_duplicate_skill_name
def get_skills() -> list[Skill] :
    return fake_skills

def add_skills(skill:SkillIn) -> Skill : #the -> symbol in a function definition is used for type hints, specifically to indicate the return type of the function
    check_duplicate_skill_name(skill.name)

    new_skill = {
        "id" : (len(fake_skills)+1),
        "name": skill.name, 
        "level": skill.level
    }
    fake_skills.append(new_skill)
    return new_skill



