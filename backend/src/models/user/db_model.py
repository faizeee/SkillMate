from models.user_role import UserRole
from sqlmodel import SQLModel, Relationship, Field
from typing import Optional


class User(SQLModel, table=True):
    """This class represents a user in the system."""

    id: int | None = Field(default=None, primary_key=True)
    user_role_id: int | None = Field(nullable=True, foreign_key="user_roles.id")
    username: str
    password_hash: str

    # Relationship to UserRole table (many-to-one)
    role: Optional[UserRole] = Relationship(back_populates="users")

    @property
    def role_name(self) -> str | None:
        """Get role name from role object."""
        return self.role.title if self.role else None
