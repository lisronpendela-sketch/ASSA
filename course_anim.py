import re

# 1. Update JS in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_js = """/* ── Course filter ── */
document.querySelectorAll('.filter-btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const f=btn.dataset.filter;
    document.querySelectorAll('.course-card').forEach(c=>{
      const show=f==='all'||c.dataset.class===f;
      c.style.display=show?'flex':'none';
    });
  });
});"""

new_js = """/* ── Course filter ── */
const grid = document.querySelector('.course-grid');
document.querySelectorAll('.filter-btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    if(btn.classList.contains('active')) return;
    document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const f=btn.dataset.filter;
    
    // Fade out
    grid.style.opacity = '0';
    grid.style.transform = 'translateY(5px)';
    
    setTimeout(() => {
      document.querySelectorAll('.course-card').forEach(c=>{
        const show=f==='all'||c.dataset.class===f;
        c.style.display=show?'flex':'none';
      });
      // Force reflow
      grid.offsetHeight;
      // Fade in
      grid.style.opacity = '1';
      grid.style.transform = 'translateY(0)';
    }, 200);
  });
});"""

if old_js in html:
    html = html.replace(old_js, new_js)
else:
    # fallback
    print("Warning: old_js not found perfectly, using regex")
    html = re.sub(
        r'/\* ── Course filter ── \*/.*?\}\);\s*\}\);\s*', 
        new_js + '\n', 
        html, 
        flags=re.DOTALL
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Filter btn active state
css = css.replace('.filter-btn{', '.filter-btn{transition: background .2s var(--ease), color .2s var(--ease), transform .1s; ')
if '.filter-btn:active' not in css:
    css += "\n.filter-btn:active{transform:scale(0.96)}\n"
    
# Grid transition
if '.course-grid { transition:' not in css and '.course-grid{transition:' not in css:
    css += "\n.course-grid{transition:opacity .2s var(--ease), transform .2s var(--ease)}\n"

# Course card hover
css = css.replace('transition:box-shadow .3s var(--ease);display:flex;flex-direction:column;', 'transition:translate .2s var(--ease), box-shadow .2s var(--ease);display:flex;flex-direction:column;')
if '.course-card:hover{translate' not in css:
    css += "\n.course-card:hover{translate:0 -5px;box-shadow:var(--sh-lg)}\n"

# btn-course transition and hover
css = css.replace('transition:.22s var(--ease);', 'transition:filter .2s var(--ease), box-shadow .2s var(--ease);')
css = css.replace('.btn-course:hover{transform:translateY(-2px);box-shadow:0 8px 18px rgba(140,31,40,.35)}', '.btn-course:hover{filter:brightness(1.1);box-shadow:0 8px 18px rgba(140,31,40,.35)}')

# Course card staggers (50ms)
staggers = "\n/* Course card staggers */\n"
for i in range(1, 21):
    staggers += f".course-card.reveal:nth-child({i}) {{ transition-delay: {i * 0.05}s !important; }}\n"

if '/* Course card staggers */' not in css:
    css += staggers

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Course packages animations updated.")
