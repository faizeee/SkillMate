import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine,text
from main import app
from data.db import get_session
from tests.utils.seed import seed_test_db
from sqlalchemy.pool import StaticPool
from tests.utils.helpers import register_and_login_test_user

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
    """
    Pytest fixture to create all database tables once for the entire test session.
    """
    SQLModel.metadata.create_all(test_db_engine)
    with Session(test_db_engine) as session:
        seed_test_db(session)  # ✅ Use real seeded skills with skill levels
    yield
    SQLModel.metadata.drop_all(test_db_engine)

# Provide test client to test_files
@pytest.fixture
def client():
    """
    Pytest fixture to provide a FastAPI TestClient instance.
    """
    return TestClient(app)

# Provide test client to test_files
# @pytest.fixture(autouse=True)
# def truncate_and_seed_db():
#     """
#     Pytest fixture to truncate (clear) all tables in the in-memory SQLite database
#     and then re-seed it with test data before each individual test.
#     """
#     with Session(test_db_engine) as session:
#         with session.begin():
#             table_names = [table.name for table in SQLModel.metadata.sorted_tables]
#             for table_name in table_names:
#                 session.exec(text(f"DELETE FROM {table_name};"))
#                 session.exec(text(f"DELETE FROM sqlite_sequence WHERE name='{table_name}';"))
#             seed_test_db(session)
#     yield


# Provide auth_header to test_files
@pytest.fixture
def auth_header(client):
    token = register_and_login_test_user(client)
    return {"Authorization":f"Bearer {token}"}