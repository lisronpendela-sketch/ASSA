import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

yt_grid_new = """    <div class="yt-grid">
      <a class="yt-card reveal" href="https://www.youtube.com/playlist?list=PLRFjILhvIduHYdP2rctOh_htfgzF5D2qb" target="_blank" rel="noopener">
        <div class="yt-thumb">
          <img src="yt-9.jpg" alt="Class 9 Important Topics" style="position:absolute; width:100%; height:100%; object-fit:cover; top:0; left:0; z-index:0;">
          <div class="yt-play" style="z-index: 2;"></div>
        </div>
        <div class="yt-body"><h3>Class 9 All Subjects Important Topics</h3><div class="meta">▶ Watch Playlist on YouTube</div></div>
      </a>
      <a class="yt-card reveal d1" href="https://www.youtube.com/playlist?list=PLRFjILhvIduGT0S4no0v0D7XRTSpv5E8n" target="_blank" rel="noopener">
        <div class="yt-thumb">
          <img src="yt-10.jpg" alt="Class 10 Important Topics" style="position:absolute; width:100%; height:100%; object-fit:cover; top:0; left:0; z-index:0;">
          <div class="yt-play" style="z-index: 2;"></div>
        </div>
        <div class="yt-body"><h3>Class 10 All Subjects Important Topics</h3><div class="meta">▶ Watch Playlist on YouTube</div></div>
      </a>
      <a class="yt-card reveal d2" href="https://www.youtube.com/playlist?list=PLRFjILhvIduEbgi01_Pj8qCXzzmuprOlB" target="_blank" rel="noopener">
        <div class="yt-thumb">
          <img src="yt-12.jpg" alt="12 Physics 2026_2027" style="position:absolute; width:100%; height:100%; object-fit:cover; top:0; left:0; z-index:0;">
          <div class="yt-play" style="z-index: 2;"></div>
        </div>
        <div class="yt-body"><h3>12 Physics 2026_2027</h3><div class="meta">▶ Watch Playlist on YouTube</div></div>
      </a>
    </div>"""

# Replace the old yt-grid
html = re.sub(r'<div class="yt-grid">.*?</div>\s*<div style="text-align:center"', yt_grid_new + '\n\n    <div style="text-align:center"', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated YouTube thumbnails in index.html")
