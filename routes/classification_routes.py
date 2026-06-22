from fastapi import APIRouter
from services.image_classifier import predict_room

router = APIRouter(
    prefix="/classify",
    tags=["Classification"]
)

import os

@router.get("/")
def classify(image_path: str):

    image_path = image_path.replace("\\", "/")

    if image_path.startswith("backend/"):
        image_path = image_path[len("backend/"):]

    room = predict_room(image_path)

    return {"room": room}