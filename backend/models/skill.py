from pydantic import BaseModel, Field, validator
class Skill(BaseModel):
    name:str = Field(...,min_length=2,max_length=50)
    level:str = Field(...,min_length=2)

    @validator('name','level',pre=True)
    def trim_inputs(cls,v):
        if(isinstance(v,str)):
          return v.strip()
        return v
    
    @validator('level')
    def validate_level(cls,v):
        valid_levels = ["Beginner", "Intermediate", "Advanced"]
        if v not in valid_levels:
            raise ValueError(f"Level must be one of: {', '.join(valid_levels)}")
        return v