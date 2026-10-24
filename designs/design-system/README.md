# SciPy India design system

The visual spec for SciPy India: scipy.in's theme, plus the rules for conference graphics (social posts, stories, banners).

## Designing with Claude

Attach `scipy-india-design-spec.md` to a conversation with Claude and describe what you need, such as "a square post announcing our keynote speaker". That one file holds the brief for Claude, the brand book, every token, the components, ready-made CSS and the logo.

## What's here

- `project/README.md` is the brand book: voice, colour, type, layout, logo, icons.
- `project/tokens.json` holds every colour (light and dark), type style, spacing step, radius and shadow. It is the source of truth.
- `project/components/<Name>/README.md` covers each component: what it is, its exact sizes and colours, and its do's and don'ts. `preview.html` beside it is a token-only sample.
- `project/assets/Logos/scipy-india-logo.svg` is the logo.
- `css/scipy-india-tokens.css` is the tokens as CSS custom properties. It defaults to light, and switches to dark with `data-theme="dark"` (as on scipy.in) or the OS setting.
- `scipy-india-design-spec.md` is everything above in one file, for Claude. Its opening brief lives in `scripts/bundle_intro.md`.

## Changing the spec

Values were measured from scipy.in and the 2026 countdown templates on 24 October 2026.

1. Edit the files in `project/` (or `scripts/bundle_intro.md`).
2. Run `python3 scripts/build_bundle.py`. It regenerates both the CSS and the one-file spec.
3. Commit the sources and the regenerated files together.
