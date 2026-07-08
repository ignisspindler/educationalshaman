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

The visual language is **"Daylight Edition"**: paper-and-ink editorial, like a university press broadsheet. Hairline rules, double newspaper rules, letterpress plates with hard offset shadows, and a faint paper-grain overlay. Dark sections are deliberate "ink plates," not the default. All tokens are CSS custom properties defined at `:root` in `css/style.css`.

**Palette:**
- Paper: `--paper: #f4eee1`, deeper paper: `--paper-2: #ece4d1`
- Ink: `--ink: #211d16`, body: `--ink-2: #4a4335`, muted: `--ink-3: #79705d`
- Accents: Ember `--ember: #bf4d1e` (primary), Steel `--steel: #3f5573` (links), Plum `--plum: #6b4d7a` (tertiary)
- Legacy aliases (`--text`, `--text-muted`, `--amber`, `--indigo`, etc.) map to the new palette and are **re-scoped inside `.section--dark`/`.cta-band`** so inline styles adapt automatically on ink plates. Keep using the aliases in inline styles.

**Typography:** Fraunces (display, variable optical size), Newsreader (body), IBM Plex Mono (labels/badges/eyebrows). Loaded from Google Fonts in each HTML `<head>`.

**Shadows/borders:** No soft shadows. Plates use `1.5px solid var(--ink)` borders with hard offset shadows (e.g. `8px 8px 0 var(--paper-2)`); hovers shift `translate(-2px,-2px)` with an ember offset shadow.

**Layout:** Max-width 1140px, centered. Hamburger nav activates at 860px; other breakpoints at 640/720/760/820/980px. Fluid type via `clamp()`. Scroll reveals are progressive (`.js .rise` pattern in `main.js`); append `?static` to any page URL to disable animations for screenshots.

**Signature elements:** token-stream texture behind the home hero (`.stream`), the framework as a lab specimen table (`.specimen`) with an inverse-mirror row hover, ghost outlined wordmark in the footer (`.ghost-mark`), asterism dividers (`.rule`).

**Note:** `SPEC.md` and `proposal-facelift.html` document the previous dark-neumorphism design and the facelift study that replaced it; both are historical.

## Content

The site is branded **Mindwright.ai** (the repo/domain name `educationalshaman.com` is the legacy name). Copy, glossary terms, and concept names reflect Eugene Geis's proprietary framework. `llms.txt` is a comprehensive LLM-facing reference for all Mindwright terminology — consult it when editing content to stay consistent with established definitions.

The glossary (`glossary.html`) is the most content-dense page and uses a sticky left-label layout pattern that appears elsewhere in `about.html`.
