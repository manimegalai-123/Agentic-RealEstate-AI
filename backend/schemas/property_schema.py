from pydantic import BaseModel


class PropertyCreate(BaseModel):
    owner_name: str
    phone: str
    location: str
    area: int