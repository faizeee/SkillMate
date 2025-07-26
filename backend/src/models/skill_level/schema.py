from pydantic import BaseModel


class SkillLevelRead(BaseModel):
    """This class describes the structure of skill level."""

    id: int
    name: str
    description: str
