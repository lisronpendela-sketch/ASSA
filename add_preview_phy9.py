import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Card for Physics 9
target_card = """<!-- Book 2 -->
      <div class="course-card reveal d1" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Physics</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Physics</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Physics%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>"""

replacement_card = """<!-- Book 2 -->
      <div class="course-card reveal d1" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Physics</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Physics</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon); width: 100%; text-align: center; margin-bottom: 0.5rem;">Rs. 499</div>
            <button class="btn-course" onclick="openPreview('phy9')" style="flex: 1; background: var(--navy); color: white; border: none; cursor: pointer; padding: 0.6rem 0.5rem; text-align: center; font-size: 0.9rem;">Free Preview</button>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Physics%20Formative%20Book." target="_blank" class="btn-course" style="flex: 1; text-decoration:none; text-align:center; padding: 0.6rem 0.5rem; font-size: 0.9rem;">Order on WA</a>
          </div>"""

if target_card in html:
    html = html.replace(target_card, replacement_card)
    print("Updated card HTML for Physics 9.")
else:
    print("Could not find exact card HTML for Physics 9 to replace.")

# 2. Add the JS previewData for phy9
phy9_js = """
  phy9: `
    <h4 style="margin-bottom: 1rem; color: var(--navy); font-size: 1.2rem;">Class 9 Physics</h4>
    <p style="margin-bottom: 1rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">This one has a particularly useful angle. The book identifies the practical/PBA areas separately, including measuring instruments and measurement skills. It specifically lists meter rule, measuring tape, Vernier caliper, screw gauge, cylinder measurement, stopwatch, significant figures and centre of gravity of irregular objects.</p>
    
    <h5 style="margin-bottom: 0.8rem; color: var(--navy); font-size: 1.05rem;">What students will find inside:</h5>
    <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Complete Class 9 Physics assessment coverage:</strong> The book is prepared around the FBiSE assessment framework and SLOs.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Practical measurement skills:</strong> Students get focused preparation for instruments and measurement concepts such as the meter rule, measuring tape, Vernier caliper and screw gauge.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Measurement-based understanding:</strong> The material covers taking measurements with a Vernier caliper and measuring cylindrical objects, helping students understand how measurement is applied practically.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Significant figures and rounding:</strong> Students can prepare for accurate presentation of measured values through rounding and significant-figure concepts.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Stopwatch and practical skills:</strong> The book highlights stopwatch-related practical assessment preparation.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Centre of gravity of irregular objects:</strong> The identified PBA material also includes the centre of gravity of irregular objects.</li>
      <li style="margin-bottom: 0.5rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Clear assessment distinction:</strong> The book explains that these practical topics are for Composite PBA and are not exclusive Formative Assessment topics.</li>
    </ul>
    
    <div style="padding: 1rem; background: var(--ivory); border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem;">
      <strong style="color: var(--navy);">Best for:</strong> Students who want stronger preparation for Physics concepts plus practical/PBA requirements.
    </div>
  `,
"""

# Insert phy9_js right after 'const previewData = {\n'
if 'const previewData = {' in html:
    html = html.replace('const previewData = {', 'const previewData = {\n' + phy9_js)
    print("Injected JS for Physics 9.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
