from pydantic import BaseModel


class HealthcheckOutput(BaseModel):
    status: str
    timestamp: str


class ListingOutput(BaseModel):
    id: int
    price_category: str  # TODO: to enum
