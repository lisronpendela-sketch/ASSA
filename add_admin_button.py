import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will add an Admin button into the header navigation menu next to 'Contact'
nav_item_regex = r'(<li><a href="#contact">Contact</a></li>)'
admin_button = r'\1\n        <li><a href="/admin/index.html" style="color: var(--gold); font-weight: bold; margin-left: 1rem; border: 2px solid var(--gold); border-radius: 20px; padding: 0.3rem 0.8rem;">Admin Login</a></li>'

html = re.sub(nav_item_regex, admin_button, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
