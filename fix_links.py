files = ['index.html', 'classes.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('href="#classes"', 'href="classes.html"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print("Links updated")
