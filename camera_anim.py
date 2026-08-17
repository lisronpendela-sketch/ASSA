import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

camera_click_css = """
/* ═══ CAMERA CLICK ANIMATION ═══ */
@keyframes cameraClick {
  0% { transform: scale(1); filter: brightness(1) contrast(1); }
  20% { transform: scale(0.96); filter: brightness(1.6) contrast(1.2); }
  100% { transform: scale(1); filter: brightness(1) contrast(1); }
}
.hero-circle:hover .hero-student img {
  animation: cameraClick 0.4s ease-out;
}
@media (prefers-reduced-motion: reduce) {
  .hero-circle:hover .hero-student img {
    animation: none !important;
  }
}
"""

if 'CAMERA CLICK ANIMATION' not in css:
    css += camera_click_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Camera click animation added.")
