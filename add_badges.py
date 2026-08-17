import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
.sb-mid-left{top:45%;left:-8%;animation-delay:-1.2s}
.sb-mid-left .sb-ic{background:linear-gradient(135deg,var(--gold),var(--gold-dark));color:var(--navy-dark)}
.sb-mid-right{bottom:45%;right:-6%;animation-delay:-2.1s}
.sb-mid-right .sb-ic{background:linear-gradient(135deg,#0C6B45,#12995f)}
"""

mobile_css_992 = """
  .sb-mid-left{top:45%;left:0}
  .sb-mid-right{bottom:45%;right:0}
"""

mobile_css_768 = """
  .sb-mid-left{top:45%;left:0}
  .sb-mid-right{bottom:45%;right:0}
"""

if '.sb-mid-left' not in css:
    # We will just append the base classes at the end of the .stat-badge section
    css = re.sub(r'(\.sb-bottom \.sb-ic\{[^}]*\})', r'\1' + new_css, css)
    
    # Add to 992px media query
    css = re.sub(r'(\.sb-bottom\{bottom:12%;left:0\})', r'\1' + mobile_css_992, css)

    # Add to 768px media query
    css = re.sub(r'(\.sb-bottom\{bottom:10%;left:0\})', r'\1' + mobile_css_768, css)
    
    # Add to scale rule
    css = re.sub(r'(\.sb-top,\.sb-bottom\{transform:scale\(\.92\)\})', r'.sb-top,.sb-bottom,.sb-mid-left,.sb-mid-right{transform:scale(.92)}', css)

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)


# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_badges = """
      <div class="stat-badge sb-mid-left">
        <div class="sb-ic">🏆</div>
        <div><div class="sb-n">500+</div><div class="sb-l">A / A+ Scorers</div></div>
      </div>
      <div class="stat-badge sb-mid-right">
        <div class="sb-ic">😊</div>
        <div><div class="sb-n">98%</div><div class="sb-l">Satisfaction Rate</div></div>
      </div>
"""

if 'sb-mid-left' not in html:
    target = r'(<div class="stat-badge sb-bottom">.*?</div>\s*</div>)'
    html = re.sub(target, r'<div class="stat-badge sb-bottom">\n        <div class="sb-ic">🎓</div>\n        <div><div class="sb-n">12,000+</div><div class="sb-l">Students Taught</div></div>\n      </div>' + new_badges, html, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Added 2 new badges successfully.")
