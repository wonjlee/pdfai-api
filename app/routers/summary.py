from fastapi import APIRouter, UploadFile, File, Depends, Header
from app.services.summarize_service import summarize_pdf
from app.auth.dependency import verify_api_key
from app.auth.api_key_manager import generate_api_key
from app.usage.usage_manager import increase_usage
from app.usage.usage_manager import get_usage


router = APIRouter()

@router.post("/pdf/summary")
async def pdf_summary(
    file: UploadFile = File(...),
    valid: bool = Depends(verify_api_key),
    x_api_key: str = Header(None)
):
    file_bytes = await file.read()
    summary = summarize_pdf(file_bytes)

    # 사용량 증가
    today_count = increase_usage(x_api_key)

    return {
        "summary": summary,
        "usage_today": today_count
    }


@router.get("/generate-key")
async def create_api_key():
    key = generate_api_key()
    return {"api_key": key}


@router.get("/usage")
async def usage(x_api_key: str = Header(None)):
    return get_usage(x_api_key)