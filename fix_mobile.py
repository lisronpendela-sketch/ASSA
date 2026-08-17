import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

start_marker = "/* " + chr(10024) + " MOBILE (" + chr(8804) + "600px) - single column everywhere " + chr(10024) + " */"
end_marker = "/* Social popup in hero */"

# Let's just use regex since the unicode chars might be problematic to match perfectly
pattern = r"/\*.*?MOBILE.*?600px.*?single column everywhere.*?\*/.*?/\* Social popup in hero \*/"

new_mobile_css = """/* MOBILE (600px) - single column everywhere */
@media(max-width:600px){
  .class-grid,.course-grid,.yt-grid,.why-grid{grid-template-columns:1fr}
  .stats-row{grid-template-columns:1fr 1fr}
  .footer-grid{grid-template-columns:1fr}
  .footer-bottom{flex-direction:column;text-align:center}
  /* larger tap targets on touch */
  .filter-btn{transition: background .2s var(--ease), color .2s var(--ease), transform .1s; padding:12px 20px}
  .btn{padding:14px 26px}
  .course-foot{flex-wrap:wrap;gap:.8rem}
  .course-foot .btn-course{width:100%;text-align:center;justify-content:center;padding:12px}
  
  /* Hero section adjustments for mobile */
  .hero { padding: 4.5rem 1rem 2rem !important; }
  .hero-inner { gap: 1.5rem !important; }
  .hero h1 { font-size: clamp(1.8rem, 7.5vw, 2.3rem); margin-bottom: 0.8rem; }
  .hero-sub { margin-bottom: 1.2rem; font-size: 1rem; }
  .hero-checks { margin-bottom: 1.5rem; gap: 0.8rem; flex-direction: column; align-items: center; }
  .hero-dots { display: none; }
  .hero-right { padding: 0 !important; max-width: 320px; margin: 0 auto; min-height: auto; }
  .hero-circle { width: clamp(200px, 68vw, 300px); height: clamp(200px, 68vw, 300px); }
  
  /* Floating stat badges adjustments */
  .stat-badge { padding: 4px 10px 4px 4px; gap: 6px; }
  .stat-badge .sb-ic { width: 30px; height: 30px; font-size: 0.85rem; }
  .stat-badge .sb-n { font-size: 0.85rem; }
  .stat-badge .sb-l { font-size: 0.6rem; margin-top: 1px; }

  /* Tighter zigzag positions */
  .sb-top { top: -2%; right: -3%; }
  .sb-mid-right { top: 38%; right: -5%; bottom: auto; }
  .sb-mid-left { top: 62%; left: -5%; }
  .sb-bottom { bottom: -2%; left: -3%; }
}

/* SMALL PHONES (420px) */
@media(max-width:420px){
  .hero h1 { font-size: clamp(1.6rem, 7.5vw, 2rem); }
  .stat-num { font-size: 2rem; }
  .about-points { grid-template-columns: 1fr; }
  .about-exp { right: -4px; }
  
  .sb-top { right: -4%; }
  .sb-mid-right { right: -6%; }
  .sb-mid-left { left: -6%; }
  .sb-bottom { left: -4%; }
  
  .topbar { font-size: .72rem; gap: .5rem; }
  .topbar-left { gap: .9rem; }
}

/* VERY SMALL (360px) - last-resort tightening, design intact */
@media(max-width:360px){
  .hero h1 { font-size: clamp(1.5rem, 7vw, 1.8rem); }
  .brand-text strong { font-size: .92rem; }
  .hero-cta { flex-direction: column; gap: 0.8rem; }
  .hero-cta .btn { width: 100%; justify-content: center; }
  
  .stat-badge { padding: 3px 8px 3px 3px; gap: 4px; }
  .stat-badge .sb-ic { width: 26px; height: 26px; font-size: 0.75rem; }
  .stat-badge .sb-n { font-size: 0.75rem; }
  .stat-badge .sb-l { font-size: 0.55rem; }
}

/* Social popup in hero */"""

match = re.search(pattern, css, flags=re.DOTALL)
if match:
    new_css = css[:match.start()] + new_mobile_css + css[match.end()-len("/* Social popup in hero */"):]
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("Successfully updated mobile styles!")
else:
    print("Regex match failed.")
