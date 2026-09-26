from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_number = Column(String(30), unique=True, nullable=False, index=True)
    policy_number = Column(String(30), nullable=False, index=True)
    claim_type = Column(String(50), nullable=False)
    claim_amount = Column(Float, nullable=False)
    claim_date = Column(String(20), nullable=False)
    status = Column(String(30), default="Pending")
    description = Column(String(500), nullable=True)