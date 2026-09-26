from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.policy import Policy
from app.models.customer import Customer
from app.schemas.policy import PolicyCreate, PolicyResponse


router = APIRouter(
    prefix="/api/policies",
    tags=["Policies"]
)


@router.get("/", response_model=list[PolicyResponse])
def get_policies(db: Session = Depends(get_db)):
    return db.query(Policy).all()


@router.get("/{policy_number}", response_model=PolicyResponse)
def get_policy(
    policy_number: str,
    db: Session = Depends(get_db)
):
    policy = (
        db.query(Policy)
        .filter(Policy.policy_number == policy_number)
        .first()
    )

    if not policy:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return policy


@router.post(
    "/",
    response_model=PolicyResponse,
    status_code=201
)
def create_policy(
    policy_data: PolicyCreate,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.customer_id == policy_data.customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer does not exist"
        )

    existing_policy = (
        db.query(Policy)
        .filter(
            Policy.policy_number == policy_data.policy_number
        )
        .first()
    )

    if existing_policy:
        raise HTTPException(
            status_code=400,
            detail="Policy number already exists"
        )

    policy = Policy(
        policy_number=policy_data.policy_number,
        customer_id=policy_data.customer_id,
        policy_type=policy_data.policy_type,
        premium_amount=policy_data.premium_amount,
        coverage_amount=policy_data.coverage_amount,
        start_date=policy_data.start_date,
        end_date=policy_data.end_date
    )

    db.add(policy)
    db.commit()
    db.refresh(policy)

    return policy


@router.delete("/{policy_number}")
def delete_policy(
    policy_number: str,
    db: Session = Depends(get_db)
):
    policy = (
        db.query(Policy)
        .filter(Policy.policy_number == policy_number)
        .first()
    )

    if not policy:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    db.delete(policy)
    db.commit()

    return {
        "message": "Policy deleted successfully",
        "policy_number": policy_number
    }