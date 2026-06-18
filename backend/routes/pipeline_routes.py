from typing import Annotated
from fastapi import APIRouter, UploadFile, File
import os
import shutil
from graph.realestate_graph import app_graph
from services.property_pipeline import process_property

router = APIRouter(
    prefix="/pipeline",
    tags=["Pipeline"]
)


@router.post("/")
async def run_pipeline(
    files: Annotated[list[UploadFile], File()]
):

    image_paths = []

    os.makedirs("static/uploads", exist_ok=True)

    for file in files:

        path = f"static/uploads/{file.filename}"

        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        image_paths.append(path)

    result = app_graph.invoke(
        {
            "images": image_paths
        }
    )

    print(result)

    return result

