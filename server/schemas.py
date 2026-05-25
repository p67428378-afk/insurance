
from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
import uuid
from datetime import datetime

# --- Premium Schemas ---

class PremiumCalculationRequest(BaseModel):
    base_rate: Decimal = Field(..., gt=0, description="The base rate for the premium.")
    ncb_percentage: Decimal = Field(..., description="No Claims Bonus percentage.")
    vehicle_multiplier: Decimal = Field(..., description="Vehicle risk multiplier.")

class PremiumCalculationResponse(BaseModel):
    final_premium: Decimal

# --- Policy Schemas ---

class PolicyBase(BaseModel):
    base_rate: Decimal
    ncb_percentage: Decimal
    vehicle_multiplier: Decimal
    final_premium: Decimal

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    policy_id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
