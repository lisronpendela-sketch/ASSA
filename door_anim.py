import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the classes in the news section
old_html = """    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; align-items: start;">
      <div class="course-card reveal" style="padding: 1rem; background: var(--white);">
        <img src="news-1.jpg" alt="ASSA Flyer" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="course-card reveal d1" style="padding: 1rem; background: var(--white);">
        <img src="news-2.jpg" alt="FBISE Important Announcement" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="course-card reveal d2" style="padding: 1rem; background: var(--white);">
        <img src="news-3.jpg" alt="FBISE E-Kachehri" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
    </div>"""

new_html = """    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; align-items: start; perspective: 1500px;">
      <div class="course-card reveal door-anim" style="padding: 1rem; background: var(--white);">
        <img src="news-1.jpg" alt="ASSA Flyer" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="course-card reveal door-anim d1" style="padding: 1rem; background: var(--white);">
        <img src="news-2.jpg" alt="FBISE Important Announcement" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="course-card reveal door-anim d2" style="padding: 1rem; background: var(--white);">
        <img src="news-3.jpg" alt="FBISE E-Kachehri" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
    </div>"""

html = html.replace(old_html, new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_append = """
/* ═══ DOOR OPENING ANIMATION ═══ */
.reveal.door-anim {
  transform-origin: left center !important;
  transform: rotateY(90deg) !important;
  transition: opacity 0.6s var(--ease), transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
}
.reveal.door-anim.in {
  transform: rotateY(0deg) !important;
}
@media (prefers-reduced-motion: reduce) {
  .reveal.door-anim {
    transform: none !important;
    transition: opacity 0.6s ease !important;
  }
}
"""

if 'DOOR OPENING ANIMATION' not in css:
    css += css_append
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Door opening animation added to news section.")
