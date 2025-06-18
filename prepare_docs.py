import os

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# استبدال روابط الصور
content = content.replace("screenshots/", "screenshots/")

# استبدال رابط LICENSE
content = content.replace(
    "(../LICENSE)", 
    "(https://github.com/PostgresCraft/encryption_service/blob/main/LICENSE)"
).replace(
    "(LICENSE)", 
    "(https://github.com/PostgresCraft/encryption_service/blob/main/LICENSE)"
)

# حفظ الملف الجديد في docs/index.md
os.makedirs("docs", exist_ok=True)
with open("docs/index.md", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted README.md to docs/index.md successfully.")
