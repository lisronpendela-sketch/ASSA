import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore 600px segment
pattern_600 = r"/\* MOBILE \(600px\).*?/\* Social popup in hero \*/"
replacement_600 = """/* MOBILE (600px) - single column everywhere */
@media(max-width:600px){
  .class-grid,.course-grid,.yt-grid,.why-grid{grid-template-columns:1fr}
  .stats-row{grid-template-columns:1fr 1fr}
  .footer-grid{grid-template-columns:1fr}
  .footer-bottom{flex-direction:column;text-align:center}
  /* larger tap targets (44px) on touch */
  .filter-btn{transition: background .2s var(--ease), color .2s var(--ease), transform .1s; padding:12px 20px}
  .btn{padding:14px 26px}
  .course-foot{flex-wrap:wrap;gap:.8rem}
  .course-foot .btn-course{width:100%;text-align:center;justify-content:center;padding:12px}
  .hero-circle{width:clamp(230px,74vw,360px);height:clamp(230px,74vw,360px)}
  .sb-top{top:8%;right:0}
  .sb-bottom{bottom:10%;left:0}
  .sb-mid-left{top:45%;left:0}
  .sb-mid-right{bottom:45%;right:0}

}

/* SMALL PHONES (420px) */
@media(max-width:420px){
  .stat-num{font-size:2rem}
  .hero-checks{gap:.9rem;flex-direction:column;align-items:center}
  .hero-dots{display:none}
  .about-points{grid-template-columns:1fr}
  .about-exp{right:-4px}
  .stat-badge{padding:6px 13px 6px 6px}
  .stat-badge .sb-ic{width:36px;height:36px;font-size:1rem}
  .stat-badge .sb-n{font-size:.98rem}
  .stat-badge .sb-l{font-size:.66rem}
  .topbar{font-size:.72rem;gap:.5rem}
  .topbar-left{gap:.9rem}
}

/* VERY SMALL (360px) - last-resort tightening, design intact */
@media(max-width:360px){
  .brand-text strong{font-size:.92rem}
  .hero-cta{flex-direction:column}
  .hero-cta .btn{width:100%;justify-content:center}
  .sb-top,.sb-bottom,.sb-mid-left,.sb-mid-right{transform:scale(.92)}
}

/* Social popup in hero */"""

css = re.sub(pattern_600, replacement_600, css, flags=re.DOTALL)

# Restore 768px segment
pattern_768 = r"\.sb-top\{top:2%;right:-2%\}\s*\.sb-bottom\{bottom:2%;left:-2%\}\s*\.sb-mid-left\{top:65%;left:-2%\}\s*\.sb-mid-right\{top:30%;right:-2%;bottom:auto\}"
replacement_768 = """.sb-top{top:10%;right:0}
  .sb-bottom{bottom:12%;left:0}
  .sb-mid-left{top:45%;left:0}
  .sb-mid-right{bottom:45%;right:0}"""

css = re.sub(pattern_768, replacement_768, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored style.css successfully!")
