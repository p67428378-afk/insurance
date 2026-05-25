
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.app.db.session import get_db # Updated import
from server.app.schemas.policy import PremiumCalculationRequest, PolicyResponse
from server.app.crud.policy import create_policy
from server.app.core.config import settings
from decimal import Decimal

router = APIRouter()

@router.post("/calculate", response_model=PolicyResponse)
def calculate_premium(request: PremiumCalculationRequest, db: Session = Depends(get_db)):
    base_rate = Decimal(str(settings.BASE_RATE))

    # Validate NCB and vehicle multiplier ranges
    ncb_percentage = Decimal(str(request.ncb_percentage))
    if not (Decimal('0.29') <= ncb_percentage <= Decimal('0.50')):
        raise HTTPException(status_code=422, detail="NCB percentage must be between 0.29 and 0.50.")

    vehicle_multiplier = Decimal(str(request.vehicle_multiplier))
    if not (Decimal('1.6') <= vehicle_multiplier <= Decimal('9.8')):
        raise HTTPException(status_code=422, detail="Vehicle multiplier must be between 1.6 and 9.8.")

    calculated_premium = base_rate * (Decimal('1') - ncb_percentage) * vehicle_multiplier
    calculated_premium = calculated_premium.quantize(Decimal('0.01'))

    try:
        policy = create_policy(db, request, calculated_premium, base_rate)
        # Manually construct the response to ensure correct types
        response = PolicyResponse(
            policy_id=policy.policy_id,
            customer_id=policy.customer_id,
            vehicle_details=policy.vehicle_details,
            base_rate=policy.base_rate,
            ncb_percentage=policy.ncb_percentage,
            vehicle_multiplier=policy.vehicle_multiplier,
            calculated_premium=policy.calculated_premium,
            created_at=policy.created_at,
            updated_at=policy.updated_at
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
