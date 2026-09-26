from pydantic import BaseModel, ConfigDict, Field


class PolicyCreate(BaseModel):
    policy_number: str = Field(
        min_length=5,
        max_length=30
    )

    customer_id: str = Field(
        min_length=5,
        max_length=20
    )

    policy_type: str = Field(
        min_length=2,
        max_length=50
    )

    premium_amount: float = Field(
        gt=0
    )

    coverage_amount: float = Field(
        gt=0
    )

    start_date: str

    end_date: str


class PolicyResponse(BaseModel):
    id: int
    policy_number: str
    customer_id: str
    policy_type: str
    premium_amount: float
    coverage_amount: float
    start_date: str
    end_date: str
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )