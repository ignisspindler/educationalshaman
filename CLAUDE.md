# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development

This is a static site — there is no build step. Open any HTML file directly in a browser, or serve the root with any static file server:

```bash
python3 -m http.server 8000
```

To run the Flask API locally:

```bash
pip install -r requirements.txt
cd api && flask --app index run --port 5001
```

The contact form POSTs to `/api/contact`. Locally you'll need `SENDGRID_API_KEY` set in your environment for email to work.

Deploy via Vercel CLI:

```bash
vercel          # preview
vercel --prod   # production
```

## Architecture

**Frontend:** 6 static HTML files (no framework, no bundler). One shared stylesheet (`css/style.css`, ~1300 lines) and one shared script (`js/main.js`, 75 lines). Pages are: `index.html`, `organizations.html`, `personal.html`, `framework.html`, `glossary.html`, `about.html`.

**Backend:** A single Flask WSGI app (`api/index.py`) with one endpoint — `POST /api/contact`. It validates the payload and sends email via SendGrid. Deployed as a Vercel serverless function.

**Routing:** Defined entirely in `vercel.json`. Static files are served by `@vercel/static`; all `/api/*` routes hit the Flask function.

## Design System

The visual language is dark neumorphism. All tokens are CSS custom properties defined at `:root` in `css/style.css`.

**Palette:**
- Background: `--bg: #1f2840`, surfaces: `--surface: #273249`, inset: `--surface-inset: #161e34`
- Accents: Amber `--amber: #c8933c`, Indigo `--indigo: #96a8e8`, Violet `--violet: #b08de8`
- Text: `--text: #e8eaf6`, muted: `--text-muted: #9ba8cc`

**Typography:** Playfair Display (headings), Jost (body), JetBrains Mono (labels/badges). Loaded from Google Fonts in each HTML `<head>`.

**Neumorphic shadows:** Use `--shadow-xs/sm/md/lg` paired variables (light + dark). Never use raw `box-shadow` values — always reference the tokens.

**Layout:** Max-width 1080px, centered. Mobile breakpoints at 600px, 640px, 760px, 820px, 860px. Fluid type via `clamp()`. Hamburger nav activates at 860px.

**Canonical reference:** `SPEC.md` documents the full component inventory, color rationale, and WCAG AA contrast notes.

## Content

The site is branded **Mindwright.ai** (the repo/domain name `educationalshaman.com` is the legacy name). Copy, glossary terms, and concept names reflect Eugene Geis's proprietary framework. `llms.txt` is a comprehensive LLM-facing reference for all Mindwright terminology — consult it when editing content to stay consistent with established definitions.

The glossary (`glossary.html`) is the most content-dense page and uses a sticky left-label layout pattern that appears elsewhere in `about.html`.
