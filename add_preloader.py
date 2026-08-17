import re

html_inject = """
<!-- ═══ PRELOADER ═══ -->
<div id="preloader">
  <div class="pl-content">
    <div class="pl-logo">
      <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="width:60px;height:60px;">
        <circle cx="50" cy="50" r="48" fill="#14305C" stroke="#F0B429" stroke-width="3"/>
        <polygon points="50,26 78,38 50,50 22,38" fill="#F0B429"/>
        <path d="M34 44 L34 56 Q50 64 66 56 L66 44 L50 51 Z" fill="#8C1F28"/>
        <line x1="78" y1="38" x2="78" y2="54" stroke="#F0B429" stroke-width="2"/>
        <circle cx="78" cy="56" r="3" fill="#F0B429"/>
        <text x="50" y="80" text-anchor="middle" font-family="Poppins,sans-serif" font-weight="700" font-size="13" fill="#fff">AKBAR</text>
      </svg>
    </div>
    <div class="pl-line"></div>
  </div>
</div>
"""

css_inject = """
/* ═══ PRELOADER ═══ */
#preloader {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  animation: pl-exit 0.3s cubic-bezier(0.4, 0, 0.2, 1) 0.7s forwards;
  pointer-events: none;
}
.pl-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
.pl-logo {
  opacity: 0;
  transform: translateY(10px);
  animation: pl-logo 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
.pl-line {
  width: 0;
  height: 2px;
  background: var(--gold);
  border-radius: 2px;
  animation: pl-line 0.4s cubic-bezier(0.4, 0, 0.2, 1) 0.3s forwards;
}

@keyframes pl-logo {
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes pl-line {
  100% {
    width: 60px;
  }
}
@keyframes pl-exit {
  100% {
    opacity: 0;
    visibility: hidden;
  }
}
@media (prefers-reduced-motion: reduce) {
  #preloader { display: none; }
}
"""

def add_preloader_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'id="preloader"' not in html:
        html = re.sub(r'(<body>)', r'\1\n' + html_inject, html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

add_preloader_html('index.html')
add_preloader_html('classes.html')

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '#preloader' not in css:
    css += css_inject
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Preloader added.")
