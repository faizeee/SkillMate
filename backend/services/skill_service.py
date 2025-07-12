from fastapi import HTTPException
from data.fake_skills import fake_skills

def check_duplicate_skill_name(name: str):
    if any(s["name"].lower() == name.lower() for s in fake_skills):
        raise HTTPException(status_code=400, detail="Skill already exists.")