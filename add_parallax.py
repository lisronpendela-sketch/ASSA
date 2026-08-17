import re

# 1. Update style.css
css_append = """
/* ═══ SUBTLE HERO PARALLAX ═══ */
.hero-right {
  --py: 0px;
}
.hero-circle, .stat-badge {
  translate: 0 var(--py);
  will-change: translate;
}
@media (prefers-reduced-motion: reduce) {
  .hero-circle, .stat-badge {
    translate: none !important;
  }
}
"""
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'SUBTLE HERO PARALLAX' not in css:
    css += css_append
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update index.html
js_append = """
/* ── Subtle Hero Parallax ── */
const heroRight = document.querySelector('.hero-right');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let tickParallax = false;
window.addEventListener('scroll', () => {
  if (!prefersReducedMotion.matches && heroRight && !tickParallax) {
    window.requestAnimationFrame(() => {
      const scrollY = window.scrollY;
      if (scrollY < 800) {
        // Move up to 15px max
        const y = Math.min(scrollY * 0.05, 15);
        heroRight.style.setProperty('--py', `-${y}px`);
      }
      tickParallax = false;
    });
    tickParallax = true;
  }
});
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'Subtle Hero Parallax' not in html:
    html = html.replace('/* ── Smooth anchor scroll ── */', js_append + '\n/* ── Smooth anchor scroll ── */')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Parallax added successfully.")
