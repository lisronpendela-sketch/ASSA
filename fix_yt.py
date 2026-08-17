import re

files = ['index.html', 'classes.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('href="https://youtube.com/@AkbarStudySmartAcademy"', 'href="https://youtube.com/@akbarstudysmartacademy?si=3gcJ0zBQJgjN6ZDf"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated footer contact YouTube link.")
