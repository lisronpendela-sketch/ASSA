import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Card for Class 11 Computer Science (Book 4)
target_card = """<!-- Book 4 -->
      <div class="course-card reveal" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Computer Science</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Computer Science</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Computer%20Science%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>"""

replacement_card = """<!-- Book 4 -->
      <div class="course-card reveal" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Computer Science</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Computer Science</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon); width: 100%; text-align: center; margin-bottom: 0.5rem;">Rs. 499</div>
            <button class="btn-course" onclick="openPreview('cs11')" style="flex: 1; background: var(--navy); color: white; border: none; cursor: pointer; padding: 0.6rem 0.5rem; text-align: center; font-size: 0.9rem;">Free Preview</button>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Computer%20Science%20Formative%20Book." target="_blank" class="btn-course" style="flex: 1; text-decoration:none; text-align:center; padding: 0.6rem 0.5rem; font-size: 0.9rem;">Order on WA</a>
          </div>"""

if target_card in html:
    html = html.replace(target_card, replacement_card)
    print("Updated card HTML for CS 11.")
else:
    print("Could not find exact card HTML for CS 11 to replace.")

# 2. Add the JS previewData for cs11
cs11_js = """
  cs11: `
    <h4 style="margin-bottom: 1rem; color: var(--navy); font-size: 1.2rem;">Class 11 Computer Science</h4>
    <p style="margin-bottom: 1rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">Here I would not claim that the book contains exclusive Formative topics, because the PDF itself says there are essentially no standalone Formative Assessment topics. It covers 8 chapters, with different assessment allocations.</p>
    
    <h5 style="margin-bottom: 0.8rem; color: var(--navy); font-size: 1.05rem;">What students will find inside:</h5>
    <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Complete 8-chapter coverage:</strong> The book is organized across all eight chapters of the Class 11 Computer Science syllabus.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Official assessment distribution:</strong> The content follows the assessment distribution rather than treating every chapter as identical.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Chapter 1 assessment focus:</strong> The first SLO of Chapter 1 is identified within Composite PBA.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Chapters 2, 3 and 4:</strong> These chapters are included in both Theory Assessment and Composite PBA, making them important for broader examination preparation.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Chapters 5 and 6:</strong> These chapters are included in Theory Assessment, giving students focused theoretical preparation.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Chapters 7 and 8:</strong> These chapters are included in both Theory Assessment and Composite PBA.</li>
      <li style="margin-bottom: 0.5rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Structured preparation:</strong> The book is designed around the prescribed assessment distribution so students can understand where different parts of the syllabus fit.</li>
    </ul>
    
    <div style="padding: 1rem; background: var(--ivory); border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem;">
      <strong style="color: var(--navy);">Best for:</strong> Class 11 Computer Science students who want their preparation organized according to the FBiSE assessment structure.
    </div>
  `,
"""

# Insert cs11_js right after 'const previewData = {\n'
if 'const previewData = {\n' in html:
    html = html.replace('const previewData = {\n', 'const previewData = {\n' + cs11_js)
    print("Injected JS for CS 11.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
