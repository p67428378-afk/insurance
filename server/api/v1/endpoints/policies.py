
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid

from server import crud, models, schemas
from server.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Policy)
def create_policy(policy: schemas.PolicyCreate, db: Session = Depends(get_db)):
    """
    Creates a new policy record with the calculated premium.
    """
    return crud.create_policy(db=db, policy=policy)

@router.get("/{policy_id}", response_model=schemas.Policy)
def read_policy(policy_id: uuid.UUID, db: Session = Depends(get_db)):
    """
    Retrieves a policy by its ID.
    """
    db_policy = crud.get_policy(db, policy_id=policy_id)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy
