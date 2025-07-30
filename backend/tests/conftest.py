import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from main import app
from data.db import get_session
from tests.utils.seed import seed_test_db
from sqlalchemy.pool import StaticPool
from tests.utils.helpers import register_and_login_test_user
from core.config import config

# In-memory SQLite for testing
test_db_engine = create_engine(
    config.test_database_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


# Dependency override for FastAPI
def override_get_session():
    with Session(test_db_engine) as session:
        yield session


# Apply the override globally
app.dependency_overrides[get_session] = override_get_session


# Create schema and seed DB before running tests
@pytest.fixture(scope="session", autouse=True)
def prepare_test_db():
    """Pytest fixture to create all database tables once for the entire test session."""
    SQLModel.metadata.create_all(test_db_engine)
    with Session(test_db_engine) as session:
        seed_test_db(session)  # ✅ Use real seeded skills with skill levels
    yield
    SQLModel.metadata.drop_all(test_db_engine)


@pytest.fixture(scope="function")  # Use 'function' scope for isolated tests
def drop_tables():
    """Pytest fixture to ensure a clean database state for each test.

    Drops all tables before a test, and creates them afterwards.
    """
    # Teardown (occurs before the test runs, effectively cleaning previous state)
    SQLModel.metadata.drop_all(test_db_engine)
    print("\n--- All tables dropped ---")  # Added for visibility during tests
    # Yield control to the test function
    yield
    SQLModel.metadata.create_all(test_db_engine)


# Provide test client to test_files
@pytest.fixture
def client():
    """Pytest fixture to provide a FastAPI TestClient instance."""
    return TestClient(app)


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
