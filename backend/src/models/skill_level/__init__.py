from .schema import SkillLevelRead
from .db_model import SkillLevel

SkillLevel.update_forward_refs()

__all__ = ["SkillLevelRead", "SkillLevel"]
