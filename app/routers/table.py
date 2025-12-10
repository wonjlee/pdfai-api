from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/extract/table")
async def extract_table(file: UploadFile = File(...)):
    # TODO: 표 추출 로직
    return {"message": "Table extraction endpoint ready"}
