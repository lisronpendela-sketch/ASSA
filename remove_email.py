import re

for filename in ['index.html', 'classes.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the info@akbaracademy.pk line
    html = re.sub(r'<span class="topbar-item tb-hide"><span class="ic">✉️</span> info@akbaracademy.pk</span>\s*', '', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Removed email from topbar in both HTML files")
