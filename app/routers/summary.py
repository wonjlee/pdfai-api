from fastapi import APIRouter, UploadFile, File
from app.services.summarize_service import summarize_pdf

router = APIRouter()

@router.post("/pdf/summary")
async def pdf_summary(file: UploadFile = File(...)):
    """
    PDF 업로드 → AI Vision 요약 결과 반환
    """
    file_bytes = await file.read()
    summary = summarize_pdf(file_bytes)

    return {
        "filename": file.filename,
        "summary": summary
    }
