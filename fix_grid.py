import re

filename = 'index.html'
with open(filename, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific grid container for news
target = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">'
replacement = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; align-items: start;">'

html = html.replace(target, replacement)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added align-items: start to News grid")
