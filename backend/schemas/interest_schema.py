from pydantic import BaseModel

class InterestRequest(BaseModel):
    property_id: int
    buyer_name: str
    phone: str
    purpose: str

