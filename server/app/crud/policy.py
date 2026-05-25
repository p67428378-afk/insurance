
from sqlalchemy.orm import Session
from server.app.models.policy import Policy
from server.app.schemas.policy import PremiumCalculationRequest
from decimal import Decimal

def create_policy(db: Session, request: PremiumCalculationRequest, calculated_premium: Decimal, base_rate: Decimal) -> Policy:
    db_policy = Policy(
        customer_id=request.customer_id,
        vehicle_details=request.vehicle_details.model_dump(),
        base_rate=base_rate,
        ncb_percentage=Decimal(str(request.ncb_percentage)),
        vehicle_multiplier=Decimal(str(request.vehicle_multiplier)),
        calculated_premium=calculated_premium
    )
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy
