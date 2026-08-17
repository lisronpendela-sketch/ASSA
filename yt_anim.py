import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update yt-card transition and hover
css = css.replace('transition:translate .2s var(--ease), box-shadow .2s var(--ease), border-color .2s var(--ease);', 'transition:translate .25s var(--ease), box-shadow .25s var(--ease), border-color .25s var(--ease);')
css = css.replace('.yt-card:hover{transform:translateY(-6px);box-shadow:var(--sh-lg)}', '.yt-card:hover{translate:0 -4px;box-shadow:var(--sh-lg)}')

# 2. Add transition to image
if '.yt-thumb img' not in css:
    css += '\n.yt-thumb img { transition: transform 0.25s var(--ease); }\n.yt-card:hover .yt-thumb img { transform: scale(1.03); }\n'

# 3. Update yt-play hover
css = css.replace('transition:.25s var(--ease);', 'transition:transform .25s var(--ease);')
css = css.replace('.yt-card:hover .yt-play{transform:scale(1.12)}', '.yt-card:hover .yt-play{transform:scale(1.08)}')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Free lectures animations updated.")
