
from fastapi.testclient import TestClient
from server.main import app
from decimal import Decimal

client = TestClient(app)

def test_calculate_premium_success():
    """Test successful premium calculation with valid inputs."""
    response = client.post(
        "/api/v1/premium/calculate",
        json={
            "base_rate": 500,
            "ncb_percentage": 0.30,
            "vehicle_multiplier": 2.0
        }
    )
    assert response.status_code == 200
    # Calculation: 500 * (1 - 0.30) = 350; 350 * 2.0 = 700
    assert response.json() == {"final_premium": "700.00"}

def test_calculate_premium_clamping_ncb_low():
    """Test premium calculation clamping a low NCB value."""
    response = client.post(
        "/api/v1/premium/calculate",
        json={
            "base_rate": 500,
            "ncb_percentage": 0.10, # Below min
            "vehicle_multiplier": 2.0
        }
    )
    assert response.status_code == 200
    # Calculation uses clamped NCB of 0.29: 500 * (1 - 0.29) = 355; 355 * 2.0 = 710
    assert response.json() == {"final_premium": "710.00"}

def test_calculate_premium_clamping_ncb_high():
    """Test premium calculation clamping a high NCB value."""
    response = client.post(
        "/api/v1/premium/calculate",
        json={
            "base_rate": 500,
            "ncb_percentage": 0.60, # Above max
            "vehicle_multiplier": 2.0
        }
    )
    assert response.status_code == 200
    # Calculation uses clamped NCB of 0.50: 500 * (1 - 0.50) = 250; 250 * 2.0 = 500
    assert response.json() == {"final_premium": "500.00"}

def test_calculate_premium_clamping_multiplier_low():
    """Test premium calculation clamping a low multiplier value."""
    response = client.post(
        "/api/v1/premium/calculate",
        json={
            "base_rate": 500,
            "ncb_percentage": 0.30,
            "vehicle_multiplier": 1.0 # Below min
        }
    )
    assert response.status_code == 200
    # Calculation uses clamped multiplier of 1.6: 500 * (1 - 0.30) = 350; 350 * 1.6 = 560
    assert response.json() == {"final_premium": "560.00"}

def test_calculate_premium_clamping_multiplier_high():
    """Test premium calculation clamping a high multiplier value."""
    response = client.post(
        "/api/v1/premium/calculate",
        json={
            "base_rate": 500,
            "ncb_percentage": 0.30,
            "vehicle_multiplier": 10.0 # Above max
        }
    )
    assert response.status_code == 200
    # Calculation uses clamped multiplier of 9.8: 500 * (1 - 0.30) = 350; 350 * 9.8 = 3430
    assert response.json() == {"final_premium": "3430.00"}

def test_calculate_premium_invalid_base_rate():
    """Test that an incorrect base rate is rejected."""
    response = client.post(
        "/api/v1/premium/calculate",
        json={
            "base_rate": 499,
            "ncb_percentage": 0.30,
            "vehicle_multiplier": 2.0
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Base rate must be $500.00."}
