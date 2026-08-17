import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update the underline duration to 200ms
css = re.sub(r'transition:transform \.25s var\(--ease\)', r'transition:transform .2s var(--ease)', css)

# 2. Append Nav Entrance Animations
nav_animation_css = """
/* ═══ NAV ENTRANCE ANIMATION ═══ */
@keyframes nav-enter {
  0% { opacity: 0; transform: translateY(-8px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* Base delay is 0.7s to wait for preloader to finish */
.brand { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.7s forwards; opacity: 0; }
.nav-links > li:nth-child(1) { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.75s forwards; opacity: 0; }
.nav-links > li:nth-child(2) { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.8s forwards; opacity: 0; }
.nav-links > li:nth-child(3) { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.85s forwards; opacity: 0; }
.nav-links > li:nth-child(4) { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.9s forwards; opacity: 0; }
.nav-links > li:nth-child(5) { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.95s forwards; opacity: 0; }
.nav-links > li:nth-child(6) { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.0s forwards; opacity: 0; }
.nav-right, .m-nav-right, .hamburger, .m-enroll { animation: nav-enter 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.95s forwards; opacity: 0; }

@media (prefers-reduced-motion: reduce) {
  .brand, .nav-links > li, .nav-right, .m-nav-right, .hamburger, .m-enroll {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
  }
}
"""

if 'nav-enter' not in css:
    css += nav_animation_css
    
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Nav animations applied successfully.")
