from pydantic import BaseModel


class ListingInput(BaseModel):
    id: int
    accommodates: int
    room_type: str  # TODO: to enum
    beds: int
    bedrooms: int
    bathrooms: int
    neighbourhood: str  # TODO: to enum
    tv: int
    elevator: int
    internet: int
    latitude: float
    longitude: float
