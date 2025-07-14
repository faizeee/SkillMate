from pydantic import BaseModel, Field, validator
from .base import allowed_levels

class SkillIn(BaseModel):
    name:str = Field(...,min_length=2,max_length=50)
    level:str = Field(...,min_length=2)

    @validator('name','level',pre=True)
    def trim_fields(cls,v):
        if not (isinstance(v,str)):
            return v
        return v.strip()

    @validator('level')
    def validate_level(cls,v):
         valid_levels = allowed_levels()
         if(v not in valid_levels):
             raise ValueError(f"Level must be one of {', '.join(valid_levels)}")
         return v
    
class Skill(SkillIn):
    id:int