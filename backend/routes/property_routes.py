from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.models import Property
from database.dependencies import get_db
from schemas.property_schema import PropertyCreate

router = APIRouter(
    prefix="/property",
    tags=["Property"]
)


@router.post("/")
def create_property(
        property_data: PropertyCreate,
        db: Session = Depends(get_db)
):

    new_property = Property(
        owner_name=property_data.owner_name,
        phone=property_data.phone,
        location=property_data.location,
        area=property_data.area
    )

    db.add(new_property)
    db.commit()
    db.refresh(new_property)

    return {
        "message": "Property created successfully",
        "id": new_property.id
    }


@router.get("/")
def get_properties(db: Session = Depends(get_db)):

    properties = db.query(Property).all()

    return properties