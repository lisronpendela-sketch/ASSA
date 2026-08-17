import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_h1 = '<h1>Study Smart, Score <span class="gold">Higher</span><br>in Your <span class="accent">Board Exams</span></h1>'
new_h1 = '<h1><span class="hero-line">Study Smart, Score <span class="gold">Higher</span></span><br><span class="hero-line">in Your <span class="accent">Board Exams</span></span></h1>'

html = html.replace(target_h1, new_h1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove float animation from .stat-badge
css = re.sub(r'animation:float 5s ease-in-out infinite alternate;', '', css)

hero_animations = """
/* ═══ HERO ENTRANCE ANIMATION ═══ */
@keyframes hero-fade-up {
  0% { opacity: 0; transform: translateY(15px); }
  100% { opacity: 1; transform: translateY(0); }
}
@keyframes hero-line-up {
  0% { opacity: 0; transform: translateY(25px); }
  100% { opacity: 1; transform: translateY(0); }
}
@keyframes hero-badge-up {
  0% { opacity: 0; transform: translateY(8px); }
  100% { opacity: 1; transform: translateY(0); }
}
@keyframes hero-img-in {
  0% { opacity: 0; transform: scale(0.96); }
  100% { opacity: 1; transform: scale(1); }
}
@keyframes float-slow {
  0% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
  100% { transform: translateY(0); }
}

.hero-eyebrow { opacity: 0; animation: hero-fade-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.1s forwards; }

.hero-line { display: inline-block; opacity: 0; }
h1 > .hero-line:nth-of-type(1) { animation: hero-line-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.2s forwards; }
h1 > .hero-line:nth-of-type(2) { animation: hero-line-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.3s forwards; }

.hero-sub { opacity: 0; animation: hero-fade-up 0.35s cubic-bezier(0.4, 0, 0.2, 1) 1.4s forwards; }

.hero-check { opacity: 0; }
.hero-check:nth-child(1) { animation: hero-fade-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.45s forwards; }
.hero-check:nth-child(2) { animation: hero-fade-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.52s forwards; }
.hero-check:nth-child(3) { animation: hero-fade-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.59s forwards; }

.hero-cta > a { opacity: 0; animation: hero-fade-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.65s forwards; }

.hero-social-pop { opacity: 0; animation: hero-fade-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.75s forwards; }

.hero-circle { opacity: 0; animation: hero-img-in 0.7s cubic-bezier(0.4, 0, 0.2, 1) 1.2s forwards; }

.stat-badge { opacity: 0; animation: hero-badge-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.9s forwards; }

.hero-dots, .hero-blob { animation: float-slow 6s ease-in-out infinite; }

@media (prefers-reduced-motion: reduce) {
  .hero-eyebrow, .hero-line, .hero-sub, .hero-check, .hero-cta > a, .hero-social-pop, .hero-circle, .stat-badge, .hero-dots, .hero-blob {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
  }
}
"""

if 'hero-fade-up' not in css:
    css += hero_animations
    
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Hero animations added successfully.")
