import os
import shutil

# Move PDFs
pdf_files = [
    "Class 11 Computer Science Formative Book Akbar Study Smart Academy.pdf",
    "Class 11 Physics Formative Book Akbar Study Smart Academy.pdf",
    "Class 11 Tarjmatulquran Formative Book Akbar Study Smart Academy.pdf",
    "Class 9 Computer Science Formative Book Akbar Study Smart Academy.pdf",
    "Class 9 Physics Formative Book Akbar Study Smart Academy.pdf",
    "Class 9 Tarjmatulquran Formative Book Akbar Study Smart Academy.pdf"
]

target_dir = os.path.join(os.getcwd(), "uploads", "books")
os.makedirs(target_dir, exist_ok=True)

for pdf in pdf_files:
    if os.path.exists(pdf):
        try:
            shutil.move(pdf, os.path.join(target_dir, pdf))
            print(f"Moved {pdf} to uploads/books/")
        except Exception as e:
            print(f"Failed to move {pdf}: {e}")

# Inject HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

books_html = """
<!-- 📚 BOOKS -->
<section class="section" id="books" style="background: var(--white);">
  <div class="container">
    <div class="sec-head reveal fade-down">
      <span class="sec-tag">PUBLICATIONS</span>
      <h2>Our Premium <span class="gold">Books</span></h2>
      <p class="sec-desc">Exclusive Formative Books by Akbar Study Smart Academy. Prepared according to the NBF Textbook and Assessment Framework.</p>
    </div>
    <div class="class-grid" id="books-container">
      
      <!-- Book 1 -->
      <div class="course-card reveal" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Computer Science</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Computer Science</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Computer%20Science%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Book 2 -->
      <div class="course-card reveal d1" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Physics</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Physics</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Physics%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Book 3 -->
      <div class="course-card reveal d2" data-class="9">
        <div class="course-head ch-9"><span class="course-tag">CLASS 9</span><h3>Tarjuma Tul Quran</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 9</li>
            <li><strong>Subject:</strong> Tarjuma Tul Quran</li>
            <li><strong>Language:</strong> Urdu/Arabic</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%209%20Tarjuma%20Tul%20Quran%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Book 4 -->
      <div class="course-card reveal" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Computer Science</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Computer Science</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Computer%20Science%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Book 5 -->
      <div class="course-card reveal d1" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Physics</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Physics</li>
            <li><strong>Language:</strong> English</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Physics%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Book 6 -->
      <div class="course-card reveal d2" data-class="11">
        <div class="course-head ch-11"><span class="course-tag">CLASS 11</span><h3>Tarjuma Tul Quran</h3><p>Formative Book</p></div>
        <div class="course-body">
          <ul style="margin-bottom: 1.5rem;">
            <li><strong>Class:</strong> 11</li>
            <li><strong>Subject:</strong> Tarjuma Tul Quran</li>
            <li><strong>Language:</strong> Urdu/Arabic</li>
            <li><strong>Coverage:</strong> NBF Textbook & Assessments</li>
            <li><strong>Pages:</strong> Comprehensive Guide</li>
            <li><strong>Author:</strong> Akbar Study Smart Academy</li>
            <li><strong>Feedback:</strong> Highly Recommended</li>
          </ul>
          <div class="course-foot" style="align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1rem;">
            <div style="font-size:1.2rem; font-weight:bold; color:var(--maroon);">Rs. 499</div>
            <a href="https://wa.me/923235792758?text=Assalam-o-Alaikum!%20I%20want%20to%20order%20the%20Class%2011%20Tarjuma%20Tul%20Quran%20Formative%20Book." target="_blank" class="btn-course" style="text-decoration:none; text-align:center; padding: 0.6rem 1rem;">Order on WhatsApp</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

"""

# Find injection point
target = "<!-- " + chr(10024) + " NEWS & UPDATES " + chr(10024) + " -->"
fallback_target = "<!-- 📰 NEWS & UPDATES -->"
fallback_target_2 = "id=\"news\""

if target in html:
    html = html.replace(target, books_html + "\n" + target)
    print("Injected successfully using primary target.")
elif fallback_target in html:
    html = html.replace(fallback_target, books_html + "\n" + fallback_target)
    print("Injected successfully using fallback target.")
else:
    # Look for <section ... id="news" ...>
    idx = html.find('id="news"')
    if idx != -1:
        # back up to <section
        sec_idx = html.rfind('<section', 0, idx)
        if sec_idx != -1:
            html = html[:sec_idx] + books_html + "\n" + html[sec_idx:]
            print("Injected successfully using DOM search.")
        else:
            print("Failed to find insertion point.")
    else:
        print("Failed to find insertion point.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
