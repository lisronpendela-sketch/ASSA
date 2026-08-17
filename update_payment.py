import re

files = ['index.html', 'classes.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update footer payment method text
    html = html.replace('JazzCash · Easypaisa · Bank', 'Easypaisa · Meezan Bank')

    # 2. Update Modal HTML
    # Remove the whole modal-body and replace it to be exact
    old_modal_body = re.search(r'<div class="modal-body">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
    if old_modal_body:
        new_modal_body = """<div class="modal-body">
      <div class="modal-course" id="modalCourse">
        <span class="mc-name">Selected Course</span>
      </div>

      <div class="modal-steps">
        <div class="modal-step"><span class="step-n"></span><span class="step-txt">Send your fee to any account below (Easypaisa / Meezan Bank).</span></div>
        <div class="modal-step"><span class="step-n"></span><span class="step-txt">Take a screenshot of your payment confirmation.</span></div>
        <div class="modal-step"><span class="step-n"></span><span class="step-txt">Send the screenshot to us on WhatsApp with your class &amp; name.</span></div>
        <div class="modal-step"><span class="step-n"></span><span class="step-txt">We confirm &amp; add you to the private class WhatsApp group + Google Drive (notes &amp; tests).</span></div>
      </div>

      <div class="pay-methods">
        <div class="pay-method"><div class="pay-logo pm-easy">Easy<br>paisa</div><div class="pay-info"><div class="pm-name">Easypaisa</div><div class="pm-num">03100878172</div><div class="pm-title">Akbar Study Smart Academy</div></div></div>
        <div class="pay-method" style="border-left: 4px solid #552781;"><div class="pay-logo pm-bank" style="background:#552781;color:#fff;">MEEZAN</div><div class="pay-info"><div class="pm-name">Meezan Bank</div><div class="pm-num">00300114966512</div><div class="pm-title">Akbar Study Smart Academy</div></div></div>
      </div>

      <a class="btn btn-wa" id="modalWaBtn" href="https://wa.me/923235792758" target="_blank" rel="noopener">💬 Send Screenshot on WhatsApp (0323-5792758)</a>
    </div>
  </div>
</div>"""
        html = html.replace(old_modal_body.group(0), new_modal_body)

    # 3. Update the openEnroll javascript
    old_js = re.search(r'function openEnroll.*?modal\.classList\.add\(\'open\'\);document\.body\.style\.overflow=\'hidden\';\n}', html, re.DOTALL)
    if old_js:
        new_js = """function openEnroll(name,price){
  const mc=document.getElementById('modalCourse');
  if(name){mc.style.display='flex';mc.querySelector('.mc-name').textContent=name;}
  else{mc.style.display='none';}
  document.getElementById('modalTitle').textContent='Enroll Now';
  const msg=encodeURIComponent('Assalam-o-Alaikum! I want to enroll in: '+name+'. Please guide me.');
  document.getElementById('modalWaBtn').href='https://wa.me/923235792758?text='+msg;
  modal.classList.add('open');document.body.style.overflow='hidden';
}"""
        html = html.replace(old_js.group(0), new_js)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated payment details in HTML files.")
