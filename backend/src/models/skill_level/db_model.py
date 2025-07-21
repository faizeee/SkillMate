from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List

class SkillLevel(SQLModel,table=True):
    __tablename__="skill_levels"
    id:Optional[int] = Field(default=None, primary_key=True)
    name:str
    description: Optional[str] = None

    # Relationship to Skill table (one-to-many)
    skills : List["Skill"] = Relationship(back_populates='level')
