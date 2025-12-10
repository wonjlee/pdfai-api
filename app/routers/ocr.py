from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/extract/ocr")
async def extract_ocr(file: UploadFile = File(...)):
    # TODO: OCR 로직
    return {"message": "OCR endpoint ready"}
