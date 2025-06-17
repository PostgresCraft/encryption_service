# generate_index.py

import markdown
from jinja2 import Template

# تحميل محتوى README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme_text = f.read()

# تحويل Markdown إلى HTML
html_body = markdown.markdown(readme_text)

# قالب HTML أساسي باستخدام Jinja2
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; max-width: 800px; }
        pre { background: #f4f4f4; padding: 10px; overflow-x: auto; }
        code { background: #f0f0f0; padding: 2px 4px; border-radius: 4px; }
        h1, h2, h3 { color: #333; }
        a { color: #0366d6; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    {{ content | safe }}
</body>
</html>
"""

# ربط القالب بالمحتوى
template = Template(html_template)
rendered_html = template.render(content=html_body)

# حفظ كـ index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("✅ تم توليد index.html بنجاح من README.md")
