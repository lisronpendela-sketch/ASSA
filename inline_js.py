import re

with open('admin/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the import line
js = re.sub(r"import \{ SUPABASE_URL, SUPABASE_ANON_KEY \} from '\./supabase-config\.js';", "", js)

# Inject the variables directly
vars_code = """
const SUPABASE_URL = 'https://lugrvspmtugihwqmzgu.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx1Z3J2c3BtdHVnaWh3cW1xemd1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODY1MjAyNDEsImV4cCI6MjEwMjA5NjI0MX0.LPnF1ctYJfUpo1RCHES5uKh8tPgUpBTCKvsdzjcoRxo';
"""

js = vars_code + js

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<script type="module" src="app.js"></script>', '<script>\n' + js + '\n</script>')

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
