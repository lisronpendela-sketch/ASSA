import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix justify-content on .nav
css = css.replace('justify-content:center;', 'justify-content:space-between;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed navbar layout in style.css")
