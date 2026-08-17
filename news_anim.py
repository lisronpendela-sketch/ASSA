import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

news_anim = """
/* ═══ NEWS SECTION ANIMATIONS ═══ */
#news .course-card:hover {
  translate: 0 -4px;
}
#news .course-card img {
  transition: transform 0.25s var(--ease);
}
#news .course-card:hover img {
  transform: scale(1.03);
}
"""

if 'NEWS SECTION ANIMATIONS' not in css:
    css += news_anim
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("News section animations updated.")
