from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/extract/invoice")
async def extract_invoice(file: UploadFile = File(...)):
    # TODO: Vision API 연결
    return {"message": "Invoice extraction endpoint ready"}
