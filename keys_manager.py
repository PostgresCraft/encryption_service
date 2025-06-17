
import os
from pathlib import Path
from cryptography.fernet import Fernet

KEYS_DIR = Path("user_keys")
KEYS_DIR.mkdir(exist_ok=True)

def get_user_key(user_id: str) -> bytes:
    key_path = KEYS_DIR / f"{user_id}.key"
    if not key_path.exists():
        key = Fernet.generate_key()
        with open(key_path, "wb") as f:
            f.write(key)
        return key
    else:
        return key_path.read_bytes()
