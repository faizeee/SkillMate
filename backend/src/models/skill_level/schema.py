from pydantic import BaseModel
class SkillLevelRead(BaseModel):
    id:int
    name:str
    description:str