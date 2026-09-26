from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.claim import Claim
from app.models.policy import Policy


router = APIRouter(
    prefix="/api/claims",
    tags=["Claims"]
)


@router.get("/")
def get_claims(
    db: Session = Depends(get_db)
):
    return db.query(Claim).all()


@router.get("/{claim_number}")
def get_claim(
    claim_number: str,
    db: Session = Depends(get_db)
):
    claim = (
        db.query(Claim)
        .filter(
            Claim.claim_number == claim_number
        )
        .first()
    )

    if not claim:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return claim


@router.post("/")
def create_claim(
    claim_number: str = Form(...),
    policy_number: str = Form(...),
    claim_type: str = Form(...),
    claim_amount: float = Form(...),
    claim_date: str = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db)
):
    # Check whether the policy exists
    policy = (
        db.query(Policy)
        .filter(
            Policy.policy_number == policy_number
        )
        .first()
    )

    if not policy:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Policy '{policy_number}' does not exist."
            )
        )

    # Check whether the claim number already exists
    existing_claim = (
        db.query(Claim)
        .filter(
            Claim.claim_number == claim_number
        )
        .first()
    )

    if existing_claim:
        raise HTTPException(
            status_code=400,
            detail="Claim number already exists."
        )

    # Validate claim amount
    if claim_amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Claim amount must be greater than zero."
        )

    # Create claim
    claim = Claim(
        claim_number=claim_number,
        policy_number=policy_number,
        claim_type=claim_type,
        claim_amount=claim_amount,
        claim_date=claim_date,
        description=description
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return {
        "message": "Claim created successfully.",
        "claim": {
            "id": claim.id,
            "claim_number": claim.claim_number,
            "policy_number": claim.policy_number,
            "claim_type": claim.claim_type,
            "claim_amount": claim.claim_amount,
            "claim_date": claim.claim_date,
            "status": claim.status,
            "description": claim.description
        }
    }


@router.delete("/{claim_number}")
def delete_claim(
    claim_number: str,
    db: Session = Depends(get_db)
):
    claim = (
        db.query(Claim)
        .filter(
            Claim.claim_number == claim_number
        )
        .first()
    )

    if not claim:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    db.delete(claim)
    db.commit()

    return {
        "message": "Claim deleted successfully.",
        "claim_number": claim_number
    }