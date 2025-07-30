from .schema import UserRoleRead
from .db_model import UserRole

UserRole.model_rebuild()

__all__ = ["UserRoleRead", "UserRole"]
