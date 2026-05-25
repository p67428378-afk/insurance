
import uuid
from sqlalchemy import Column, DateTime, func, JSON, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    vehicle_details = Column(JSON, nullable=False)
    base_rate = Column(Numeric(10, 2), nullable=False)
    ncb_percentage = Column(Numeric(5, 4), nullable=False)
    vehicle_multiplier = Column(Numeric(5, 2), nullable=False)
    calculated_premium = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
