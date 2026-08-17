import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the old continuous waRing animation
css = re.sub(r'\.wa-float::after\s*\{[^}]*\}', '', css)
css = re.sub(r'@keyframes waRing\s*\{.*?100%\s*\{[^}]*\}\s*\}', '', css, flags=re.DOTALL)

# Add transition to max-width and transform
css = css.replace('transition:translate .25s var(--ease), box-shadow .25s var(--ease), border-color .25s var(--ease);', 'transition:max-width .3s var(--ease), padding-right .3s var(--ease), gap .3s var(--ease), transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s var(--ease);')

# Change wa-float hover
old_hover = '.wa-float:hover{max-width:260px;padding-right:22px;gap:11px}'
new_hover = '.wa-float:hover{max-width:260px;padding-right:22px;gap:11px;transform:scale(1.08) !important;animation:none !important}'
css = css.replace(old_hover, new_hover)

# Add waPulse and active state
wa_append = """
@keyframes waPulse {
  0%, 92% { transform: scale(1); }
  96% { transform: scale(1.04); }
  100% { transform: scale(1); }
}
.wa-float {
  animation: waPulse 4.5s ease-in-out infinite;
  transform-origin: center;
}
.wa-float:active {
  transform: scale(0.96) !important;
  animation: none !important;
}
@media (prefers-reduced-motion: reduce) {
  .wa-float {
    animation: none !important;
  }
}
"""

if 'waPulse' not in css:
    css += wa_append

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("WhatsApp float animations updated.")
