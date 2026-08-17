import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<option value="news">News & Update</option>',
    '<option value="news">News & Update</option>\n                            <option value="classes">Classes</option>\n                            <option value="achievements">Achievements</option>\n                            <option value="tests">Tests</option>\n                            <option value="about">About</option>\n                            <option value="contact">Contact</option>'
)

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
