import re, base64, os, sys

path = sys.argv[1]
outdir = sys.argv[2] if len(sys.argv) > 2 else "site/static/images/people"

with open(path) as f:
    raw = f.read()

pattern = re.compile(r'\\*"([a-zA-Z_0-9]+)\\*"\s*:\s*\\*"([A-Za-z0-9+/=]{100,})\\*"')
matches = pattern.findall(raw)
print(f"Found {len(matches)} matches in {path}")
os.makedirs(outdir, exist_ok=True)
for name, b64 in matches:
    try:
        rawbytes = base64.b64decode(b64)
    except Exception as e:
        print(name, "decode error", e)
        continue
    ext = 'jpg'
    if rawbytes[:4] == b'RIFF':
        ext = 'webp'
    elif rawbytes[:8] == b'\x89PNG\r\n\x1a\n':
        ext = 'png'
    elif rawbytes[:3] == b'\xff\xd8\xff':
        ext = 'jpg'
    fn = os.path.join(outdir, f"{name}.{ext}")
    with open(fn, 'wb') as out:
        out.write(rawbytes)
    print(name, ext, len(rawbytes), "->", fn)
