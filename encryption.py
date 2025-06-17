from cryptography.fernet import Fernet
from keys_manager import get_user_key

def encrypt(plaintext: str, user_id: str) -> str:
    key = get_user_key(user_id)
    f = Fernet(key)
    return f.encrypt(plaintext.encode()).decode()

def decrypt(ciphertext: str, user_id: str) -> str:
    key = get_user_key(user_id)
    f = Fernet(key)
    return f.decrypt(ciphertext.encode()).decode()
