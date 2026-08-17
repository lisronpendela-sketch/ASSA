import re

def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix class-card onclicks
    # <div class="class-card cc-11 reveal d2" onclick="window.open(\'https://wa.me/923235792758\', \'_blank\')">
    html = html.replace("onclick=\"window.open(\\'https://wa.me/923235792758\\', \\'_blank\\')\"", "onclick=\"openEnroll(this.querySelector('.class-label') ? this.querySelector('.class-label').innerText : (this.closest('.course-card') ? this.closest('.course-card').querySelector('h3').innerText : 'Selected Course'))\"")

    # Fix button onclicks inside course cards where it was replaced
    # <button class="btn-course" onclick="window.open(\'https://wa.me/923235792758\', \'_blank\')">
    # Wait, the previous replace actually covers all exact string matches of the onclick attribute value!
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html('index.html')
fix_html('classes.html')
print("Fixed onclick attributes")
