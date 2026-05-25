
from sqlalchemy.orm import Session
import uuid
from . import models, schemas

def get_policy(db: Session, policy_id: uuid.UUID):
    return db.query(models.Policy).filter(models.Policy.policy_id == policy_id).first()

def create_policy(db: Session, policy: schemas.PolicyCreate):
    db_policy = models.Policy(
        base_rate=policy.base_rate,
        ncb_percentage=policy.ncb_percentage,
        vehicle_multiplier=policy.vehicle_multiplier,
        final_premium=policy.final_premium
    )
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy
