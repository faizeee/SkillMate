from pydantic import BaseModel, Field ,field_validator
class SkillIn(BaseModel):
    name:str = Field(...,min_length=2,max_length=50)
    skill_level_id:int

    # @validator('name','skill_level_id',pre=True)
    # def trim_fields(cls,v):
    #     if not (isinstance(v,str)):
    #         return v
    #     return v.strip()

    # Validator to convert 'name' to lowercase
    @field_validator('name') # Decorator specifies which field to validate/transform
    @classmethod # Class method is required for field_validator
    def transform_input(cls,value:str) :
        """Converts the skill name  strips leading/trailing whitespace."""
        return value.strip()
    
class SkillRead(SkillIn):
    id:int
    level:str