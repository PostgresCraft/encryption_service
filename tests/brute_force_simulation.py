from cryptography.fernet import Fernet, InvalidToken

# Encrypted message
ciphertext = (
    "gAAAAABoUTdrrPiIrIKJ_uryYmTR2_B2ZZgmQc8xAyTHf3y7trBxXsmjpxgLYkmpoh1EUxRs4lvyPjuUHZp2VtyYUkiugHhWXVlXozx_EGy5thKE6ZatmF4="
)

# Number of brute-force attempts
attempts = 100_000000  # 100,000 attempts, negligible compared to 2^256

print(f"🚀 Starting brute-force decryption attempt... (Attempts: {attempts})")

for i in range(attempts):
    fake_key = Fernet.generate_key()
    fernet = Fernet(fake_key)
    try:
        decrypted = fernet.decrypt(ciphertext.encode())
        print("🎉 Unexpected success! Key:", fake_key.decode())
        print("Decrypted text:", decrypted.decode())
        break
    except InvalidToken:
        if i % 10000 == 0:
            print(f"⏳ Attempt #{i}... Failed.")
else:
    print("❌ All attempts exhausted... Decryption unsuccessful.")
