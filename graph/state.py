from typing import TypedDict

class PropertyState(TypedDict):

    owner_name: str
    phone: str
    email: str
    location: str
    area: int
    floor: int
    status: str

    images: list

    labels: list
    features: dict
    price: float
    description: str
    poster: str

    owner_verified: bool
    listing: dict

    buyer_name: str
    purpose: str

    notification: str

    # NEW
    recommended_buyers: list