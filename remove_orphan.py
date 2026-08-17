import re

def remove_orphan_modal(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The orphan modal starts right after the correct one ends.
    # It starts with:
    #         <div class="pay-method"><div class="pay-logo pm-easy">Easy<br>paisa</div><div class="pay-info"><div class="pm-name">Easypaisa</div><div class="pm-num">0323-5792758</div>
    # And ends after:
    #     </div>
    #   </div>
    # </div>
    
    # We will use regex to find this specific chunk and remove it
    pattern = r'\s*<div class="pay-method"><div class="pay-logo pm-easy">Easy<br>paisa</div><div class="pay-info"><div class="pm-name">Easypaisa</div><div class="pm-num">0323-5792758</div>.*?</div>\s*</div>\s*</div>'
    
    html = re.sub(pattern, '', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

remove_orphan_modal('index.html')
remove_orphan_modal('classes.html')

print("Removed orphan modal code from both files.")
