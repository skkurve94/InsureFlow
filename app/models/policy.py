from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String(30), unique=True, nullable=False, index=True)
    customer_id = Column(String(20), nullable=False, index=True)
    policy_type = Column(String(50), nullable=False)
    premium_amount = Column(Float, nullable=False)
    coverage_amount = Column(Float, nullable=False)
    start_date = Column(String(20), nullable=False)
    end_date = Column(String(20), nullable=False)
    status = Column(String(20), default="Active")