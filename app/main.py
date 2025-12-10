from fastapi import FastAPI
from app.routers import health, invoice, table, ocr

app = FastAPI(
    title="PDF AI API",
    description="AI 기반 PDF → JSON 자동화 API SaaS",
    version="0.1.0"
)

app.include_router(health.router)
app.include_router(invoice.router)
app.include_router(table.router)
app.include_router(ocr.router)
