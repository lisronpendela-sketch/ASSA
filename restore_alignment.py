import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Revert EVERYTHING back to center
css = css.replace('justify-content:space-between;', 'justify-content:center;')

# 2. Selectively apply space-between to the layout containers that actually need it
def set_space_between(classname):
    global css
    # Find the block for the classname
    # using regex to find classname{ ... justify-content:center; ... }
    pattern = r'(\.' + classname + r'\{[^}]*)justify-content:center;'
    css = re.sub(pattern, r'\1justify-content:space-between;', css)

classes_to_fix = [
    'topbar',
    'nav',
    'class-cta',
    'course-foot',
    'footer-bottom',
    'modal-course'
]

for cls in classes_to_fix:
    set_space_between(cls)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored original alignment for all elements")
