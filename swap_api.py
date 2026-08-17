import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the supabase injection block with the custom node api injection block
supabase_regex = r'<!-- ═══ DYNAMIC CMS INTEGRATION ═══ -->.*?</body>'

custom_api_injection = """<!-- ═══ DYNAMIC CMS INTEGRATION ═══ -->
<script>
  async function loadDynamicNews() {
    try {
      // Fetch from our local custom Node.js server
      const res = await fetch('/api/news');
      if (!res.ok) throw new Error('Server not responding');
      
      const data = await res.json();
      
      if (data && data.length > 0) {
        const grid = document.getElementById('news-grid');
        if (!grid) return;
        
        grid.innerHTML = ''; // clear hardcoded items
        
        const localObs = new IntersectionObserver(es => {
          es.forEach(e => {
            if(e.isIntersecting) { e.target.classList.add('in'); }
            else { e.target.classList.remove('in'); }
          });
        }, {threshold: .05, rootMargin: '0px 0px -20px 0px'});

        data.forEach((item, index) => {
          let delayClass = index === 1 ? 'd1' : (index === 2 ? 'd2' : '');
          
          const el = document.createElement('div');
          el.className = `course-card reveal door-anim ${delayClass}`;
          el.style.padding = '1rem';
          el.style.background = 'var(--white)';
          
          let contentHtml = '';
          if (item.image_url) {
             contentHtml += `<img src="${item.image_url}" alt="${item.title}" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">`;
          }
          
          contentHtml += `<h3 style="margin-top:1rem;font-size:1.1rem;font-weight:700;">${item.title}</h3>`;
          if (item.short_description) {
             contentHtml += `<p style="font-size:0.9rem;color:var(--text);margin-top:0.5rem;">${item.short_description}</p>`;
          }
          
          el.innerHTML = contentHtml;
          grid.appendChild(el);
          localObs.observe(el);
        });
      }
    } catch(err) {
      console.warn("Failed to load dynamic news, falling back to static.", err);
    }
  }
  
  loadDynamicNews();
</script>
</body>"""

html = re.sub(supabase_regex, custom_api_injection, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
