from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from app.services.file_service import FileService
import io

router = APIRouter()

file_service = FileService()

@router.post("/upload/")
async def upload_files(files: list[UploadFile] = File(...)):
    return await file_service.upload_files(files)

@router.post("/merge/")
async def merge_files(selected_columns: dict):
    return file_service.merge_files(selected_columns)

@router.post("/filter/")
async def filter_data(filters: dict):
    return file_service.filter_data(filters)

@router.get("/download/")
async def download_filtered_file():
    file_stream = file_service.get_filtered_file()
    if not file_stream:
        raise HTTPException(status_code=404, detail="No filtered data to download.")
    return StreamingResponse(
        io.BytesIO(file_stream),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=filtered_data.xlsx"},
    )
