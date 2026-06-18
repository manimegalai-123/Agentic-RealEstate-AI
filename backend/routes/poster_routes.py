from fastapi import APIRouter

router = APIRouter(
    prefix="/poster",
    tags=["Poster"]
)


@router.post("/accept/{property_id}")
def accept_poster(property_id: int):

    print(f"Poster accepted for property {property_id}")

    return {
        "message": "Poster accepted successfully"
    }


@router.post("/reject/{property_id}")
def reject_poster(property_id: int):

    print(f"Poster rejected for property {property_id}")

    return {
        "message": "Poster rejected successfully"
    }