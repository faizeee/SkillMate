from sqlmodel import Session
from models import Skill, SkillLevel, User, UserRole
from core.auth import get_password_hash


def seed_test_db(db_con: Session):
    print("🚨 Seeder bound to:", db_con.bind.url)
    beginner = SkillLevel(name="Beginner", description="Just Starting")
    intermediate = SkillLevel(name="Intermediate", description="Going Good")
    advance = SkillLevel(name="Advance", description="Master")

    db_con.add_all([beginner, intermediate, advance])
    db_con.flush()  # Get generated IDs

    skill_php = Skill(name="PHP", skill_level_id=advance.id)
    skill_py = Skill(name="Python", skill_level_id=beginner.id)
    skill_js = Skill(name="JavaScript", skill_level_id=intermediate.id)

    db_con.add_all([skill_php, skill_js, skill_py])

    super_admin = UserRole(title="Super Admin", description="System Admin")
    admin = UserRole(title="Admin", description="User Admin")
    user = UserRole(title="User", description="User")

    db_con.add_all([super_admin, admin, user])
    db_con.flush()

    print("User Roles Seeded!")

    hash_pswd = get_password_hash("12345678")
    superadmin = User(
        username="superadmin",
        password_hash=hash_pswd,
        user_role_id=super_admin.id,
    )
    adminuser = User(
        username="adminuser",
        password_hash=get_password_hash("12345678"),
        user_role_id=admin.id,
    )
    useracc = User(
        username="faizeee",
        password_hash=hash_pswd,
        user_role_id=user.id,
    )

    db_con.add_all([superadmin, adminuser, useracc])
    db_con.commit()
