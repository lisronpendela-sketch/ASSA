import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_cta_pattern = r'<!-- ═══ FINAL CTA ═══ -->\s*<section class="section cta-band">\s*<div class="container reveal">\s*<h2>Ready to <span class="gold">study smart</span> and score higher\?</h2>\s*<p>Join Akbar Study Smart Academy today.*?</div>\s*</div>\s*</section>'

new_cta_html = """<!-- ═══ FINAL CTA ═══ -->
<section class="section cta-band">
  <div class="container">
    <h2 class="reveal scale-cta">Ready to <span class="gold">study smart</span> and score higher?</h2>
    <p class="reveal d1">Join Akbar Study Smart Academy today. Pick your class, enroll on WhatsApp, and start your journey to top board results.</p>
    <div class="hero-cta reveal d2">
      <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20enroll%20at%20Akbar%20Study%20Smart%20Academy." target="_blank" rel="noopener" class="btn btn-wa">💬 Enroll on WhatsApp</a>
      <a href="#courses" class="btn btn-outline-light">View All Courses</a>
    </div>
  </div>
</section>"""

if re.search(old_cta_pattern, html, flags=re.DOTALL):
    html = re.sub(old_cta_pattern, new_cta_html, html, flags=re.DOTALL)
else:
    print("Warning: old CTA not found precisely.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_append = """
/* ═══ FINAL CTA ANIMATIONS ═══ */
.reveal.scale-cta {
  transform: scale(0.96) !important;
  transition: opacity 0.6s var(--ease), transform 0.6s var(--ease) !important;
}
.reveal.scale-cta.in {
  transform: scale(1) !important;
}
"""
if 'FINAL CTA ANIMATIONS' not in css:
    css += css_append

# Update .btn-wa:hover
css = css.replace('.btn-wa:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(37,211,102,.5)}', '.btn-wa:hover{transform:translateY(-3px);box-shadow:0 12px 24px rgba(37,211,102,.3)}')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CTA section animations updated.")
