import re

files = ['index.html', 'classes.html']

social_html = """  <div class="topbar-social">
    <a href="https://whatsapp.com/channel/0029VbAMQxi7j6g2ycJ2jE09" target="_blank" rel="noopener" aria-label="WhatsApp Channel" title="WhatsApp Channel">✆</a>
    <a href="https://youtube.com/@akbarstudysmartacademy?si=3gcJ0zBQJgjN6ZDf" target="_blank" rel="noopener" aria-label="YouTube" title="YouTube">▶</a>
    <a href="https://www.facebook.com/share/18MpitdX3e/" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook">f</a>
    <a href="https://www.instagram.com/akbar_study_smart_academy?igsh=MTQ1N2doZjJ2Mnk3YQ==" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">📸</a>
    <a href="https://vt.tiktok.com/ZSCLLLBwM/" target="_blank" rel="noopener" aria-label="TikTok" title="TikTok">🎵</a>
  </div>"""

footer_social_html = """        <div class="footer-social">
          <a href="https://whatsapp.com/channel/0029VbAMQxi7j6g2ycJ2jE09" target="_blank" rel="noopener" aria-label="WhatsApp Channel" title="WhatsApp Channel">✆</a>
          <a href="https://youtube.com/@akbarstudysmartacademy?si=3gcJ0zBQJgjN6ZDf" target="_blank" rel="noopener" aria-label="YouTube" title="YouTube">▶</a>
          <a href="https://www.facebook.com/share/18MpitdX3e/" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook">f</a>
          <a href="https://www.instagram.com/akbar_study_smart_academy?igsh=MTQ1N2doZjJ2Mnk3YQ==" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">📸</a>
          <a href="https://vt.tiktok.com/ZSCLLLBwM/" target="_blank" rel="noopener" aria-label="TikTok" title="TikTok">🎵</a>
        </div>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace topbar-social
    html = re.sub(r'<div class="topbar-social">.*?</div>', social_html, html, flags=re.DOTALL)
    
    # Replace footer-social
    html = re.sub(r'<div class="footer-social">.*?</div>', footer_social_html, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Social links updated")
