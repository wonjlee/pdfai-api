from fastapi import FastAPI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

from app.routers.summary import router as summary_router

app = FastAPI(
    title="PDF Summary API",
    description="PDF를 자동으로 요약하는 API 서비스",
    version="1.0.0"
)

app.include_router(summary_router, prefix="/v1")
