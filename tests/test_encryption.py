import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from keys_manager import get_user_key
from encryption import encrypt, decrypt

# 1. Define the user ID
user_id = "tamer"

# 2. Retrieve or generate the user's encryption key
key = get_user_key(user_id)
print(f"[🔑] Loaded user-specific key for user_id: {user_id}")

# 3. Test encryption
plaintext = "Highly confidential, Tamer!"
encrypted_data = encrypt(plaintext, user_id)
print(f"[🔒] Encrypted: {encrypted_data}")

# 4. Test decryption
decrypted_data = decrypt(encrypted_data, user_id)
print(f"[🔓] Decrypted: {decrypted_data}")

# 5. Final verification
assert decrypted_data == plaintext, "❌ Error: Decrypted data does not match the original."
print("[✅] Test passed. User-specific encryption works correctly.")
