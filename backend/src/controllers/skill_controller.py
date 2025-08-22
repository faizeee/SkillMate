"""Contains skills curd: create,update,delete and fetch handlers."""

from typing import Optional
from click import File
from fastapi import HTTPException, UploadFile, status
from models.base.response_schemas import ResponseMessage
from models.skill import Skill, SkillIn, SkillRead
from models.skill_level import SkillLevel
from utils.helpers import save_file
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from sqlalchemy import func


def get_skill_levels(db: Session) -> list[SkillLevel]:
    """Fetch All Skill Levels from db.

    Args:
        db (Session): Need a resolved Session object by route.
    Returns:
        list[SkillLevel]: List of skill levels.
    """
    try:
        levels = db.exec(select(SkillLevel)).all()
        return levels
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_skills(db: Session) -> list[SkillRead]:
    """Fetch All Skills from db.

    Args:
        db (Session): Need a resolved Session object by route.
    Returns:
        list[SkillRead]: List of skills.
    """
    try:
        # Use select to build your query
        query = select(Skill).options(selectinload(Skill.level))
        # execute the statement and fetch all results
        skills = db.exec(query).all()
        results = [
            {
                "id": skill.id,
                "name": skill.name,
                "skill_level_id": skill.skill_level_id,
                "level_name": skill.level.name if skill.level else "N/A",
            }
            for skill in skills
        ]
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# The -> symbol in a function definition is used for type hints,
# specifically to indicate the return type of the function.
async def add_skills(
    db: Session, skill: SkillIn, file: UploadFile | None = File(None)
) -> SkillRead:
    """Add new skill to Skill table.

    Args:
        db (Session): Need a resolved Session object by route.
        skill(SkillIn): submitted data
    Returns:
        SkillRead: New Created Skill.
    """
    check_skill_duplicate(db=db, skill_name=skill.name)
    file_path = await save_file(file, subdir="skills") if file else None
    # 1. Create and add the new skill
    skill_data = skill.model_dump()
    new_skill = Skill(
        **skill_data, icon_path=file_path
    )  # OR Skill(name=skill.name,skill_level_id=skill.skill_level_id)
    db.add(new_skill)
    # This assigns the 'id' to new_skill and saves it.
    db.commit()

    # This fetches the latest state from the database, including the related SkillLevel object.
    db.refresh(new_skill, attribute_names=["level"])
    # Now, new_skill.level will contain the fully loaded SkillLevel object
    result = new_skill.model_dump()
    result["level_name"] = new_skill.level.name if new_skill.level else "N/A"

    return result


def get_skill_by_id(id: int, db: Session) -> SkillRead:
    """Fetch a Skill from db based on id.

    Args:
        id(int): Skill id
        db (Session): Need a resolved Session object by route.
    Returns:
        SkillRead: single fetched skill with level details.
    """
    selected_skill = db.exec(
        select(Skill).filter(Skill.id == id).options(selectinload(Skill.level))
    ).first()
    if not selected_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )
    result = selected_skill.model_dump()
    result["level_name"] = selected_skill.level.name if selected_skill.level else "N/A"
    return result


def delete_skill_by_id(id: int, db: Session) -> ResponseMessage:
    """Delete a Skill from skills table based on id.

    Args:
        id(int): Skill id
        db (Session): Need a resolved Session object by route.
    Returns:
        ResponseMessage: status of requested operation.
    """
    selected_skill = db.exec(
        select(Skill).filter(Skill.id == id)
    ).first()  # Fetches the item

    if not selected_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Skill with id {id} not found",
        )

    db.delete(selected_skill)  # Deletes the in-memory object
    db.commit()
    # db.refresh(selected_skill) # Less critical for delete, but doesn't hurt

    return ResponseMessage(message=f"Skill with id {id} deleted successfully")


async def update_skill_by_id(
    db: Session, skill_id: int, inputs: SkillIn, file: UploadFile | None = None
) -> SkillRead:
    """Update a skill in skills table based on skill_id.

    Args:
        db (Session): Need a resolved Session object by route.
        skill_id(int): Skill id
        inputs: skill data
        file: UploadFile Or None
    Returns:
        SkillRead: New Created Skill.
    """
    skill = db.get(Skill, skill_id)
    if not skill:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Skill not found")

    check_skill_duplicate(db, inputs.name, skill_id)

    # NOTE: use inputs.model_dump(exclude_unset=True).items()  for partial
    # updates it ignores the unchanged
    for key, value in inputs.model_dump(exclude_unset=True).items():
        setattr(skill, key, value)

    if file:
        file_path = await save_file(file, subdir="skills")
        setattr(skill, "icon_path", file_path)

    db.commit()
    db.refresh(skill)
    skill_data = skill.model_dump()
    skill_data["level_name"] = skill.level.name if skill.level else "N/A"
    return skill_data


def check_skill_duplicate(
    db: Session, skill_name: str, skill_id: Optional[int | None] = None
):
    """Database Uniqueness Validation, ignoring the skill being updated."""
    filters = [func.lower(Skill.name) == skill_name.lower()]

    # Exclude the current skill from the uniqueness check if it has an ID
    if skill_id:
        filters.append(Skill.id != skill_id)

    statement = select(Skill).filter(*filters)
    if db.exec(statement).first():
        raise HTTPException(
            status_code=409, detail=f"Skill with name '{skill_name}' already exits"
        )


# Option 2: Direct Delete Query
# def delete_skill_by_id(id: int, db: Session) -> dict:
#     delete_statement = delete(Skill).where(Skill.id == id) # Constructs the delete statement
#     result = db.exec(delete_statement) # Executes the delete
#     db.commit()

#     if result.rowcount == 0: # Checks affected rows
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Skill with id {id} not found"
#         )

#     return {"message": f"Skill with id {id} deleted successfully","status":"ok"}
