from datetime import datetime, timedelta, timezone

import jwt

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from pwdlib import PasswordHash

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


password_hash = PasswordHash.recommended()


SECRET_KEY = (
    "insureflow-development-secret-change-before-aws"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

security = HTTPBearer()


def hash_password(password: str) -> str:

    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return password_hash.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
    user_id: int,
    email: str
) -> str:

    expiration = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": str(user_id),
        "email": email,
        "exp": expiration
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def get_authenticated_user(
    credentials: HTTPAuthorizationCredentials,
    db: Session
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid authentication token."
            )

    except jwt.ExpiredSignatureError:

        raise HTTPException(
            status_code=401,
            detail="Authentication token has expired."
        )

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token."
        )

    user = (
        db.query(User)
        .filter(
            User.id == int(user_id)
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return user


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(
            User.email == user_data.email
        )
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail=(
                "An account with this email "
                "already exists."
            )
        )

    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=hashed_password,
        phone=user_data.phone,
        role="customer",
        is_active=True
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "Account created successfully.",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        }
    }


@router.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.email == login_data.email
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not user.is_active:

        raise HTTPException(
            status_code=403,
            detail="This account has been disabled."
        )

    if not verify_password(
        login_data.password,
        user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    access_token = create_access_token(
        user_id=user.id,
        email=user.email
    )

    return {
        "message": "Login successful.",
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        }
    }


@router.get("/me")
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    user = get_authenticated_user(
        credentials,
        db
    )

    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "role": user.role,
        "is_active": user.is_active
    }


@router.put("/profile")
def update_profile(
    full_name: str,
    phone: str | None = None,
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    user = get_authenticated_user(
        credentials,
        db
    )

    full_name = full_name.strip()

    if len(full_name) < 2:

        raise HTTPException(
            status_code=400,
            detail="Full name must contain at least 2 characters."
        )

    user.full_name = full_name

    if phone is not None:

        user.phone = phone.strip() or None

    db.commit()

    db.refresh(user)

    return {
        "message": "Profile updated successfully.",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        }
    }


@router.put("/password")
def change_password(
    current_password: str,
    new_password: str,
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    user = get_authenticated_user(
        credentials,
        db
    )

    if not verify_password(
        current_password,
        user.password_hash
    ):

        raise HTTPException(
            status_code=400,
            detail="Current password is incorrect."
        )

    if len(new_password) < 8:

        raise HTTPException(
            status_code=400,
            detail=(
                "New password must contain "
                "at least 8 characters."
            )
        )

    if verify_password(
        new_password,
        user.password_hash
    ):

        raise HTTPException(
            status_code=400,
            detail=(
                "New password must be different "
                "from your current password."
            )
        )

    user.password_hash = hash_password(
        new_password
    )

    db.commit()

    return {
        "message": "Password changed successfully."
    }


@router.delete("/account")
def delete_account(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    user = get_authenticated_user(
        credentials,
        db
    )

    db.delete(user)

    db.commit()

    return {
        "message": "Account deleted successfully."
    }