from pydantic import BaseModel


class UserRoleRead(BaseModel):
    """This class describes the structure of skill level."""

    id: int
    name: str
    description: str
