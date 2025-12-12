import secrets

# 임시 저장용 (나중에 PostgreSQL로 변경)
API_KEYS = set()

def generate_api_key():
    """고객에게 발급할 새로운 API 키 생성"""
    key = "pdfai_" + secrets.token_hex(16)
    API_KEYS.add(key)
    return key

def validate_api_key(key: str) -> bool:
    """API 키가 유효한지 확인"""
    return key in API_KEYS
