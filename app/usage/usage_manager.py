import json
import os
from datetime import datetime

USAGE_FILE = "usage.json"

def _load_usage():
    if not os.path.exists(USAGE_FILE):
        return {}
    with open(USAGE_FILE, "r") as f:
        return json.load(f)

def _save_usage(data):
    with open(USAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def increase_usage(api_key: str):
    data = _load_usage()
    today = datetime.utcnow().strftime("%Y-%m-%d")

    if api_key not in data:
        data[api_key] = {}

    if today not in data[api_key]:
        data[api_key][today] = 0

    data[api_key][today] += 1
    _save_usage(data)

    return data[api_key][today]

def get_usage(api_key: str):
    data = _load_usage()
    return data.get(api_key, {})
