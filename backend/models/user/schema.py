from pydantic import BaseModel, Field, field_validator

class UserBase(BaseModel):
    username:str = Field(...,min_length=6, max_length=12)
    @field_validator('username')
    @classmethod
    def no_spaces (cls,value:str):
        if " " in value:
            raise ValueError("Username must not contain spaces")
        return value.lower()


class UserCreate(UserBase):
    password:str = Field (...,min_length=8)

    
class UserRead(UserBase):
    id:int

