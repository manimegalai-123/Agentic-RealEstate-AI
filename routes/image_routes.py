from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter(
    prefix="/image",
    tags=["Image"]
)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    path = f"static/uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Uploaded successfully",
        "filename": file.filename
    }