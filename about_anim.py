import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the About section using regex to match from <!-- ═══ ABOUT ═══ --> to <!-- ═══ FINAL CTA ═══ -->
old_about_pattern = r'<!-- ═══ ABOUT ═══ -->.*?<!-- ═══ FINAL CTA ═══ -->'

new_about_html = """<!-- ═══ ABOUT ═══ -->
<section class="section about" id="about">
  <div class="container">
    <div class="sec-head center">
      <div class="reveal">
        <span class="eyebrow">About the Academy</span>
        <h2 class="sec-title">Akbar Study Smart <span class="gold">Academy</span></h2>
      </div>
      <p class="sec-desc reveal d1" style="max-width: 800px; margin: 0 auto;">Akbar Study Smart Academy is an Official Educational Platform</p>
    </div>
    
    <div style="max-width: 900px; margin: 0 auto; text-align: center; font-size: 1.05rem; line-height: 1.7; color: var(--text);">
      <div class="reveal fade-only d2">
        <p style="margin-bottom: 1.2rem;">Akbar Study Smart Academy is a platform that helps students achieve their academic goals. We have experienced teachers who deeply explain every subject. We provide students with study materials, online classes, and test series to help them prepare well for their exams.</p>
        <p style="margin-bottom: 2rem;">The objective of Akbar Study Smart Academy is to provide students with knowledge and skills to succeed in their future. We help students achieve their goals and motivate them to fulfill their dreams. If you want to achieve your academic goals, Akbar Study Smart Academy can be a good option for you. To join us, you can contact us.</p>
      </div>
      
      <div class="feature-grid reveal d3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; text-align: left; background: var(--white); padding: 2rem; border-radius: var(--r-lg); box-shadow: var(--sh-sm); border: 1px solid var(--border);">
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">🎓</span> <span>FBISE 9th, 10th, 11th &amp; 12th Preparation</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">📝</span> <span>Important MCQs, Notes &amp; Guess Papers</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">📖</span> <span>Past Papers &amp; Paper Pattern Updates</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">🎯</span> <span>High Weightage Topics &amp; Exam Tips</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">🏛️</span> <span>Classes from PG to UNIVERSITY</span></div>
      </div>
      
      <div class="hero-cta center reveal d4" style="margin-top: 2.5rem; justify-content: center;">
        <a href="https://wa.me/923235792758" target="_blank" class="btn btn-primary">📝 Enroll Now</a>
        <a href="#contact" class="btn" style="background:var(--navy);color:#fff">Contact Us</a>
      </div>
    </div>
  </div>
</section>

<!-- ═══ FINAL CTA ═══ -->"""

html = re.sub(old_about_pattern, new_about_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_append = """
/* ═══ ABOUT SECTION ANIMATIONS ═══ */
.reveal.fade-only {
  transform: none !important;
}
#about .feature-grid > div {
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.3s var(--ease), transform 0.3s var(--ease);
}
#about .feature-grid.in > div {
  opacity: 1;
  transform: translateY(0);
}
#about .feature-grid.in > div:nth-child(1) { transition-delay: 0.35s; }
#about .feature-grid.in > div:nth-child(2) { transition-delay: 0.40s; }
#about .feature-grid.in > div:nth-child(3) { transition-delay: 0.45s; }
#about .feature-grid.in > div:nth-child(4) { transition-delay: 0.50s; }
#about .feature-grid.in > div:nth-child(5) { transition-delay: 0.55s; }
#about .feature-grid.in > div:nth-child(6) { transition-delay: 0.60s; }
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'ABOUT SECTION ANIMATIONS' not in css:
    css += css_append
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("About section animations updated.")
