import re

# 1. Update index.html to add test-card class
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_div = '<div style="background: var(--white); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 2.5rem 1.5rem; max-width: 700px; margin: 0 auto; box-shadow: var(--sh-md); text-align: center;" class="reveal">'
new_div = '<div style="background: var(--white); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 2.5rem 1.5rem; max-width: 700px; margin: 0 auto; box-shadow: var(--sh-md); text-align: center;" class="test-card reveal">'

if target_div in html:
    html = html.replace(target_div, new_div)
else:
    print("Warning: tests div not exactly matched, using regex")
    html = re.sub(r'(id="tests".*?class=")(reveal)(")', r'\1test-card \2\3', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add test card animations to style.css
css_append = """
/* ═══ TESTS SECTION ANIMATIONS ═══ */
.test-card.reveal {
  transform: scale(0.98);
}
.test-card.reveal.in {
  transform: scale(1);
}
#tests .btn-primary {
  transition: transform 0.2s var(--ease), box-shadow 0.2s var(--ease);
}
#tests .btn-primary:hover {
  transform: translateY(-2px) !important;
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'TESTS SECTION ANIMATIONS' not in css:
    css += css_append
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Tests section animations updated.")
