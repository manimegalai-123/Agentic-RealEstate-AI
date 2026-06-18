from pydantic import BaseModel


class PriceInput(BaseModel):
    bedroom: int
    bathroom: int
    kitchen: int
    gaming: int
    dining:int
    laundry: int
    living:int
    office:int
    terrace:int
    yard:int