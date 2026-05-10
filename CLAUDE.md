# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is Nahuel Brandan's GitHub profile repository. The `README.md` renders as the public-facing profile page at github.com/nahuelbrandan. Its primary content is HTML/Markdown with badge images, social links, and a skills section.

## Structure

- `README.md` — the GitHub profile page (rendered by GitHub)
- `resources/` — images referenced in the README (banner, logo, GitHub mark variants for dark/light mode)
- `asd.py` — scratch/experimental Python file, not part of the profile

## Running Python scripts

The repo includes a `.venv` (Python 3.12). Activate it before running scripts:

```bash
source .venv/bin/activate
python asd.py
```

## Key details about the README

- Dark/light mode GitHub mark icons are handled via `<picture>` + `<source media="(prefers-color-scheme: ...)">` — keep both variants when editing that section.
- Badge images use `shields.io` URLs with custom colors matching each technology's branding.
- The typing animation SVG is served from `readme-typing-svg.herokuapp.com` — edit the `lines=` query parameter to change displayed text.
