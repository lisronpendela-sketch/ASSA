import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Card for CS 9
target_card = """<div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Computer%20Science%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>"""

replacement_card = """<div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon); width: 100%; text-align: center; margin-bottom: 0.5rem;">Rs. 499</div>
            <button class="btn-course" onclick="openPreview('cs9')" style="flex: 1; background: var(--navy); color: white; border: none; cursor: pointer; padding: 0.6rem 0.5rem; text-align: center; font-size: 0.9rem;">Free Preview</button>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Computer%20Science%20Formative%20Book." target="_blank" class="btn-course" style="flex: 1; text-decoration:none; text-align:center; padding: 0.6rem 0.5rem; font-size: 0.9rem;">Order on WA</a>
          </div>"""

if target_card in html:
    html = html.replace(target_card, replacement_card)
    print("Updated card HTML.")
else:
    print("Could not find exact card HTML to replace.")

# 2. Add Modal HTML before enrollModal
modal_html = """
<!-- PREVIEW MODAL -->
<div class="modal-overlay" id="previewModal">
  <div class="modal" role="dialog" aria-modal="true" aria-labelledby="previewModalTitle" style="max-width: 600px;">
    <div class="modal-head">
      <button class="modal-close" onclick="closePreview()" aria-label="Close">×</button>
      <h3 id="previewModalTitle">Book Preview</h3>
      <p id="previewModalSub">See what's inside before you purchase</p>
    </div>
    <div class="modal-body">
      <div id="previewContent" style="max-height: 60vh; overflow-y: auto; padding-right: 10px;">
        <!-- Dynamic content -->
      </div>
      <div class="course-foot" style="margin-top: 1.5rem; justify-content: center;">
         <button class="btn btn-primary" onclick="closePreview()" style="width: 100%; padding: 12px; background: var(--navy); color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">Close Preview</button>
      </div>
    </div>
  </div>
</div>

<div class="modal-overlay" id="enrollModal">"""

if '<div class="modal-overlay" id="enrollModal">' in html and 'id="previewModal"' not in html:
    html = html.replace('<div class="modal-overlay" id="enrollModal">', modal_html)
    print("Injected modal HTML.")

# 3. Add JS at the end
js_code = """
/* Book Previews */
const previewData = {
  cs9: `
    <h4 style="margin-bottom: 1rem; color: var(--navy); font-size: 1.2rem;">Class 9 Computer Science</h4>
    <p style="margin-bottom: 1rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">The PDF specifically states that all 7 chapters are relevant to the official assessment framework, with no separate exclusive Formative Assessment topics. It covers both Theory Assessment and Performance-Based Assessment (PBA).</p>
    
    <h5 style="margin-bottom: 0.8rem; color: var(--navy); font-size: 1.05rem;">What students will find inside:</h5>
    <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; font-size: 0.95rem; color: var(--text); line-height: 1.6;">
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Complete 7-chapter coverage:</strong> The book brings the complete Class 9 Computer Science syllabus into one organized resource instead of making students search through different parts of the textbook.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>FBiSE Assessment Framework alignment:</strong> Content is organized according to the assessment framework so students can understand what is relevant for examination preparation.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Theory + PBA preparation:</strong> All seven chapters are relevant to Theory Assessment and PBA, helping students prepare beyond simple textbook reading.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Assessment-focused preparation:</strong> The material is designed around what students need to understand and prepare for assessment rather than unnecessary textbook repetition.</li>
      <li style="margin-bottom: 0.8rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Organized revision:</strong> Students can use the book as a focused revision resource instead of repeatedly going through the entire textbook.</li>
      <li style="margin-bottom: 0.5rem; position: relative; padding-left: 1.2rem;"><span style="color: var(--maroon); position: absolute; left: 0; top: 0;">•</span><strong>Better understanding of the complete syllabus:</strong> Because there are no exclusive Formative Assessment topics in Class 9 Computer Science, the book helps students maintain coverage across the complete syllabus.</li>
    </ul>
    
    <div style="padding: 1rem; background: var(--ivory); border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem;">
      <strong style="color: var(--navy);">Best for:</strong> Students who want one organized Computer Science resource for structured exam preparation.
    </div>
  `
};

const pModal = document.getElementById('previewModal');
function openPreview(bookId) {
  if (previewData[bookId] && pModal) {
    document.getElementById('previewContent').innerHTML = previewData[bookId];
    pModal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
}
function closePreview() {
  if (pModal) {
    pModal.classList.remove('open');
    document.body.style.overflow = '';
  }
}
if(pModal) {
  pModal.addEventListener('click', e => { if(e.target === pModal) closePreview(); });
}
"""

if 'const previewData =' not in html:
    html = html.replace('</script>', js_code + '\n</script>')
    print("Injected JS.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
