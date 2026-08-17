import re

svgs = {
    'wa': '<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>',
    'yt': '<svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 0 0-2.122 2.136C0 8.07 0 12 0 12s0 3.93.501 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>',
    'fb': '<svg viewBox="0 0 24 24"><path d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692v-3.622h3.128V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116c.73 0 1.323-.593 1.323-1.325V1.325C24 .593 23.407 0 22.675 0z"/></svg>',
    'ig': '<svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>',
    'tk': '<svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 15.71a6.34 6.34 0 0 0 11.2 4.14V7.43a8.3 8.3 0 0 0 4 1.89v-3.1a4.93 4.93 0 0 1-2.61-.43l-.06.01z"/></svg>'
}

hero_social_html = f"""      <div class="hero-social-pop">
        <span class="hsp-text">Connect with us:</span>
        <a href="https://whatsapp.com/channel/0029VbAMQxi7j6g2ycJ2jE09" target="_blank" rel="noopener" aria-label="WhatsApp Channel" class="hsp-ic hsp-wa">{svgs['wa']}</a>
        <a href="https://youtube.com/@akbarstudysmartacademy?si=3gcJ0zBQJgjN6ZDf" target="_blank" rel="noopener" aria-label="YouTube" class="hsp-ic hsp-yt">{svgs['yt']}</a>
        <a href="https://www.facebook.com/share/18MpitdX3e/" target="_blank" rel="noopener" aria-label="Facebook" class="hsp-ic hsp-fb">{svgs['fb']}</a>
        <a href="https://www.instagram.com/akbar_study_smart_academy?igsh=MTQ1N2doZjJ2Mnk3YQ==" target="_blank" rel="noopener" aria-label="Instagram" class="hsp-ic hsp-ig">{svgs['ig']}</a>
        <a href="https://vt.tiktok.com/ZSCLLLBwM/" target="_blank" rel="noopener" aria-label="TikTok" class="hsp-ic hsp-tk">{svgs['tk']}</a>
      </div>"""

def replace_social_icons(html_content, class_name):
    # Regex to find the div
    div_pattern = f'<div class="{class_name}">.*?</div>'
    match = re.search(div_pattern, html_content, re.DOTALL)
    if not match:
        return html_content
    
    div_content = match.group(0)
    
    # Replace characters with SVGs
    div_content = div_content.replace('>✆<', f'>{svgs["wa"]}<')
    div_content = div_content.replace('>▶<', f'>{svgs["yt"]}<')
    div_content = div_content.replace('>f<', f'>{svgs["fb"]}<')
    div_content = div_content.replace('>📸<', f'>{svgs["ig"]}<')
    div_content = div_content.replace('>🎵<', f'>{svgs["tk"]}<')
    
    return html_content.replace(match.group(0), div_content)

for filename in ['index.html', 'classes.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace in topbar and footer
    html = replace_social_icons(html, 'topbar-social')
    html = replace_social_icons(html, 'footer-social')
    
    if filename == 'index.html':
        # Add to hero right after hero-cta
        if 'hero-social-pop' not in html:
            html = html.replace('</div>\n    </div>\n\n    <div class="hero-right">', f'</div>\n{hero_social_html}\n    </div>\n\n    <div class="hero-right">')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

css_addition = """
/* Social popup in hero */
.hero-social-pop {
  margin-top: 2rem;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
.hsp-text {
  font-family: var(--f-head);
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--muted);
  margin-right: 6px;
}
.hsp-ic {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--white);
  color: var(--navy);
  transition: 0.3s var(--ease);
  border: 1px solid var(--border);
}
.hsp-ic svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
}
.hsp-ic:hover {
  transform: translateY(-4px);
  border-color: transparent;
}
.hsp-wa:hover { background: #25D366; color: #fff; box-shadow: 0 8px 20px rgba(37,211,102,.35); }
.hsp-yt:hover { background: #FF0000; color: #fff; box-shadow: 0 8px 20px rgba(255,0,0,.35); }
.hsp-fb:hover { background: #1877F2; color: #fff; box-shadow: 0 8px 20px rgba(24,119,242,.35); }
.hsp-ig:hover { background: #E1306C; color: #fff; box-shadow: 0 8px 20px rgba(225,48,108,.35); }
.hsp-tk:hover { background: #000000; color: #fff; box-shadow: 0 8px 20px rgba(0,0,0,.35); }

/* Ensure topbar and footer SVGs are sized right */
.topbar-social a svg { width: 14px; height: 14px; fill: currentColor; }
.footer-social a svg { width: 18px; height: 18px; fill: currentColor; }
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_addition)

print("Icons updated successfully!")
