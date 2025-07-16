from pydantic import BaseModel, Field, validator
from .base import allowed_levels

class SkillIn(BaseModel):
    name:str = Field(...,min_length=2,max_length=50)
    skill_level_id:int

    @validator('name','skill_level_id',pre=True)
    def trim_fields(cls,v):
        if not (isinstance(v,str)):
            return v
        return v.strip()
    
class SkillRead(SkillIn):
    id:int
    level:str