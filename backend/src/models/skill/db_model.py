from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from models.skill_level import SkillLevel


class Skill(SQLModel, table=True):
    """This class represents a skill in the system."""

    __tablename__ = "skills"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    icon_path: Optional[str] = None
    skill_level_id: int = Field(foreign_key="skill_levels.id")

    # Relationship to SkillLevel table (many-to-one)
    level: Optional[SkillLevel] = Relationship(back_populates="skills")
