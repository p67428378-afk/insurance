
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.main import app
from server.app.db.session import get_db
from server.app.models.policy import Base
import uuid

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_calculate_premium_success(db_session):
    customer_id = str(uuid.uuid4())
    response = client.post(
        "/api/v1/premiums/calculate",
        json={
            "customer_id": customer_id,
            "vehicle_details": {"make": "Toyota", "model": "Camry", "year": 2021},
            "ncb_percentage": 0.30,
            "vehicle_multiplier": 2.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == customer_id
    assert data["calculated_premium"] == "700.00" # 500 * (1 - 0.30) * 2.0 = 700
    assert "policy_id" in data

def test_calculate_premium_invalid_ncb():
    response = client.post(
        "/api/v1/premiums/calculate",
        json={
            "customer_id": str(uuid.uuid4()),
            "vehicle_details": {"make": "Toyota", "model": "Camry", "year": 2021},
            "ncb_percentage": 0.10, # Below minimum
            "vehicle_multiplier": 2.0
        }
    )
    assert response.status_code == 422
    assert "NCB percentage must be between 0.29 and 0.50" in response.json()["detail"]

def test_calculate_premium_invalid_multiplier():
    response = client.post(
        "/api/v1/premiums/calculate",
        json={
            "customer_id": str(uuid.uuid4()),
            "vehicle_details": {"make": "Toyota", "model": "Camry", "year": 2021},
            "ncb_percentage": 0.40,
            "vehicle_multiplier": 10.0 # Above maximum
        }
    )
    assert response.status_code == 422
    assert "Vehicle multiplier must be between 1.6 and 9.8" in response.json()["detail"]
