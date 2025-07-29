import select
from typing import Optional
from fastapi.testclient import TestClient
from models.skill import Skill
from sqlmodel import Session


def register_and_login_test_user(client: TestClient) -> dict:
    """Register a new test user and returns a valid JWT access token."""
    # Register user data
    payload = {"username": "testuser", "password": "12345678"}
    # Register user
    client.post("/api/register/", json=payload)
    # Login user
    response = client.post("/api/login/", json=payload)
    # print(f"Login Helper response text -> {response.status_code} : {response.text} : {response.json()}")
    assert response.status_code == 200
    # token = response.json()["access_token"]
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
