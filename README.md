# Golden Lab Website

Source for goldenneurolab.com, rebuilt as a static site so content updates are
plain-text edits + a build + a git push, instead of clicking through the
Squarespace editor. The design (black background, red/white Montserrat +
Lato type, photo-forward people page, full-abstract publications list) was
copied from the live Squarespace site, including the real logo and staff
photos.

## How it's organized

```
site/
  content/          <- EDIT THESE to change what's on the site
    site.yaml        (lab name, mission, nav, contact info, research blurbs)
    people.yaml       (current members + alumni)
    publications.yaml (every paper, one entry each)
    news.yaml          (news/announcements)
    pages.yaml          (SimBA / ArgiNLS / Join text)
  templates/         <- Jinja2 HTML templates (page layout/design)
  static/            <- CSS + images
  build.py           <- regenerates the site from content/ + templates/
docs/                <- the generated, ready-to-publish site (do not hand-edit)
```

## Making an update

1. Edit the relevant file in `site/content/`.
   - New publication → add an entry to `publications.yaml`.
   - New/departing lab member → edit `people.yaml`.
   - New announcement → add an entry to the top of `news.yaml`.
2. Rebuild:
   ```
   cd site
   python3 build.py
   ```
3. Preview `docs/*.html` in a browser.
4. Commit and push:
   ```
   git add -A
   git commit -m "Update: <what changed>"
   git push
   ```
   If the repo is connected to GitHub Pages or Netlify, the live site updates
   automatically within a minute or two of the push.

## Photos

Real staff/member photos are already in `site/static/images/people/` (pulled
from the live site) and referenced by filename in `people.yaml` (the
`photo:` field). To add a new person, drop their photo in that folder and
point `photo:` at it.

## Migration tools

`migration-tools/` holds the one-off scripts used to pull content and images
off the old Squarespace site (`gen_publications.py`, `decode_images.py`,
`screenshot.py`). They're not needed for day-to-day updates — kept only in
case a future re-scrape is useful.

## Deployment (live)

- **GitHub repo:** https://github.com/GoldenLabWebsite/golden-lab-website
- **Live URL (GitHub Pages):** https://goldenlabwebsite.github.io/golden-lab-website/
- Pages is configured to serve from `main` branch, `/docs` folder. Any push
  to `main` that updates `docs/` goes live within about a minute.

**Not yet done:** pointing goldenneurolab.com itself at this site. That
requires a DNS change at GoDaddy (adding GitHub's A records + a CNAME file)
and should happen only once you're happy with the content — Squarespace can
stay live as a fallback until then.
