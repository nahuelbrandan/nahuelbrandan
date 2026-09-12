#!/usr/bin/env python3
"""Actualiza la lista de últimos posts del blog en README.md.

Lee el feed Atom de nahuelbrandan.com y reemplaza el bloque entre los marcadores
<!-- posts:start --> y <!-- posts:end -->. Solo usa la biblioteca estándar.
Lo corre el workflow .github/workflows/update-posts.yml; también se puede correr a mano.
"""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FEED = "https://nahuelbrandan.com/feed.xml"
README = Path(__file__).resolve().parent.parent / "README.md"
COUNT = 3
NS = {"a": "http://www.w3.org/2005/Atom"}
START, END = "<!-- posts:start -->", "<!-- posts:end -->"


def fetch_posts():
    with urllib.request.urlopen(FEED, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    posts = []
    for entry in root.findall("a:entry", NS)[:COUNT]:
        title = entry.findtext("a:title", default="", namespaces=NS).strip()
        date = entry.findtext("a:published", default="", namespaces=NS)[:10]
        link = next(
            (l.get("href") for l in entry.findall("a:link", NS) if l.get("rel", "alternate") == "alternate"),
            "",
        )
        posts.append((date, title, link))
    return posts


def render(posts):
    items = "\n".join(f'<li>{d} &nbsp;<a href="{u}">{t}</a></li>' for d, t, u in posts)
    return f"{START}\n<ul>\n{items}\n</ul>\n{END}"


def main():
    posts = fetch_posts()
    if not posts:
        print("el feed no trajo posts, no toco el README", file=sys.stderr)
        return 1
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        print("no encontré los marcadores en README.md", file=sys.stderr)
        return 1
    new = pattern.sub(lambda _: render(posts), text)
    if new == text:
        print("sin cambios")
        return 0
    README.write_text(new, encoding="utf-8")
    print(f"README actualizado con {len(posts)} posts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
