import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace the script logic at the bottom of the page
script_regex = r'<!-- ═══ DYNAMIC CMS INTEGRATION ═══ -->.*?</body>'

new_script = """<!-- ═══ DYNAMIC CMS INTEGRATION ═══ -->
<script>
  // Helper to trigger reveal animations for newly added elements
  function triggerAnimations(elements) {
    const localObs = new IntersectionObserver(es => {
      es.forEach(e => {
        if(e.isIntersecting) { e.target.classList.add('in'); }
        else { e.target.classList.remove('in'); }
      });
    }, {threshold: .05, rootMargin: '0px 0px -20px 0px'});
    elements.forEach(el => localObs.observe(el));
  }

  // Load News
  async function loadDynamicNews() {
    try {
      const res = await fetch('/api/content/news');
      if (!res.ok) return;
      const data = await res.json();
      
      if (data && data.length > 0) {
        const grid = document.getElementById('news-grid');
        if (!grid) return;
        
        grid.innerHTML = ''; 
        let newElements = [];
        data.forEach((item, index) => {
          let delayClass = index === 1 ? 'd1' : (index === 2 ? 'd2' : '');
          const el = document.createElement('div');
          el.className = `course-card reveal door-anim ${delayClass}`;
          el.style.padding = '1rem';
          el.style.background = 'var(--white)';
          
          let contentHtml = '';
          if (item.file_url) contentHtml += `<img src="${item.file_url}" alt="${item.title}" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">`;
          contentHtml += `<h3 style="margin-top:1rem;font-size:1.1rem;font-weight:700;">${item.title}</h3>`;
          if (item.description) contentHtml += `<p style="font-size:0.9rem;color:var(--text);margin-top:0.5rem;">${item.description}</p>`;
          
          el.innerHTML = contentHtml;
          grid.appendChild(el);
          newElements.push(el);
        });
        triggerAnimations(newElements);
      }
    } catch(err) { console.warn("Failed to load news", err); }
  }

  // Load Courses
  async function loadDynamicCourses() {
    try {
      const res = await fetch('/api/content/courses');
      if (!res.ok) return;
      const data = await res.json();
      
      if (data && data.length > 0) {
        // Find the course grid. We need to add an id to it if it doesn't exist.
        // Wait, the course grid has class "course-grid".
        const grid = document.querySelector('.course-grid');
        if (!grid) return;
        
        // Append newly added custom courses to the top of the grid
        let newElements = [];
        
        data.reverse().forEach((item, index) => {
          const el = document.createElement('div');
          // For simplicity, we just categorize them as 'foundation' or let them show in all
          el.className = `course-card reveal slide-anim`;
          el.dataset.class = 'custom'; 
          
          let contentHtml = '';
          if (item.file_url) contentHtml += `<img src="${item.file_url}" alt="${item.title}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px 8px 0 0;">`;
          contentHtml += `<div class="cc-content">
                            <h3 class="cc-title">${item.title}</h3>
                            <p class="cc-desc">${item.description || 'Custom added course'}</p>
                            <button class="btn btn-outline" style="width:100%; margin-top:1rem;" onclick="openEnroll('${item.title}')">Enroll Now</button>
                          </div>`;
          
          el.innerHTML = contentHtml;
          grid.prepend(el);
          newElements.push(el);
        });
        triggerAnimations(newElements);
      }
    } catch(err) { console.warn("Failed to load courses", err); }
  }

  // Execute all loaders
  loadDynamicNews();
  loadDynamicCourses();

</script>
</body>"""

html = re.sub(script_regex, new_script, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
