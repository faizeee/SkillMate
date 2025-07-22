from fastapi import HTTPException, status
from httpx import delete
from models.base.response_schemas import ResponseMessage
from models.skill import Skill, SkillIn,SkillRead
from models.skill_level import SkillLevel
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from sqlalchemy import func

def get_skill_levels(db:Session) ->list[SkillLevel] :
    try:
        levels = db.exec(select(SkillLevel)).all()
        return levels
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


def get_skills(db:Session) -> list[SkillRead] :
    try:
        # Use select to build your query
        query = select(Skill).options(selectinload(Skill.level))
        # execute the statement and fetch all results    
        skills = db.exec(query).all()
        results = [
            {
                "id" : skill.id,
                "name": skill.name,
                "skill_level_id":skill.skill_level_id,
                "level":skill.level.name if skill.level else "N/A"
            } 
            for skill in skills
            ]
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))     

def add_skills(skill:SkillIn, db:Session) -> SkillRead : #the -> symbol in a function definition is used for type hints, specifically to indicate the return type of the function

    # Database Uniqueness Validation
    # Build a statement to check for an existing skill with the same name (case-insensitive if desired)
    # For case-insensitive, you might convert both to lower() if your DB supports it or use specific functions
    # For SQLite, it's typically case-insensitive for ASCII by default, but explicit is better.
    
    if db.exec(select(Skill).filter(func.lower(Skill.name) == skill.name.lower())).first():
        raise HTTPException(status_code=409, detail=f"Skill with name '{skill.name}' already exits")
    # 1. Create and add the new skill
    new_skill = Skill(**skill.model_dump()) # OR Skill(name=skill.name,skill_level_id=skill.skill_level_id)
    db.add(new_skill)
    # This assigns the 'id' to new_skill and saves it.
    db.commit()
    
    # This fetches the latest state from the database, including the related SkillLevel object.
    db.refresh(new_skill, attribute_names=["level"])
    # Now, new_skill.level will contain the fully loaded SkillLevel object
    result = new_skill.model_dump()
    result['level'] = new_skill.level.name if new_skill.level else "N/A"

    return result

def get_skill_by_id(id:int,db:Session) -> SkillRead :
    selected_skill = db.exec(select(Skill).filter(Skill.id == id).options(selectinload(Skill.level))).first()
    if not selected_skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Skill not found")
    result = selected_skill.model_dump()
    result['level'] = selected_skill.level.name if selected_skill.level else "N/A"
    return result

def delete_skill_by_id(id: int, db: Session) -> ResponseMessage:
    selected_skill = db.exec(select(Skill).filter(Skill.id == id)).first() # Fetches the item

    if not selected_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Skill with id {id} not found"
        )

    db.delete(selected_skill) # Deletes the in-memory object
    db.commit()
    # db.refresh(selected_skill) # Less critical for delete, but doesn't hurt

    return ResponseMessage(message=f"Skill with id {id} deleted successfully")

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