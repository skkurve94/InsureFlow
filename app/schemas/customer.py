from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CustomerCreate(BaseModel):
    customer_id: str = Field(
        min_length=5,
        max_length=20
    )

    full_name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15
    )

    city: str = Field(
        min_length=2,
        max_length=100
    )


class CustomerResponse(BaseModel):
    id: int
    customer_id: str
    full_name: str
    email: str
    phone: str
    city: str
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )