from typing import Optional
from fastapi.testclient import TestClient
from models.skill import Skill
from sqlmodel import Session
from core.config import config as app_config
from alembic.config import Config
from alembic import command
from sqlmodel import SQLModel
from sqlalchemy import text
from tests.utils.seed import seed_test_db
from sqlmodel import select
import os


def run_alembic_upgrade():
    """Run migrations before running any test run."""
    alembic_config_file_path = os.path.join(
        os.path.dirname(__file__), "../../../alembic.ini"
    )
    alembic_config = Config(alembic_config_file_path)
    alembic_config.set_main_option("sqlalchemy.url", app_config.test_database_url)
    print("---------------- RUNNING MIGRATIONS  ------------------------")
    command.upgrade(alembic_config, "head")


def reset_test_db(engine):
    """Drop and recreate the test DB using SQLAlchemy Utils, then run Alembic."""
    SQLModel.metadata.drop_all(engine)
    drop_the_alembic_version(engine)


def drop_the_alembic_version(engine):
    """DROP TABLE IF EXISTS alembic_version cascade."""
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE;"))
        conn.commit()


def seed_db(engine):
    """Seed the database from seeder."""
    with Session(engine) as session:
        seed_test_db(session)
    print("✅ Test DB reseeded")


def run_migrations_and_seed_db(test_db_engine):
    """Run migrations and seed the database."""
    run_alembic_upgrade()
    seed_db(test_db_engine)


def register_and_login_test_user(client: TestClient) -> dict:
    """Register a new test user and returns a valid valid user data."""
    # Register user data
    payload = {"username": "testuser", "password": "12345678"}
    # Register user
    client.post("/api/register/", json=payload)
    return login_test_user(client, payload)


def login_test_user(client: TestClient, user_payload: dict) -> dict:
    """Login a test user and returns a valid user data."""
    response = client.post("/api/login/", json=user_payload)
    assert response.status_code == 200
    return response.json()


def create_test_skill(
    client: TestClient, auth_header: dict, skill_data: Optional[dict] = None
) -> dict:
    """Create a new skill using the API and return the response JSON."""
    if skill_data is None:
        # Create the Pydantic instance inside the function
        skill_data = {"name": "Test Skill", "skill_level_id": "1"}

    response = client.post("/api/skills/", json=skill_data, headers=auth_header)
    assert response.status_code == 200
    return response.json()


def count_skills_in_db(session: Session) -> int:
    """Return number of skills currently in the DB (for testing side effects)."""
    return session.exec(select(Skill)).count()


def get_all_skills(client: TestClient) -> list[dict]:
    """Hit the GET /api/skills endpoint and return the list."""
    response = client.get("/api/skills/")
    assert response.status_code == 200
    return response.json()
