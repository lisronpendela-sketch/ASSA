import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<style>([\s\S]*?)</style>', html)
if match:
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
    
    new_html = html.replace(match.group(0), '<link rel="stylesheet" href="style.css">')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Done")
else:
    print("No style block found")
