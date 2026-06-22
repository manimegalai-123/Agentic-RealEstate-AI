from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form
import os
import shutil
from graph.realestate_graph import app_graph

router = APIRouter(
    prefix="/pipeline",
    tags=["Pipeline"]
)


@router.post("/")
async def run_pipeline(
    owner_name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    location: str = Form(...),
    area: int = Form(...),
    floor: int = Form(...),
    status: str = Form(...),
    files: list[UploadFile] = File(...)):

    image_paths = []

    os.makedirs("static/uploads", exist_ok=True)

    for file in files:
        path = f"static/uploads/{file.filename}"

        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        image_paths.append(path)
    print(owner_name)
    print(phone)
    print(email)
    print(location)
    print(area)
    print(floor)
    print(status)

    state = {
    "images": image_paths,
    "owner_name": owner_name,
    "phone": phone,
    "email": email,
    "location": location,
    "area": area,
    "floor": floor,
    "status": status
}

    print(state)

    result = app_graph.invoke(state)

    return result