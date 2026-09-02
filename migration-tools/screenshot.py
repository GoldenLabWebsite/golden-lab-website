import sys
from playwright.sync_api import sync_playwright

url = sys.argv[1]
out = sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 900
height = int(sys.argv[4]) if len(sys.argv) > 4 else 1400

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page(viewport={"width": width, "height": height})
    page.goto(url, wait_until="networkidle")
    page.screenshot(path=out, full_page=True)
    browser.close()
print("saved", out)
