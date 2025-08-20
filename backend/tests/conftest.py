from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine
from main import app
from data.db import get_session
from tests.utils.helpers import (
    register_and_login_test_user,
    login_test_user,
    run_migrations_and_seed_db,
    reset_test_db,
)
from core.config import config as app_config

test_db_engine = create_engine(app_config.test_database_url)


# Dependency override for FastAPI
def override_get_session():
    with Session(test_db_engine) as session:
        yield session


# Apply the override globally
app.dependency_overrides[get_session] = override_get_session


# Create schema and seed DB before running tests
@pytest.fixture(scope="session", autouse=True)
def setup_test_db_at_start():
    """Pytest fixture to create all database tables once for the entire test session."""
    run_migrations_and_seed_db(test_db_engine)
    yield
    reset_test_db(test_db_engine)


@pytest.fixture(scope="function")
def reset_db_state():
    """Reset the db state before the test."""
    reset_test_db(test_db_engine)  # Drop and recreate
    run_migrations_and_seed_db(test_db_engine)  # Run migrations + seed
    yield


@pytest.fixture(scope="function")  # Use 'function' scope for isolated tests
def drop_all_tables_for_error_test():
    """Pytest fixture to ensure a clean database state for each test."""
    reset_test_db(test_db_engine)
    yield
    run_migrations_and_seed_db(test_db_engine)


# Provide test client to test_files
@pytest.fixture
def client():
    """Pytest fixture to provide a FastAPI TestClient instance."""
    return TestClient(app)


@pytest.fixture
async def async_client():
    """Create async client."""
    async with AsyncClient(app, base_url="http://test") as client:
        yield client


@pytest.fixture
def test_engine():
    return test_db_engine


# Provide logged in user to test_files
@pytest.fixture
def current_user(client):
    return register_and_login_test_user(client)


# Provide auth_header to test_files
@pytest.fixture
def auth_header(current_user):
    token = current_user["access_token"]
    return {"Authorization": f"Bearer {token}"}


# Provide logged in user to test_files
@pytest.fixture
def admin_user(client):
    payload = {"username": "adminuser", "password": "12345678"}
    return login_test_user(client, payload)


# Provide auth_header to test_files
@pytest.fixture
def auth_header_for_admin(admin_user):
    token = admin_user["access_token"]
    return {"Authorization": f"Bearer {token}"}
