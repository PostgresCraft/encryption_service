import os
import re

# قراءة محتوى README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# حذف رابط Live Documentation
content = re.sub(r"🔷 \[Live Documentation\]\([^)]+\)\n?", "", content)

# حذف جدول المحتويات بالكامل (من ## Table of Contents إلى أول ## بعده)
content = re.sub(r"## Table of Contents[\s\S]+?(?=\n## )", "", content)

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

# إنشاء مجلد docs إن لم يكن موجودًا
os.makedirs("docs", exist_ok=True)

# حفظ الملف الجديد
with open("docs/index.md", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted README.md to docs/index.md successfully.")