from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class UserRole(SQLModel, table=True):
    """This class represents a user role in the system."""

    __tablename__ = "user_roles"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None

    # Relationship to Skill table (one-to-many) :List [...] means to many
    users: List["User"] = Relationship(back_populates="role")
