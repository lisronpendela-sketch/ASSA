import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_about = re.search(r'<!-- ═══ ABOUT ═══ -->\s*<section class="section about" id="about">.*?</section>', html, re.DOTALL)

new_about = """<!-- ═══ ABOUT ═══ -->
<section class="section about" id="about">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">About the Academy</span>
      <h2 class="sec-title">Akbar Study Smart <span class="gold">Academy</span></h2>
      <p class="sec-desc" style="max-width: 800px; margin: 0 auto;">Akbar Study Smart Academy is an Official Educational Platform</p>
    </div>
    
    <div class="reveal" style="max-width: 900px; margin: 0 auto; text-align: center; font-size: 1.05rem; line-height: 1.7; color: var(--text);">
      <p style="margin-bottom: 1.2rem;">Akbar Study Smart Academy is a platform that helps students achieve their academic goals. We have experienced teachers who deeply explain every subject. We provide students with study materials, online classes, and test series to help them prepare well for their exams.</p>
      
      <p style="margin-bottom: 2rem;">The objective of Akbar Study Smart Academy is to provide students with knowledge and skills to succeed in their future. We help students achieve their goals and motivate them to fulfill their dreams. If you want to achieve your academic goals, Akbar Study Smart Academy can be a good option for you. To join us, you can contact us.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; text-align: left; background: var(--white); padding: 2rem; border-radius: var(--r-lg); box-shadow: var(--sh-sm); border: 1px solid var(--border);">
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">🎓</span> <span>FBISE 9th, 10th, 11th &amp; 12th Preparation</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">📝</span> <span>Important MCQs, Notes &amp; Guess Papers</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">📖</span> <span>Past Papers &amp; Paper Pattern Updates</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">🎯</span> <span>High Weightage Topics &amp; Exam Tips</span></div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-weight: 500; color: var(--navy);"><span style="font-size: 1.3rem;">🏛️</span> <span>Classes from PG to UNIVERSITY</span></div>
      </div>
      
      <div class="hero-cta center" style="margin-top: 2.5rem; justify-content: center;">
        <a href="https://wa.me/923235792758" target="_blank" class="btn btn-primary">📝 Enroll Now</a>
        <a href="#contact" class="btn" style="background:var(--navy);color:#fff">Contact Us</a>
      </div>
    </div>
  </div>
</section>"""

if old_about:
    html = html.replace(old_about.group(0), new_about)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("About section replaced successfully")
else:
    print("Could not find About section")
