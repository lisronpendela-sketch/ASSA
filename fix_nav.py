def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    if filename == 'index.html':
        bad_str = '<li><a href="#news">News</a>\n  <a href="#tests">Tests</a>\n  <a href="#about">About</a></li>'
        html = html.replace(bad_str, '<li><a href="#about">About</a></li>')
    else:
        bad_str = '<li><a href="index.html#news">News</a>\n  <a href="index.html#tests">Tests</a>\n  <a href="index.html#about">About</a></li>'
        html = html.replace(bad_str, '<li><a href="index.html#about">About</a></li>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_file('index.html')
fix_file('classes.html')
print("Fixed duplicate links")
