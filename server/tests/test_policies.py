
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.main import app
from server.database import Base, get_db
import uuid

# --- Test Database Setup ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables before tests
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Apply the override to the app
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# --- Fixture to clean up database after tests ---
@pytest.fixture(scope="function")
def db_session():
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables
    Base.metadata.drop_all(bind=engine)

# --- Tests ---

def test_create_and_read_policy(db_session):
    """Test creating a policy and then reading it back."""
    # 1. Create a policy
    policy_data = {
        "base_rate": 500.00,
        "ncb_percentage": 0.45,
        "vehicle_multiplier": 3.5,
        "final_premium": 962.50
    }
    response = client.post("/api/v1/policies/", json=policy_data)

    assert response.status_code == 200
    created_policy = response.json()
    assert "policy_id" in created_policy
    assert created_policy["base_rate"] == "500.00"
    assert created_policy["final_premium"] == "962.50"

    policy_id = created_policy["policy_id"]

    # 2. Read the policy back
    response = client.get(f"/api/v1/policies/{policy_id}")
    assert response.status_code == 200
    read_policy = response.json()
    assert read_policy["policy_id"] == policy_id
    assert read_policy["base_rate"] == "500.00"

def test_read_nonexistent_policy(db_session):
    """Test that reading a non-existent policy returns a 404 error."""
    non_existent_uuid = uuid.uuid4()
    response = client.get(f"/api/v1/policies/{non_existent_uuid}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Policy not found"}
