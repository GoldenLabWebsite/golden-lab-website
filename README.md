# Golden Lab Website

Source for goldenneurolab.com, rebuilt as a static site so content updates are
plain-text edits + a build + a git push, instead of clicking through the
Squarespace editor.

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

Real staff/member photos still need to be added to `site/static/images/` and
referenced by filename in `people.yaml` (the `photo:` field). Every entry
currently points at a placeholder silhouette.

## Deployment (one-time setup, not yet done)

This repository is not yet connected to a live host. See the migration notes
from Claude for the recommended next steps (GitHub Pages or Netlify, plus
repointing the goldenneurolab.com domain at GoDaddy).
