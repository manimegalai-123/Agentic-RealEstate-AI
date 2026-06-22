from pydantic import BaseModel


class PropertyCreate(BaseModel):
    owner_name: str
    phone: str
    email: str
    location: str
    area: int
    status: str
    floor: str