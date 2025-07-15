from pydantic import BaseModel, Field, validator

class UserBase(BaseModel):
    username:str = Field(...,min_length=6, max_length=12)
    @validator('username')
    def no_spaces (cls,v):
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v


class UserCreate(UserBase):
    password:str = Field (...,min_length=8)

    
class UserRead(UserBase):
    id:int

