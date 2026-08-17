import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Card for Tarjuma Tul Quran 11 (Book 6)
target_card = """<!-- Book 6 -->
      <div class="course-card reveal d2" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Tarjuma Tul Quran</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Tarjuma Tul Quran</li>
            <li><strong>Language:</strong> Urdu/Arabic</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Tarjuma%20Tul%20Quran%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>"""

replacement_card = """<!-- Book 6 -->
      <div class="course-card reveal d2" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Tarjuma Tul Quran</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Tarjuma Tul Quran</li>
            <li><strong>Language:</strong> Urdu/Arabic</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon); width: 100%; text-align: center; margin-bottom: 0.5rem;">Rs. 499</div>
            <button class="btn-course" onclick="openPreview('ttq11')" style="flex: 1; background: var(--navy); color: white; border: none; cursor: pointer; padding: 0.6rem 0.5rem; text-align: center; font-size: 0.9rem;">Free Preview</button>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Tarjuma%20Tul%20Quran%20Formative%20Book." target="_blank" class="btn-course" style="flex: 1; text-decoration:none; text-align:center; padding: 0.6rem 0.5rem; font-size: 0.9rem;">Order on WA</a>
          </div>"""

if target_card in html:
    html = html.replace(target_card, replacement_card)
    print("Updated card HTML for TTQ 11.")
else:
    print("Could not find exact card HTML for TTQ 11 to replace.")

# 2. Add the JS previewData for ttq11
ttq11_js = """
  ttq11: `
    <h4 style="margin-bottom: 1rem; color: var(--navy); font-size: 1.2rem;">Class 11 Tarjuma Tul Quran</h4>
    <p style="margin-bottom: 1rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">This one also has a very clear selling point because the book identifies 15 Surahs for Formative Assessment.</p>
    
    <h5 style="margin-bottom: 0.8rem; color: var(--navy); font-size: 1.05rem;">What students will find inside:</h5>
    <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>15 designated Surahs for Formative Assessment:</strong> The book covers Surah An-Nisa, Al-Ma'idah, An-Noor, Al-Ahzab, Muhammad, Al-Fath, Al-Hujurat, Al-Hadid, Al-Mumtahanah, As-Saff, Al-Jumu'ah, Al-Munafiqun, At-Taghabun, At-Talaq, and At-Tahrim.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Assessment-specific organization:</strong> The book identifies the Surahs that fall under Formative Assessment so students can focus their preparation accordingly.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Structured Quran preparation:</strong> Instead of approaching the syllabus randomly, students can work through the designated Surahs systematically.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Focused examination preparation:</strong> The stated purpose is to make preparation focused, structured and assessment-oriented.</li>
      <li style="margin-bottom: 0.5rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Better study planning:</strong> Students can clearly identify the content relevant to their Formative Assessment and plan their study time accordingly.</li>
    </ul>
    
    <div style="padding: 1rem; background: var(--ivory); border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem;">
      <strong style="color: var(--navy);">Best for:</strong> Class 11 students who want organized and assessment-focused preparation across the designated Tarjuma Tul Quran Surahs.
    </div>
  `,
"""

# Insert ttq11_js right after 'const previewData = {\n'
if 'const previewData = {\n' in html:
    html = html.replace('const previewData = {\n', 'const previewData = {\n' + ttq11_js)
    print("Injected JS for TTQ 11.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
