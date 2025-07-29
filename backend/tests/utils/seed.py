from sqlmodel import Session
from models.skill import Skill
from models.skill_level import SkillLevel


def seed_test_db(db_con: Session):
    beginner = SkillLevel(name="Beginner", description="Just Starting")
    intermediate = SkillLevel(name="Intermediate", description="Going Good")
    advance = SkillLevel(name="Advance", description="Master")

    db_con.add_all([beginner, intermediate, advance])
    db_con.flush()  # Get generated IDs

    skill_php = Skill(name="PHP", skill_level_id=advance.id)
    skill_py = Skill(name="Python", skill_level_id=beginner.id)
    skill_js = Skill(name="JavaScript", skill_level_id=intermediate.id)

    db_con.add_all([skill_php, skill_js, skill_py])
    db_con.commit()
