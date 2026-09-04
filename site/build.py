#!/usr/bin/env python3
"""Static site builder for the Golden Lab website.

Usage: python3 build.py

Reads structured content from content/*.yaml, renders it through the Jinja2
templates in templates/, and writes the finished HTML into ../docs (the
GitHub Pages publish directory). Run this after editing any content file.
"""
import shutil
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT.parent / "docs"


def load_yaml(name):
    with open(CONTENT / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    site = load_yaml("site.yaml")
    people = load_yaml("people.yaml")
    pubs_raw = load_yaml("publications.yaml")["publications"]
    news_raw = load_yaml("news.yaml")["news"]
    pages = load_yaml("pages.yaml")

    # Number publications 1..N with #1 = most recent (matches the original site).
    total = len(pubs_raw)
    for i, p in enumerate(pubs_raw):
        p["num"] = total - i
        # Stable per-entry anchor for deep-linking (e.g. from the cover gallery).
        if p.get("pdf"):
            p["anchor"] = "pub-" + p["pdf"].rsplit("/", 1)[-1].rsplit(".", 1)[0]
        else:
            p["anchor"] = f"pub-{p['num']}"

    years = sorted({p["year"] for p in pubs_raw}, reverse=True)
    publications_by_year = [(y, [p for p in pubs_raw if p["year"] == y]) for y in years]

    for n in news_raw:
        n["date_display"] = datetime.strptime(n["date"], "%Y-%m-%d").strftime("%B %-d, %Y")

    # Build-time timestamp shown in the footer of every page (date only, no time of day).
    build_date = datetime.now().strftime("%m/%d/%Y")

    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=True, trim_blocks=True, lstrip_blocks=True)

    pages_to_render = {
        "index.html": ("index.html", {}),
        "people.html": ("people.html", {"people": people}),
        "publications.html": ("publications.html", {"publications_by_year": publications_by_year}),
        "news.html": ("news.html", {"news": news_raw}),
        "simba.html": ("simba.html", {"page": pages["simba"]}),
        "arginls.html": ("arginls.html", {"page": pages["arginls"]}),
        "bmads.html": ("bmads.html", {"page": pages["bmads"]}),
        "apply.html": ("apply.html", {"page": pages["apply"]}),
        "contact.html": ("contact.html", {}),
    }

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for out_name, (template_name, ctx) in pages_to_render.items():
        template = env.get_template(template_name)
        html = template.render(site=site, root="", active_page=out_name, build_date=build_date, **ctx)
        (OUT / out_name).write_text(html, encoding="utf-8")

    shutil.copytree(STATIC, OUT / "static")
    (OUT / ".nojekyll").write_text("")
    # Custom domain for GitHub Pages. Written on every build since the
    # rmtree above would otherwise silently wipe it and disable the domain.
    (OUT / "CNAME").write_text("goldenneurolab.com\n")

    print(f"Built {len(pages_to_render)} pages into {OUT}")


if __name__ == "__main__":
    main()
