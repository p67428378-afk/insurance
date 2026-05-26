
from fastapi import APIRouter, HTTPException
from decimal import Decimal, getcontext
from server.schemas import PremiumCalculationRequest, PremiumCalculationResponse

# Set precision for Decimal calculations
getcontext().prec = 10

router = APIRouter()

BASE_RATE = Decimal("500.00")

@router.post("/calculate", response_model=PremiumCalculationResponse)
def calculate_premium(request: PremiumCalculationRequest):
    """
    Calculates the insurance premium based on base rate, NCB percentage, and vehicle multiplier.

    - **base_rate**: The base rate for the premium.
    - **ncb_percentage**: No Claims Bonus percentage (clamped between 0.29 and 0.50).
    - **vehicle_multiplier**: Vehicle risk multiplier (clamped between 1.6 and 9.8).
    """
    if request.base_rate != BASE_RATE:
        raise HTTPException(
            status_code=400,
            detail=f"Base rate must be ${BASE_RATE}."
        )

    # Clamp values to the specified business rule ranges
    ncb = max(Decimal("0.29"), min(request.ncb_percentage, Decimal("0.50")))
    multiplier = max(Decimal("1.6"), min(request.vehicle_multiplier, Decimal("9.8")))

    # Perform calculation
    # Premium after NCB = Base Rate * (1 - NCB)
    # Final Premium = (Premium after NCB) * Vehicle Multiplier
    premium_after_ncb = request.base_rate * (Decimal("1") - ncb)
    final_premium = premium_after_ncb * multiplier

    return {"final_premium": final_premium.quantize(Decimal('0.01'))}
