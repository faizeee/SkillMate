from fastapi import HTTPException
from data.db import fake_skills


def check_duplicate_skill_name(name: str) -> None:
    """
    Checks if the provided skill name already exists in the skill list.

    Args:
        name (str): The name of the skill to check.

    Raises:
        HTTPException: If a skill with the same name already exists (case-insensitive).
    
    Returns:
        None
    """

    if any(s["name"].lower() == name.lower() for s in fake_skills):
        raise HTTPException(status_code=400, detail="Skill already exists.")