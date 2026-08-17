import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
if '.ch-skills' not in css:
    css += "\n.ch-skills{background:linear-gradient(135deg,#5A2C8A,#7B3EBA)}\n"
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

def get_nav_desktop_inject(base_url):
    return f"""
        <a href="{base_url}"><span class="cls" style="font-size:0.5rem">SKL</span> Graphic Designing</a>
        <a href="{base_url}"><span class="cls" style="font-size:0.5rem">SKL</span> Basic IT</a>
        <a href="{base_url}"><span class="cls" style="font-size:0.5rem">SKL</span> Web Development</a>
        <a href="{base_url}"><span class="cls" style="font-size:0.5rem">SKL</span> Digital Marketing</a>
        <a href="{base_url}"><span class="cls" style="font-size:0.5rem">SKL</span> Artificial Intelligence</a>
        <a href="{base_url}"><span class="cls" style="font-size:0.5rem">SKL</span> Spoken English</a>
"""

def get_nav_mobile_inject(base_url):
    return f"""
  <a href="{base_url}">Graphic Designing</a>
  <a href="{base_url}">Basic IT</a>
  <a href="{base_url}">Web Development</a>
  <a href="{base_url}">Digital Marketing</a>
  <a href="{base_url}">Artificial Intelligence</a>
  <a href="{base_url}">Spoken English</a>
"""

courses_grid_inject = """
      <div class="course-card reveal" data-class="skills">
        <div class="course-head ch-skills"><span class="course-tag">SKILL</span><h3>Graphic Designing</h3><p>Master visual communication</p></div>
        <div class="course-body">
          <ul><li>Adobe Photoshop & Illustrator</li><li>Logo & Branding Design</li><li>Social Media Posts</li><li>Freelancing guidance</li></ul>
          <div class="course-foot"><button class="btn-course" onclick="openEnroll('Graphic Designing', '')">Enroll Now</button></div>
        </div>
      </div>
      
      <div class="course-card reveal d1" data-class="skills">
        <div class="course-head ch-skills"><span class="course-tag">SKILL</span><h3>Basic IT</h3><p>Computer fundamentals</p></div>
        <div class="course-body">
          <ul><li>MS Office (Word, Excel, PPT)</li><li>Internet & Emailing</li><li>Basic Troubleshooting</li><li>Typing & Shortcuts</li></ul>
          <div class="course-foot"><button class="btn-course" onclick="openEnroll('Basic IT', '')">Enroll Now</button></div>
        </div>
      </div>

      <div class="course-card reveal d2" data-class="skills">
        <div class="course-head ch-skills"><span class="course-tag">SKILL</span><h3>Web Development</h3><p>Build modern websites</p></div>
        <div class="course-body">
          <ul><li>HTML, CSS & JavaScript</li><li>Responsive UI Design</li><li>Frontend Frameworks</li><li>Hosting & Deployment</li></ul>
          <div class="course-foot"><button class="btn-course" onclick="openEnroll('Web Development', '')">Enroll Now</button></div>
        </div>
      </div>

      <div class="course-card reveal" data-class="skills">
        <div class="course-head ch-skills"><span class="course-tag">SKILL</span><h3>Digital Marketing</h3><p>Grow online businesses</p></div>
        <div class="course-body">
          <ul><li>Social Media Management</li><li>Facebook & Google Ads</li><li>SEO Fundamentals</li><li>Content Strategy</li></ul>
          <div class="course-foot"><button class="btn-course" onclick="openEnroll('Digital Marketing', '')">Enroll Now</button></div>
        </div>
      </div>

      <div class="course-card reveal d1" data-class="skills">
        <div class="course-head ch-skills"><span class="course-tag">SKILL</span><h3>Artificial Intelligence</h3><p>Future-proof your career</p></div>
        <div class="course-body">
          <ul><li>AI Tools (ChatGPT, Midjourney)</li><li>Prompt Engineering</li><li>Workflow Automation</li><li>Basic AI Concepts</li></ul>
          <div class="course-foot"><button class="btn-course" onclick="openEnroll('Artificial Intelligence', '')">Enroll Now</button></div>
        </div>
      </div>

      <div class="course-card reveal d2" data-class="skills">
        <div class="course-head ch-skills"><span class="course-tag">SKILL</span><h3>Spoken English</h3><p>Communicate with confidence</p></div>
        <div class="course-body">
          <ul><li>Fluency & Pronunciation</li><li>Everyday Conversations</li><li>Interview Preparation</li><li>Vocabulary Building</li></ul>
          <div class="course-foot"><button class="btn-course" onclick="openEnroll('Spoken English', '')">Enroll Now</button></div>
        </div>
      </div>
"""

def update_file(filepath, base_url):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Avoid duplicate injection
    if 'Graphic Designing' in html and 'Artificial Intelligence' in html:
        print(f"Skipping {filepath}, courses already seem to exist.")
        return

    # Desktop nav
    target_desktop = r'(<a href="#courses"><span class="cls">12</span> Class 12 — Second Year</a>\s*</div>)'
    html = re.sub(target_desktop, r'<a href="#courses"><span class="cls">12</span> Class 12 — Second Year</a>\n' + get_nav_desktop_inject(base_url) + r'      </div>', html)

    # Mobile nav
    target_mobile = r'(<a href="#courses">Class 12 — Second Year</a>)'
    html = re.sub(target_mobile, r'<a href="#courses">Class 12 — Second Year</a>\n' + get_nav_mobile_inject(base_url).rstrip(), html)

    if filepath == 'index.html':
        # Filter button
        target_filter = r'(<button class="filter-btn" data-filter="12">Class 12</button>)'
        html = re.sub(target_filter, r'<button class="filter-btn" data-filter="12">Class 12</button>\n      <button class="filter-btn" data-filter="skills">Skill Courses</button>', html)
        
        # Course grid
        target_grid = r'(onclick="openEnroll\(\'Intermediate Crash Revision \(Class 11 &amp; 12\)\',\'Rs. 6,000 one-time\'\)">Enroll Now</button></div>\s*</div>\s*</div>)'
        
        html = re.sub(target_grid, r'\1\n' + courses_grid_inject, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_file('index.html', '#courses')
update_file('classes.html', 'index.html#courses')

print("Added courses successfully.")
