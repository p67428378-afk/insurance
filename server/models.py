
import uuid
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from server.database import Base

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    base_rate = Column(Numeric(10, 2), nullable=False)
    ncb_percentage = Column(Numeric(5, 4), nullable=False)
    vehicle_multiplier = Column(Numeric(5, 4), nullable=False)
    final_premium = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
