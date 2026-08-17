import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The pattern replaces everything from <!-- ═══ HERO ═══ --> to <!-- ═══ FOOTER ═══ -->
pattern = re.compile(r'<!-- ═══ HERO ═══ -->.*?<!-- ═══ FOOTER ═══ -->', re.DOTALL)

classes_section = """<!-- ═══ CLASSES HERO ═══ -->
<section class="hero" style="min-height: 40vh; display: flex; align-items: center; justify-content: center; text-align: center;">
  <div class="container reveal">
    <span class="hero-eyebrow">Academic Programs</span>
    <h1>Classes from <span class="gold">PG</span> to <span class="accent">University</span></h1>
    <p class="hero-sub" style="margin: 0 auto;">Explore our comprehensive range of classes designed to guide students through every stage of their academic journey.</p>
  </div>
</section>

<!-- ═══ ALL CLASSES ═══ -->
<section class="section courses" id="classes">
  <div class="container">
    <div class="course-grid">
      <!-- PG -->
      <div class="course-card reveal">
        <div class="course-head ch-9"><span class="course-tag">EARLY YEARS</span><h3>PlayGroup (PG)</h3><p>A fun start to learning</p></div>
        <div class="course-body">
          <ul><li>Interactive activities</li><li>Basic alphabet & numbers</li><li>Social skills development</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 1,500<small>/ month</small></div><button class="btn-course" onclick="openEnroll('PlayGroup (PG)','Rs. 1,500 / month')">Enroll Now</button></div>
        </div>
      </div>
      <!-- Nursery -->
      <div class="course-card reveal d1">
        <div class="course-head ch-10"><span class="course-tag">EARLY YEARS</span><h3>Nursery</h3><p>Building the foundation</p></div>
        <div class="course-body">
          <ul><li>Reading and writing basics</li><li>Creative arts and crafts</li><li>Early math concepts</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 1,800<small>/ month</small></div><button class="btn-course" onclick="openEnroll('Nursery','Rs. 1,800 / month')">Enroll Now</button></div>
        </div>
      </div>
      <!-- Prep -->
      <div class="course-card reveal d2">
        <div class="course-head ch-11"><span class="course-tag">EARLY YEARS</span><h3>Prep</h3><p>Getting ready for school</p></div>
        <div class="course-body">
          <ul><li>Advanced phonics</li><li>Basic arithmetic</li><li>Environmental awareness</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 2,000<small>/ month</small></div><button class="btn-course" onclick="openEnroll('Prep','Rs. 2,000 / month')">Enroll Now</button></div>
        </div>
      </div>
      <!-- Primary & Middle -->
      <div class="course-card reveal">
        <div class="course-head ch-12"><span class="course-tag">CLASS 1 TO 8</span><h3>Primary & Middle</h3><p>Core academic growth</p></div>
        <div class="course-body">
          <ul><li>Comprehensive subject coverage</li><li>Regular assessments</li><li>Concept-first approach</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 2,500<small>/ month</small></div><button class="btn-course" onclick="openEnroll('Primary & Middle (Class 1-8)','Rs. 2,500 / month')">Enroll Now</button></div>
        </div>
      </div>
      <!-- Matric -->
      <div class="course-card reveal d1">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9 & 10</span><h3>Matriculation</h3><p>Board exam excellence</p></div>
        <div class="course-body">
          <ul><li>FBISE aligned notes</li><li>Past papers & revision</li><li>Weekly test sessions</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 3,000<small>/ month</small></div><button class="btn-course" onclick="openEnroll('Matriculation (Class 9-10)','Rs. 3,000 / month')">Enroll Now</button></div>
        </div>
      </div>
      <!-- Inter -->
      <div class="course-card reveal d2">
        <div class="course-head ch-10"><span class="course-tag">CLASS 11 & 12</span><h3>Intermediate</h3><p>Pre-Med / Pre-Eng</p></div>
        <div class="course-body">
          <ul><li>In-depth science lectures</li><li>Entry-test preparation</li><li>Mock board exams</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 4,000<small>/ month</small></div><button class="btn-course" onclick="openEnroll('Intermediate (Class 11-12)','Rs. 4,000 / month')">Enroll Now</button></div>
        </div>
      </div>
      <!-- University -->
      <div class="course-card reveal">
        <div class="course-head ch-11"><span class="course-tag">HIGHER ED</span><h3>University Preparation</h3><p>Guidance for higher studies</p></div>
        <div class="course-body">
          <ul><li>University entry tests</li><li>Career counseling</li><li>Advanced concept mastery</li></ul>
          <div class="course-foot"><div class="course-price">Rs. 5,000<small>/ month</small></div><button class="btn-course" onclick="openEnroll('University Preparation','Rs. 5,000 / month')">Enroll Now</button></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ FINAL CTA ═══ -->
<section class="section cta-band">
  <div class="container reveal">
    <h2>Ready to <span class="gold">enroll</span> in your class?</h2>
    <p>Join Akbar Study Smart Academy today. Contact us on WhatsApp to begin your journey.</p>
    <div class="hero-cta">
      <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20enroll." target="_blank" rel="noopener" class="btn btn-wa">💬 Enroll on WhatsApp</a>
    </div>
  </div>
</section>

<!-- ═══ FOOTER ═══ -->
"""

new_html = pattern.sub(classes_section, html)

# Fix links in the nav so they point back to index.html where necessary
new_html = new_html.replace('href="#home"', 'href="index.html#home"')
new_html = new_html.replace('href="#achievements"', 'href="index.html#achievements"')
new_html = new_html.replace('href="#lectures"', 'href="index.html#lectures"')
new_html = new_html.replace('href="#about"', 'href="index.html#about"')

# Ensure the new dropdown links in classes.html point to #classes instead of index.html
# We can leave them as #classes as they exist on this page.

with open('classes.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("classes.html generated successfully!")
