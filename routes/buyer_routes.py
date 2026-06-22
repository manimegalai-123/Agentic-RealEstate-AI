from fastapi import APIRouter

router = APIRouter(
    prefix="/buyer",
    tags=["Buyer"]
)


@router.get("/")
def buyers():

    return {
        "buyers": []
    }