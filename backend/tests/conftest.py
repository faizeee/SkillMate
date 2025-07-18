import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from main import app
from data.db import get_session
from tests.utils.seed import seed_test_db
from sqlalchemy.pool import StaticPool

# In-memory SQLite for testing
DATABASE_URL = "sqlite:///:memory:"
test_db_engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread":False},    poolclass=StaticPool)

# Dependency override for FastAPI
def override_get_session():
    with Session(test_db_engine) as session:
        yield session
# Apply the override globally
app.dependency_overrides[get_session] = override_get_session

# Create schema and seed DB before running tests
@pytest.fixture(scope="session", autouse=True)
def prepare_test_db():
    SQLModel.metadata.create_all(test_db_engine)
    with Session(test_db_engine) as session:
        seed_test_db(session)  # ✅ Use real seeded skills with skill levels
    yield
    SQLModel.metadata.drop_all(test_db_engine)

# Provide test client

@pytest.fixture
def client():
    return TestClient(app)