from pathlib import Path
import re
root=Path('.')
index=root/'index.html'; css=root/'style.css'; sw=root/'sw.js'
if not index.exists() or not css.exists() or not sw.exists():
    raise SystemExit('Kör filen i appmappen där index.html, style.css och sw.js finns.')
text=index.read_text(encoding='utf-8')
text=re.sub(r'<title>.*?</title>','<title>Jaktlaget 1.8.0</title>',text)
if 'v180.css' not in text:text=text.replace('</head>','<link rel="stylesheet" href="v180.css"></head>')
if 'v180.js' not in text:text=text.replace('</body>','<script src="v180.js"></script></body>')
index.write_text(text,encoding='utf-8')
s=sw.read_text(encoding='utf-8')
s=re.sub(r"const C='[^']+'", "const C='jaktlaget-v180-20261013'", s)
s=s.replace("'./manifest.webmanifest'", "'./manifest.webmanifest','./v180.css','./v180.js'")
sw.write_text(s,encoding='utf-8')
print('Jaktlaget v1.8.0 installerad.')
