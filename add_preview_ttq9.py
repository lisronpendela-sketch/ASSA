import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Card for Tarjuma Tul Quran 9
target_card = """<!-- Book 3 -->
      <div class="course-card reveal d2" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Tarjuma Tul Quran</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Tarjuma Tul Quran</li>
            <li><strong>Language:</strong> Urdu/Arabic</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Tarjuma%20Tul%20Quran%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>"""

replacement_card = """<!-- Book 3 -->
      <div class="course-card reveal d2" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Tarjuma Tul Quran</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Tarjuma Tul Quran</li>
            <li><strong>Language:</strong> Urdu/Arabic</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon); width: 100%; text-align: center; margin-bottom: 0.5rem;">Rs. 499</div>
            <button class="btn-course" onclick="openPreview('ttq9')" style="flex: 1; background: var(--navy); color: white; border: none; cursor: pointer; padding: 0.6rem 0.5rem; text-align: center; font-size: 0.9rem;">Free Preview</button>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Tarjuma%20Tul%20Quran%20Formative%20Book." target="_blank" class="btn-course" style="flex: 1; text-decoration:none; text-align:center; padding: 0.6rem 0.5rem; font-size: 0.9rem;">Order on WA</a>
          </div>"""

if target_card in html:
    html = html.replace(target_card, replacement_card)
    print("Updated card HTML for TTQ 9.")
else:
    print("Could not find exact card HTML for TTQ 9 to replace.")

# 2. Add the JS previewData for ttq9
ttq9_js = """
  ttq9: `
    <h4 style="margin-bottom: 1rem; color: var(--navy); font-size: 1.2rem;">Class 9 Tarjuma Tul Quran</h4>
    <p style="margin-bottom: 1rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">This is actually a strong selling point because the book has a very specific assessment focus. The PDF identifies Surah As-Saffat as the Formative Assessment portion for Class 9 Tarjuma Tul Quran, while the remaining Surahs are under Summative Assessment.</p>
    
    <h5 style="margin-bottom: 0.8rem; color: var(--navy); font-size: 1.05rem;">What students will find inside:</h5>
    <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Focused Formative Assessment preparation:</strong> Instead of mixing the entire Quran syllabus together, the book identifies the portion specifically allocated to Formative Assessment.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Surah As-Saffat focused preparation:</strong> The book specifically focuses on Surah As-Saffat, allowing students to concentrate on the designated assessment portion.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Organized assessment coverage:</strong> Students can identify exactly which portion requires focused preparation instead of spending unnecessary time searching through the complete syllabus.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Translation-focused learning:</strong> The resource is designed around Tarjuma Tul Quran preparation, helping students approach the designated Quranic content in an organized manner.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Exam-focused study approach:</strong> The content is structured to make preparation clearer and more assessment-oriented.</li>
      <li style="margin-bottom: 0.5rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Less confusion during preparation:</strong> Students can separate the designated Formative portion from the remaining Summative content.</li>
    </ul>
    
    <div style="padding: 1rem; background: var(--ivory); border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem;">
      <strong style="color: var(--navy);">Best for:</strong> Class 9 students who want focused preparation for the designated Tarjuma Tul Quran Formative Assessment portion.
    </div>
  `,
"""

# Insert ttq9_js right after 'const previewData = {\n'
if 'const previewData = {\n' in html:
    html = html.replace('const previewData = {\n', 'const previewData = {\n' + ttq9_js)
    print("Injected JS for TTQ 9.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
