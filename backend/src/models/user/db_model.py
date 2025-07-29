from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """This class represents a user in the system."""

    id: int | None = Field(default=None, primary_key=True)
    username: str
    password_hash: str
