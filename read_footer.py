import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract footer
footer = re.search(r'<footer.*?</footer>', html, re.DOTALL)
if footer:
    print(footer.group(0))
