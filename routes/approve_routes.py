from fastapi import APIRouter
import shutil
import os

router = APIRouter(
    prefix="/approve",
    tags=["Approve"]
)

@router.post("/{id}")
def approve_poster(id: int):

    source = f"posters/poster_{id}.png"
    destination = f"approved_posters/poster_{id}.png"

    os.makedirs("approved_posters", exist_ok=True)

    shutil.copy(source, destination)

    return {
        "message": "Poster approved successfully"
    }