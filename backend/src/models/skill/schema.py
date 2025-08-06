from typing import Optional
from pydantic import BaseModel, Field, field_validator

from models.skill_level import SkillLevel


class SkillIn(BaseModel):
    """This class describes the properties a skill needs to save in db."""

    name: str = Field(..., min_length=2, max_length=50)
    skill_level_id: int

    # @validator('name','skill_level_id',pre=True)
    # def trim_fields(cls,v):
    #     if not (isinstance(v,str)):
    #         return v
    #     return v.strip()

    # Validator to convert 'name' to lowercase
    @field_validator("name")  # Decorator specifies which field to validate/transform
    @classmethod  # Class method is required for field_validator
    def transform_input(cls, value: str):
        """Convert the skill name  strips leading/trailing whitespace."""
        return value.strip()


class SkillRead(SkillIn):
    """This class describes the properties a skill will contains when user asked for skill."""

    id: int
    level: Optional[SkillLevel] = None
    level_name: Optional[str] = None
