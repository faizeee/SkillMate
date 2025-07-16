import os
import sys
# Adjust path to include the 'backend' directory (your project root) in sys.path
# This allows importing from 'data.db' and 'data.models' correctly.
script_dir = os.path.dirname(os.path.abspath(__file__)) # This will be D:\ReactLearning\SkillMate\backend\seeders
project_root = os.path.dirname(script_dir) # This will correctly get D:\ReactLearning\SkillMate\backend
sys.path.insert(0, project_root)

from data.db import engine
from models.skill import Skill
from models.skill_level import SkillLevel
from sqlmodel import Session, select

def seed_initial_data():
    """
    Seeds initial SkillLevels and Skills data into the database.
    This function checks if data already exists to prevent re-seeding.
    """
    print("Attempting to seed initial data...")

    with Session(engine) as db_conn:
        existing_levels = db_conn.exec(select(SkillLevel)).first()
        if existing_levels :
            print("SkillLevels already exist. Skipping seeding.")
            return
        print("No SkillLevels found. Seeding initial data...")

        beginner = SkillLevel(name="Beginner", description="Just starting")
        intermediate = SkillLevel(name="Intermediate")
        advanced = SkillLevel(name="Advanced",description="Master of None")

        db_conn.add(beginner)
        db_conn.add(intermediate)
        db_conn.add(advanced)
        db_conn.commit()

        db_conn.refresh(beginner)
        db_conn.refresh(intermediate)
        db_conn.refresh(advanced)
        # Now, intermediate.id (and beginner.id, expert.id) will have the actual database IDs.
        print(f"Seeded SkillLevel IDs: Beginner={beginner.id}, Intermediate={intermediate.id}, Expert={advanced.id}")
        
        javaScript = Skill(name="JavaScript",skill_level_id=advanced.id)
        python = Skill(name="Python",skill_level_id=beginner.id)
        fastApi = Skill(name="FastAPI",skill_level_id=beginner.id)
        php_lang = Skill(name="PHP",skill_level_id=advanced.id)
        laravel = Skill(name="Laravel",skill_level_id=intermediate.id)
        aws = Skill(name="AWS",skill_level_id=intermediate.id)

        db_conn.add(javaScript)
        db_conn.add(python)
        db_conn.add(fastApi)
        db_conn.add(php_lang)
        db_conn.add(laravel)
        db_conn.add(aws)
        db_conn.commit()
        print("Initial data seeded successfully!")

if __name__ == "__main__":
    from data.db import init_db
    init_db() # Ensure tables exist
    seed_initial_data()