# SciPy India design spec

This one file holds everything needed to design for SciPy India:
- the brand book;
- every token, in light and dark;
- the component specs;
- ready-made CSS variables;
- the logo.

Attach it to a conversation with Claude, then describe what you need.

This file is generated from the spec repository by `scripts/build_bundle.py`. Edit the source files there, not this file.

## Brief for Claude

You are designing for SciPy India. Treat this file as binding.

- **Values.** Use only the colours, sizes, radii and spacing defined here. Don't invent colours or tints; `scipy-blue` belongs to the logo alone.
- **Theme.** Light by default. Make a dark version only when asked, using each token's dark value.
- **Font.** Use the system font stack (`--font-sans`). Use Lato (`--font-export`) only when asked for identical exports across computers.
- **Formats.** Use the sizes and margins under Social formats. For a format that isn't listed, scale from the nearest one.
- **Structure.** Follow the Format recipes under Layout. Build graphics from the components below, with their exact specs, rather than inventing new ones.
- **Code.** For HTML or SVG output:
  - paste the variables from "Tokens as CSS" and refer to them by name;
  - set `data-theme="light"` (or `"dark"`) on the root element, so the viewer's system setting can't switch the theme;
  - inline the SVG from "Logo file" rather than redrawing the logo.
- **Copy.** Follow Voice and copy:
  - dates, times and casing;
  - hashtags per network;
  - no emoji in graphics;
  - alt text for every image, written for the platform's alt-text field. In HTML, also put it on the post's root element as `role="img"` with an `aria-label`.
- **Facts.** The examples use the 2026 edition:
  - SciPy India 2026, 19th–20th December 2026, at IIT Madras, Chennai.
  - Proposals close 1st November 2026 at 23:59 IST, at cfp.scipy.in/scipy-india-2026.

  For another edition or event, use the details you're given, and ask for any that are missing.
- **Check before you finish.**
  - Text meets the pairs under Contrast.
  - Each graphic has one series colour and at most one call-to-action pill.
  - The logo is unchanged and keeps its clear space.
  - On stories, nothing sits outside the safe zones.
