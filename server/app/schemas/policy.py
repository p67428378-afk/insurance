
from pydantic import BaseModel, UUID4
from datetime import datetime
from decimal import Decimal

class VehicleDetails(BaseModel):
    make: str
    model: str
    year: int

class PremiumCalculationRequest(BaseModel):
    customer_id: UUID4
    vehicle_details: VehicleDetails
    ncb_percentage: float
    vehicle_multiplier: float

class PolicyResponse(BaseModel):
    policy_id: UUID4
    customer_id: UUID4
    vehicle_details: VehicleDetails
    base_rate: Decimal
    ncb_percentage: Decimal
    vehicle_multiplier: Decimal
    calculated_premium: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
