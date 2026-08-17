import re

news_section = """
<!-- ═══ NEWS & UPDATES ═══ -->
<section class="section" id="news" style="background: var(--ivory);">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">What's New</span>
      <h2 class="sec-title">News & <span class="gold">Updates</span></h2>
      <p class="sec-desc">Stay informed with the latest announcements from Akbar Study Smart Academy and FBISE.</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
      <div class="course-card reveal" style="padding: 1rem; background: var(--white);">
        <img src="news-1.jpg" alt="ASSA Flyer" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="course-card reveal d1" style="padding: 1rem; background: var(--white);">
        <img src="news-2.jpg" alt="FBISE Important Announcement" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
      <div class="course-card reveal d2" style="padding: 1rem; background: var(--white);">
        <img src="news-3.jpg" alt="FBISE E-Kachehri" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
      </div>
    </div>
  </div>
</section>
"""

tests_section = """
<!-- ═══ TESTS ═══ -->
<section class="section" id="tests">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Assessments</span>
      <h2 class="sec-title">Free Chapter <span class="maroon">Tests</span></h2>
      <p class="sec-desc">Test your knowledge with our SLOs based assessments aligned with the NBF Textbook.</p>
    </div>
    <div style="background: var(--white); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 2.5rem 1.5rem; max-width: 700px; margin: 0 auto; box-shadow: var(--sh-md); text-align: center;" class="reveal">
      <h3 style="font-size: 1.3rem; font-weight: 700; color: var(--navy); margin-bottom: 1rem; line-height: 1.4;">Physics Chapter 1 Test | Class 9th & 10th | Session 2026–27, 2nd Annual 2026 | ASSA</h3>
      <p style="color: var(--muted); margin-bottom: 0.5rem; font-size: 0.95rem;">Acc to Assessment Framework, SLOs Based, And NBF Textbook</p>
      <p style="font-family: var(--f-mono); font-weight: 600; color: var(--gold-dark); margin-bottom: 2rem; font-size: 1.1rem;">Total Marks: 35</p>
      <a href="https://drive.google.com/drive/folders/1hz064U38JO5iGDNxtRwxaPeDwecH_cbm" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-flex; justify-content: center; width: 100%; max-width: 320px;">📥 Download Your Chapter 1 Test</a>
    </div>
  </div>
</section>
"""

def update_html(filepath, is_index):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Insert nav links
    # find: <li><a href="#about">About</a></li> or <li><a href="index.html#about">About</a></li>
    if is_index:
        nav_insert = '<li><a href="#news">News</a></li>\n    <li><a href="#tests">Tests</a></li>\n    <li><a href="#about">About</a></li>'
        html = re.sub(r'<li><a href="#about">About</a></li>', nav_insert, html)
        
        m_nav_insert = '<a href="#news">News</a>\n  <a href="#tests">Tests</a>\n  <a href="#about">About</a>'
        html = re.sub(r'<a href="#about">About</a>', m_nav_insert, html)
        
        # Insert sections in index.html right before ABOUT
        # <!-- ═══ ABOUT ═══ -->
        sections = f"{news_section}\n{tests_section}\n<!-- ═══ ABOUT ═══ -->"
        html = html.replace("<!-- ═══ ABOUT ═══ -->", sections)
    else:
        nav_insert = '<li><a href="index.html#news">News</a></li>\n    <li><a href="index.html#tests">Tests</a></li>\n    <li><a href="index.html#about">About</a></li>'
        html = re.sub(r'<li><a href="index.html#about">About</a></li>', nav_insert, html)
        
        m_nav_insert = '<a href="index.html#news">News</a>\n  <a href="index.html#tests">Tests</a>\n  <a href="index.html#about">About</a>'
        html = re.sub(r'<a href="index.html#about">About</a>', m_nav_insert, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_html('index.html', True)
update_html('classes.html', False)

# Update style.css nav padding to push logo and button further out
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Original padding: padding:0 clamp(1rem,4vw,3rem);
css = css.replace('padding:0 clamp(1rem,4vw,3rem);', 'padding:0 clamp(0.5rem, 2vw, 1.5rem);')

# Make sure it didn't miss it
if 'padding:0 clamp(1rem,4vw,3rem)' not in css and 'padding:0 clamp(0.5rem, 2vw, 1.5rem)' not in css:
    # try another regex
    css = re.sub(r'padding:0 clamp\([^)]+\);', 'padding:0 clamp(0.5rem, 2vw, 1.5rem);', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added sections and updated nav padding.")
