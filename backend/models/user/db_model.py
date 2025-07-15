from sqlmodel import SQLModel, Field

class User(SQLModel,table=True):
    id:int | None = Field(default=None,primary_key=True)
    user: str
    password_hash:str

