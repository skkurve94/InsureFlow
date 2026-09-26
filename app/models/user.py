from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=True
    )

    role = Column(
        String(30),
        default="customer",
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )