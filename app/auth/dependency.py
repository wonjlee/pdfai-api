from fastapi import Header, HTTPException
from app.auth.api_key_manager import validate_api_key

async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="API Key is missing")

    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return True
