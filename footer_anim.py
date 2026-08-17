import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add classes to footer elements
html = html.replace('<div class="footer-brand">', '<div class="footer-brand reveal fade-footer">')
# The other three footer-col divs
html = html.replace('<div class="footer-col">\n      <h4>Courses</h4>', '<div class="footer-col reveal fade-footer df-1">\n      <h4>Courses</h4>')
html = html.replace('<div class="footer-col">\n      <h4>Quick Links</h4>', '<div class="footer-col reveal fade-footer df-2">\n      <h4>Quick Links</h4>')
html = html.replace('<div class="footer-col">\n      <h4>Get In Touch</h4>', '<div class="footer-col reveal fade-footer df-3">\n      <h4>Get In Touch</h4>')

html = html.replace('<div class="footer-bottom">', '<div class="footer-bottom reveal line-anim">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_append = """
/* ═══ FOOTER SECTION ANIMATIONS ═══ */
.reveal.fade-footer {
  transform: translateY(15px) !important;
  transition: opacity 0.5s var(--ease), transform 0.5s var(--ease) !important;
}
.reveal.fade-footer.in {
  transform: translateY(0) !important;
}
.reveal.fade-footer.df-1 { transition-delay: 0.07s !important; }
.reveal.fade-footer.df-2 { transition-delay: 0.14s !important; }
.reveal.fade-footer.df-3 { transition-delay: 0.21s !important; }

/* Social Icons Hover */
.footer-social a:hover {
  transform: scale(1.05) !important;
}

/* Footer Line Animation */
.footer-bottom {
  border-top: none !important;
  position: relative;
}
.footer-bottom::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 1px;
  background: rgba(255,255,255,.08);
  width: 0;
  transition: width 0.5s var(--ease) 0.3s;
}
.reveal.line-anim {
  transform: translateY(10px) !important;
  transition: opacity 0.5s var(--ease) 0.3s, transform 0.5s var(--ease) 0.3s !important;
}
.reveal.line-anim.in {
  transform: translateY(0) !important;
}
.reveal.line-anim.in::before {
  width: 100%;
}
"""

if 'FOOTER SECTION ANIMATIONS' not in css:
    css += css_append
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Footer section animations updated.")
