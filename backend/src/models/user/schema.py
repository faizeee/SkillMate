from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict
from models.user_role import UserRole


class UserBase(BaseModel):
    """This class describes the common structure of user."""

    username: str = Field(..., min_length=6, max_length=12)

    @field_validator("username")
    @classmethod
    def no_spaces(cls, value: str):
        """Check and if user has spaces between username and lower the string."""
        if " " in value:
            raise ValueError("Username must not contain spaces")
        return value.lower().strip()


class UserCreate(UserBase):
    """This class describes the structure of user when creating."""

    password: str = Field(..., min_length=8)


class UserRead(UserBase):
    """This class describes the structure of user when fetching."""

    id: int
    role: Optional[UserRole] = None
    role_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
