from typing import TypedDict


class PropertyState(TypedDict):

    images: list[str]

    labels: list[str]

    features: dict

    price: float

    description: str

    poster: str

    owner_verified: bool

    listing: dict

    notification: str