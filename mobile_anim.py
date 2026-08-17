import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update reveal observer to replay animations (permanent when scrolling up/down)
old_obs = "const revObs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');revObs.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -50px 0px'});"
new_obs = "const revObs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');}else{e.target.classList.remove('in');}});},{threshold:.05,rootMargin:'0px 0px -20px 0px'});"

if old_obs in html:
    html = html.replace(old_obs, new_obs)
else:
    print("Warning: could not perfectly match reveal observer JS")
    # regex fallback
    html = re.sub(r'const revObs=new IntersectionObserver\(es=>\{es\.forEach\(e=>\{if\(e\.isIntersecting\)\{e\.target\.classList\.add\(\'in\'\);revObs\.unobserve\(e\.target\);\}\}\);\},\{threshold:.12,rootMargin:\'0px 0px -50px 0px\'\}\);', new_obs, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Intersection observer updated for mobile and permanent animations.")
