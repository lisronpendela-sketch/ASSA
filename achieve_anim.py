import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_func = """function countUp(el){
  const target=parseFloat(el.dataset.count),suffix=el.dataset.suffix||'';
  const dur=1800,start=performance.now();"""

new_func = """function countUp(el){
  const target=parseFloat(el.dataset.count),suffix=el.dataset.suffix||'';
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = target + suffix; return; }
  const dur=1200,start=performance.now();"""

if old_func in html:
    html = html.replace(old_func, new_func)
else:
    print("Warning: old countUp func not found exactly.")
    # fallback
    html = html.replace('const dur=1800', "if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = target + suffix; return; }\n  const dur=1200")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Achievements animations updated.")
