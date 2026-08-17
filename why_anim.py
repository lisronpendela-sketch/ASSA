import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .why-card transition
css = css.replace('transition:.3s var(--ease);', 'transition:translate .2s var(--ease), box-shadow .2s var(--ease), border-color .2s var(--ease);')

# 2. Update .why-card:hover
css = css.replace('.why-card:hover{transform:translateY(-6px);box-shadow:var(--sh-md);border-color:rgba(240,180,41,.3)}', 
                  '.why-card:hover{translate:0 -3px;box-shadow:var(--sh-md);border-color:rgba(240,180,41,.3)}')

# 3. Add transitions to .why-ic
target_ic = 'background:linear-gradient(135deg,var(--navy),var(--navy-dark));box-shadow:0 8px 18px rgba(20,48,92,.25);\n}'
new_ic = 'background:linear-gradient(135deg,var(--navy),var(--navy-dark));box-shadow:0 8px 18px rgba(20,48,92,.25);\n  transition:transform .2s var(--ease), filter .2s var(--ease);\n}\n.why-card:hover .why-ic { transform: scale(1.05); filter: brightness(1.2); }'

if target_ic in css:
    css = css.replace(target_ic, new_ic)
else:
    # fallback regex
    css = re.sub(r'(\.why-ic\{[^}]*box-shadow:[^;]+;)(\n\})', r'\1\n  transition:transform .2s var(--ease), filter .2s var(--ease);\2\n.why-card:hover .why-ic { transform: scale(1.05); filter: brightness(1.2); }', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Why Choose Us animations updated.")
