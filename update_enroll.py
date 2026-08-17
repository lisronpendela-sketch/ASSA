import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove <div class="class-price">...</div>
    html = re.sub(r'<div class="class-price">.*?</div>', '', html)
    
    # 2. Remove <div class="course-price">...</div>
    html = re.sub(r'<div class="course-price">.*?</div>', '', html)

    # 3. Replace onclick on class cards and course cards
    # E.g. onclick="openEnroll('Class 9 — Foundation Package','Rs. 2,500 / month')"
    html = re.sub(r'onclick="openEnroll\([^)]*\)"', r'onclick="window.open(\'https://wa.me/923235792758\', \'_blank\')"', html)
    
    # 4. Replace href="#" onclick="openEnroll(...);return false;" for links like nav
    # First, handle href="#" followed by onclick
    html = re.sub(r'href="#"([^>]*)onclick="openEnroll\([^)]*\);?return false;"', r'href="https://wa.me/923235792758" target="_blank"\1', html)
    
    # Also handle if onclick is present on something that isn't href="#"
    html = re.sub(r'onclick="openEnroll\([^)]*\);?return false;"', r'onclick="window.open(\'https://wa.me/923235792758\', \'_blank\'); return false;"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

update_file('index.html')
update_file('classes.html')

# Also update CSS for center alignment of course-foot and class-cta
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('justify-content:space-between;', 'justify-content:center;')
# Also center text in course-foot just in case
css = css.replace('.course-foot{display:flex;align-items:center;justify-content:space-between;', '.course-foot{display:flex;align-items:center;justify-content:center;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated HTML files and CSS.")
