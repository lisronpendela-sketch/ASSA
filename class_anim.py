import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .class-card transition
css = css.replace('transition:transform .3s var(--ease),box-shadow .3s var(--ease);', 'transition:translate .2s var(--ease),box-shadow .2s var(--ease);')

# 2. Update .class-card:hover
css = css.replace('.class-card:hover{box-shadow:var(--sh-lg)}', '.class-card:hover{translate:0 -5px;box-shadow:var(--sh-lg)}\n.class-card .class-top{transition:filter .2s var(--ease)}\n.class-card:hover .class-top{filter:brightness(1.1)}')

# 3. Update .reveal entry animations
old_reveal = """.reveal{opacity:0;transform:translateY(34px);transition:opacity .7s var(--ease),transform .7s var(--ease)}
.reveal.in{opacity:1;transform:translateY(0)}
.reveal.d1{transition-delay:.08s}
.reveal.d2{transition-delay:.16s}
.reveal.d3{transition-delay:.24s}
.reveal.d4{transition-delay:.32s}"""

new_reveal = """.reveal{opacity:0;transform:translateY(25px);transition:opacity .5s var(--ease),transform .5s var(--ease)}
.reveal.in{opacity:1;transform:translateY(0)}
.reveal.d1{transition-delay:.1s}
.reveal.d2{transition-delay:.2s}
.reveal.d3{transition-delay:.3s}
.reveal.d4{transition-delay:.4s}"""

if old_reveal in css:
    css = css.replace(old_reveal, new_reveal)
else:
    print("Warning: old reveal block not found perfectly, attempting regex...")
    css = re.sub(r'\.reveal\{opacity:0;transform:translateY\([^}]+\);transition:opacity [^}]+,transform [^}]+\}', '.reveal{opacity:0;transform:translateY(25px);transition:opacity .5s var(--ease),transform .5s var(--ease)}', css)
    css = re.sub(r'\.reveal\.d1\{transition-delay:[^}]+\}', '.reveal.d1{transition-delay:.1s}', css)
    css = re.sub(r'\.reveal\.d2\{transition-delay:[^}]+\}', '.reveal.d2{transition-delay:.2s}', css)
    css = re.sub(r'\.reveal\.d3\{transition-delay:[^}]+\}', '.reveal.d3{transition-delay:.3s}', css)
    css = re.sub(r'\.reveal\.d4\{transition-delay:[^}]+\}', '.reveal.d4{transition-delay:.4s}', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Class card animations updated.")
