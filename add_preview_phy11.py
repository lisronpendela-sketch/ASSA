import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Card for Class 11 Physics (Book 5)
target_card = """<!-- Book 5 -->
      <div class="course-card reveal d1" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Physics</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Physics</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Physics%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>"""

replacement_card = """<!-- Book 5 -->
      <div class="course-card reveal d1" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Physics</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Physics</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon); width: 100%; text-align: center; margin-bottom: 0.5rem;">Rs. 499</div>
            <button class="btn-course" onclick="openPreview('phy11')" style="flex: 1; background: var(--navy); color: white; border: none; cursor: pointer; padding: 0.6rem 0.5rem; text-align: center; font-size: 0.9rem;">Free Preview</button>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Physics%20Formative%20Book." target="_blank" class="btn-course" style="flex: 1; text-decoration:none; text-align:center; padding: 0.6rem 0.5rem; font-size: 0.9rem;">Order on WA</a>
          </div>"""

if target_card in html:
    html = html.replace(target_card, replacement_card)
    print("Updated card HTML for Physics 11.")
else:
    print("Could not find exact card HTML for Physics 11 to replace.")

# 2. Add the JS previewData for phy11
phy11_js = """
  phy11: `
    <h4 style="margin-bottom: 1rem; color: var(--navy); font-size: 1.2rem;">Class 11 Physics</h4>
    <p style="margin-bottom: 1rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">This is probably your strongest preview page. There is a lot of genuinely valuable material in this PDF. The book covers selected Formative topics across areas including estimation, translatory motion, fluid mechanics, waves, electrostatics, relativity and particle physics.</p>
    
    <h5 style="margin-bottom: 0.8rem; color: var(--navy); font-size: 1.05rem;">What students will find inside:</h5>
    <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Estimation in Physics:</strong> Students learn how reasonable estimates can be used to check whether answers are physically sensible, plan experiments and solve problems more efficiently.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Equations of motion:</strong> The book provides focused treatment of the equations of uniformly accelerated motion, including their use in numerical problems and graphical interpretation.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Conservation of momentum:</strong> Students learn how conservation of momentum is applied to situations such as explosions, collisions, ball-and-bat interactions, rockets and other real-world examples.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Elastic and inelastic collisions:</strong> The book clearly distinguishes the two types of collisions and explains the relationship between conservation of momentum and kinetic energy.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Bernoulli effect and fluid pressure:</strong> Students explore how changes in fluid speed can produce pressure differences, with applications such as aeroplane wings, sprays and fluid systems.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Stationary waves:</strong> Coverage includes stationary waves, air columns, open and closed pipes, harmonics, resonance and experiments demonstrating stationary waves.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Interferometers and gravitational waves:</strong> Students are introduced to interferometers and their role in detecting extremely small changes associated with gravitational waves.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Ferrofluids:</strong> The book explains how magnetic fields affect ferrofluids and introduces their applications in electronics, optics and medical science.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Relativity and spacetime:</strong> Students explore the concept of time as a fourth dimension and use spacetime diagrams to understand relativistic ideas.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Matter and antimatter:</strong> The book covers antimatter, particle-antiparticle relationships, matter-antimatter asymmetry and related concepts.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Particle accelerators:</strong> Students learn the basic working principles of linear accelerators, synchrotrons and cyclotrons, along with their scientific and medical applications.</li>
    </ul>
    
    <div style="padding: 1rem; background: var(--ivory); border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem;">
      <strong style="color: var(--navy);">Best for:</strong> Students looking for deeper, organized preparation of difficult Class 11 Physics topics with numerical, conceptual and modern-physics coverage.
    </div>
  `,
"""

# Insert phy11_js right after 'const previewData = {\n'
if 'const previewData = {\n' in html:
    html = html.replace('const previewData = {\n', 'const previewData = {\n' + phy11_js)
    print("Injected JS for Physics 11.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
