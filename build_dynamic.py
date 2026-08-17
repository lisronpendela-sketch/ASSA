import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add ID to news grid
html = re.sub(
    r'(<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); gap: 1\.5rem; align-items: start; perspective: 1500px;")>',
    r'\1 id="news-grid">',
    html
)

supabase_injection = """
<!-- ═══ DYNAMIC CMS INTEGRATION ═══ -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script type="module">
  const SUPABASE_URL = 'https://lugrvspmtugihwqmzgu.supabase.co';
  const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx1Z3J2c3BtdHVnaWh3cW1xemd1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODY1MjAyNDEsImV4cCI6MjEwMjA5NjI0MX0.LPnF1ctYJfUpo1RCHES5uKh8tPgUpBTCKvsdzjcoRxo';
  const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

  async function loadDynamicNews() {
    try {
      const { data, error } = await supabase
        .from('news')
        .select('*')
        .eq('status', 'PUBLISHED')
        .order('published_at', { ascending: false })
        .limit(3);

      if (error) throw error;
      
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
          
          // Construct HTML keeping exact design parameters
          const el = document.createElement('div');
          el.className = `course-card reveal door-anim ${delayClass}`;
          el.style.padding = '1rem';
          el.style.background = 'var(--white)';
          
          let contentHtml = '';
          if (item.image_url) {
             let imgUrl = item.image_url;
             // If they picked from library, it might just be the filename or public url
             if (!imgUrl.startsWith('http')) {
                imgUrl = supabase.storage.from('public_assets').getPublicUrl(item.image_url).data.publicUrl;
             }
             contentHtml += `<img src="${imgUrl}" alt="${item.title}" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">`;
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
</body>
"""

html = html.replace('</body>', supabase_injection)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Dynamic CMS integration injected into index.html")
