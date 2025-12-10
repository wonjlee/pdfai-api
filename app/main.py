from fastapi import FastAPI

app = FastAPI(
    title="PDF AI API",
    description="AI 기반 PDF → JSON 자동화 API SaaS",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "PDF AI API server is running"}
