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

## Brand book

SciPy India is an international scientific computing and open source software conference, held annually since 2009 and run by its community. This system covers everything that carries the SciPy India name: the website at scipy.in (built on the PyData Sphinx theme) and the conference's graphics, such as social posts, stories and banners. Colours, type and radii come straight from scipy.in's theme, so a graphic made with these tokens sits naturally next to the website. Post values come from the 2026 countdown templates, measured file by file.

### Voice and copy

Write like a friendly organiser talking to the community: plain, specific, welcoming. Lead with what the reader can do and by when.

- **Name.** "SciPy India", with capital S, P and I. Add the year for an edition: "SciPy India 2026". Never "Scipy India" or "SciPy-India".
- **Spelling.** British, as on scipy.in: programme, flavour, organised, organiser.
- **Lists.** Use the Oxford comma, and keep the website's order: "workshops, talks, and posters".
- **Casing.** Sentence case for headings, labels and buttons: "Call for proposals", "Important dates", "Submit your proposal". Abbreviate as "CFP" only after the full name.
- **Dates.** Ordinal day, full month and year for the event dates and the deadline: "19th–20th December 2026", with an en dash and no spaces.
  - Drop the year only where it already shows nearby, as in a calendar note: "Closes 23:59 IST, 1st November".
  - In strips and charts, use "24 Oct", and "19–20 Dec" where space is tight.
  - Add the weekday when it helps: "Sunday, 1st November 2026".
- **Times.** 24-hour, with the time zone: "23:59 IST".
- **Venue.** "IIT Madras, Chennai" in graphics; the full form on the website: "Indian Institute of Technology Madras, Chennai 600036, Tamil Nadu, India".
- **History.** Count editions from 2009: "our 14th edition since 2009". Avoid wording that reads as if every edition happened after a gap, such as "the 14th edition, the first since 2021".
- **Links.** In graphics, show the domain and path without `https://`: `cfp.scipy.in/scipy-india-2026`. In captions, use the full URL.
- **Hashtags.** Only on Mastodon, in CamelCase: `#SciPyIndia #Python #ScientificComputing #OpenSource`. None on LinkedIn, X or Bluesky.
- **Exclamation marks.** At most one per post, at the start: "8 days left!"
- **Acronyms.** Spell out terms a general reader may not know (STEAM, RSE) when there is room.
- **Emoji.** None in graphics.
- **Standard lines.** Reuse these rather than rewording them:
  - **What we want:** "Workshops, talks, and posters on **scientific computing, research software, and AI/ML applications with a scientific flavour.**" (the bold part is the key phrase).
  - **The deadline:** "Closes **1st November 2026, 23:59 IST**".
  - **On the last day:** "Last call. **Proposals close tonight at 23:59 IST.** Send in your workshop, talk, or poster before then."
- **Alt text.** Every image gets alt text that repeats its words: the countdown, the date and venue, the deadline and the link.

### Colour

Two themes, matching scipy.in's light and dark modes. Graphics default to the light theme; every template also works in dark.

#### Website

- **Grounds.** `background` for pages, `surface` for code blocks and tinted areas, `border` for card and pill outlines.
- **Text.** `text-base` for body, headings and card titles; `text-muted` for navigation, dates and metadata.
- **Teal, the brand colour.** `primary` marks what matters: links, solid buttons, the countdown tiles. Solid buttons put `primary-text` on `primary` and hover to `primary-highlight`.
- **Purple.** `secondary` is for outline buttons and link hover. `secondary-bg` is the announcement band at the top of scipy.in, with `text-base` text and `link-higher-contrast` links.
- **Status.** `info`, `success`, `warning` and `danger`, with their `-bg` tints, are for admonitions. Always pair them with a word or icon.

#### Posts

- **Grounds.** `background` under a `post-grid`; panels in `post-panel` with a 2px `border`. The banner sits on `post-banner` under a `post-banner-grid`.
- **Text.** `on-surface` for the strongest words (wordmark, event line, headlines, key phrases); `post-text` for supporting lines; `post-muted` for small print. On the banner: `post-banner-heading`, `post-banner-text` and `post-banner-link`.
- **Series colour.** Each post series picks one colour for its tiles, icons, "today" markers and call-to-action pill: `primary` by default, `secondary` or `accent` as alternatives. Never mix them in one graphic. Text on the series colour is `on-background`.
- **Tag.** `secondary-bg` with `on-surface` text.
- **Timelines.** `post-rule` for elapsed days, `post-outline` for upcoming ones, `post-past` for crossed-out numbers; the story's day bars use `post-bar-past` and `post-bar-outline`.
- **SciPy blue.** `scipy-blue` belongs to the logo only. Don't use it for UI or text.

#### Contrast

Every text token on `background` and `surface` reaches 4.5:1 in both themes, with two exceptions:

- `primary` on light `surface` is 4.4:1. Use it there only at 24px+ or bold 19px+, or switch to `link-higher-contrast`.
- `secondary` on dark `surface` is 3.4:1. Use it there only for text 24px+, borders or icons.

On posts, `post-text` and `post-muted` reach 4.5:1 on `background` and `post-panel` in both themes. Three pairs rely on the large-text minimum of 3:1, so keep them at 24px+ or bold 19px+:

- `post-past` on `post-panel`: 3.3:1 light, 4.0:1 dark.
- The banner's teal label and link on light `post-banner`: 4.4:1.
- Digits on tiles: at least 3.9:1, the lowest being dark digits on a dark `secondary` tile.

Small text in the series colour on `post-panel` falls short in three cases:
- teal in light (4.4:1);
- pink in light (4.4:1);
- purple in dark (3.9:1).

The calendar's "Deadline" label is one example. Set such labels in `on-surface` instead, and keep the series colour on the outline and the number.

#### Countdown tiles

The flip clock is SciPy India's signature graphic. It is the countdown on scipy.in, and the hero of square, portrait and banner posts.

- **Tile fill.** The series colour.
- **Digits.** `on-background`, which is white in light and near-black in dark, exactly as on the website.
- **Lower half.** `tile-shade` (black at 14%) over the fill. On a teal tile that gives `tile-low`, the colour scipy.in draws.
- **Fold line.** `tile-fold` (black at 40%), drawn over the digits: 3px on posts, 2px on the banner.
- **Corners.**
  - `radius-sm` on the website.
  - `radius-tile` on square and portrait.
  - `radius-panel` on the small "Last day" time tiles.
  - 10px on the banner.
- **Times (23:59).** Two series-colour dots between the hour and minute pairs.

### Type

- **Family.** `sans` everywhere, the system font stack scipy.in uses (San Francisco on Apple devices, Segoe UI on Windows). Graphics use it too, so they match the website on the viewer's screen.
- **Exports.** When several people export graphics on different computers and need identical results, switch graphics to `export` (Lato 400 and 700 from Google Fonts; Lato has no 600, so 600 text renders at 700). Don't mix the two in one graphic.
- **Code.** `mono` for code and code-flavoured labels, such as the story chart's `cfp.days_left()`.
- **Weights.** 400 for running text, 600 for headings, labels and the event line, 700 for numerals, display lines, card titles and emphasis. Nothing lighter than 400.
- **Website scale.** All headings are 600 on 1.15:
  - `h1` 42px, `h2` 34px, `h3` 28px.
  - `h4` 24px, `h5` 20px, `h6` 16px.
  - `body` is 16px on 1.65 (26.4px), and `small` is 14.4px on 1.65.
- **Post scale (1080px canvas).** Square sizes below; each token's usage lists the other formats.
  - `post-numeral` 290px for flip-clock digits.
  - `post-display` 112px for "Days left".
  - `post-wordmark` 38px, `post-headline` 36px, `post-event` 27px.
  - `post-tag` and `post-footer` 22px, `post-caption` 19px.
  - Stories use `post-story-numeral` (400px) instead of tiles.
  - The banner adds `post-banner-title` (50px).
- **Line breaks.** Balance multi-line headlines (`text-wrap: balance`) so no word sits alone on the last line.

### Layout, shape and depth

- **Website cards.** Transparent, a 1px `border`, `radius-sm`, padding `space-4`, and `shadow-card` in light or `shadow-card-dark` in dark.
- **Website buttons.** Solid (`primary`) for the main action and outline (`secondary`) for the rest. Both are 16px with `radius-sm`.
- **Website pill buttons** ("+ Add to calendar"). `radius-pill` with a 1px `border`.
- **Posts.** Flat: no shadows, and no gradients in the sense of colour fades. Panels use `radius-panel`, flip-clock tiles `radius-tile`, and tags and call-to-action pills `radius-pill`.
- **Graph-paper grid.** Posts sit on a grid of 2px lines: `post-grid` every 54px, or `post-banner-grid` every 45px on the banner.
  - Placement: the lines are centred on multiples of the pitch, counted from the top-left corner.
  - In CSS, draw it with hard-stop gradients, which make crisp lines rather than a fade:

    ```css
    background-color: var(--background);
    background-image: linear-gradient(var(--post-grid) 2px, transparent 2px),
      linear-gradient(90deg, var(--post-grid) 2px, transparent 2px);
    background-size: 54px 54px;
    background-position: -1px -1px;
    ```
  - It is the one decorative texture. Keep it faint, and keep dense text on a panel.

#### Social formats

| Format | Size | Use on | Margins (top, sides, bottom) |
| --- | --- | --- | --- |
| Square | 1080 × 1080 | X, Bluesky, Mastodon | 72px all round (`post-margin`) |
| Portrait | 1080 × 1350 | LinkedIn | 76px, 80px (`post-margin-portrait`), 76px |
| Story | 1080 × 1920 | Instagram, WhatsApp Status | `story-safe-top` 200px, `story-margin` 88px, `story-safe-bottom` 260px |
| Banner | 1200 × 675 | Announcements, link previews, LinkedIn on key days | 56px, `post-margin-banner` 64px, 56px |

Every post stacks the same parts, top to bottom:

1. The lockup, with the tag on the right.
2. The event line: the date with a calendar icon, then the venue with a map pin.
3. The hero: flip clock and "Days left", the big story numeral, or "Last day" with the closing time.
4. The timeline and one supporting line, in the order each recipe gives.
5. The deadline and link: the Footer on square, a call-to-action pill on portrait and story.

#### Format recipes

Measured from the 2026 templates. In each recipe, the post is a column with `justify-content: space-between` inside its margins, and each numbered item is one direct child. Gaps inside an item are given.

##### Square (1080 × 1080)

1. **Header**, 22px gap: the lockup row (lockup left, Tag right, at least 24px apart), then the EventLine.
2. **Middle**, 40px gap between its three parts:
   - **Hero:** a row, vertically centred, 44px gap.
     - On the left, the FlipClock days tiles.
     - On the right, a column with 20px gap: "Days" and "left" on two lines in `post-display` and `on-surface`, then "to submit your proposal" at 32px on 1.3 in `post-text`, at most 340px wide.
     - At 1 day left, "Day left".
   - **Supporting line:** in `post-headline`.
   - **Timeline:** the ProgressStrip.
3. **Footer.**

**Last day:** the hero becomes a column with 24px gap: "Last day" in `post-display`, then the FlipClock time row ("23:59" and "IST"). The supporting line becomes the last-day line.

##### Portrait (1080 × 1350)

1. **Header** as on square.
2. **Hero,** centred, 26px gap: the FlipClock days tiles, then one centred line at 46px, 600, on 1.15, in `on-surface`: "Days left" in the series colour, then "to submit your proposal".
3. **The CountdownCalendar.**
4. **Supporting line:** the "What we want" line at 30px on 1.35, full width, centred and balanced.
5. **Call-to-action pill,** centred: "Submit at cfp.scipy.in/scipy-india-2026".

**Last day:** the hero is a centred column with 24px gap: "Last day" in `post-display`, then the time row (144 × 200 tiles, dots 40px apart).

##### Story (1080 × 1920)

1. **Header,** 24px gap, at story sizes.
2. **Hero:** a row with bottoms aligned and 44px gap.
   - The number of days in `post-story-numeral`, unpadded ("7").
   - Then a column with 18px gap and 4px bottom padding:
     - "days" and "left" on two lines at 110px, 700, on 0.95, in the series colour ("day" at 1);
     - "until the call for proposals closes" at 34px on 1.3 in `post-text`, at most 440px wide, balanced.
3. **The DayBars.**
4. **Supporting line:** 36px on 1.35, worded for stories: "Send us your **workshop, talk, or poster** on scientific computing, research software, and AI/ML applications with a scientific flavour."
5. **Closing group,** left-aligned, 18px gap: the call-to-action pill, then "Closes **1st November 2026, 23:59 IST**" at 26px on 1.3, in `post-muted` with the bold part in `on-surface`.

**Last day:** the hero is a column with 24px gap:
- "Last" and "day" on two lines at 180px, 700, on 0.9, in the series colour, letter-spacing −0.01em;
- then "Proposals close tonight at **23:59 IST**" at 38px on 1.3.

##### Banner (1200 × 675)

Two columns: the left fills the space, the right is 360px wide, `space-7` (48px) apart.

- **Left column,** `space-between`, three items:
  1. 14px gap: the lockup and the EventLine, both at banner size.
  2. 14px gap:
     - "Call for proposals" as a plain label in `post-tag`, in the series colour;
     - the headline in `post-banner-title` and `post-banner-heading`, balanced;
     - the supporting text at 21px on 1.45 in `post-banner-text`, at most 620px wide.
  3. A wrapping row with 20px gap:
     - the call-to-action pill, "Submit your proposal";
     - the link at 20px, 700, on 1.3, in `post-banner-link`.
- **Right column:** a centred countdown card.
  - **Card box:**
    - Fill: `background`.
    - Outline: 2px, in `secondary-bg` in light and in `background` in dark.
    - Corners and padding: `radius-panel`, padding 34px 30px.
    - Layout: content centred, 18px gap.
  - **Contents, top to bottom:**
    1. "Closes in" at 20px, 600, in `post-muted`.
    2. The FlipClock at banner size.
    3. "Days left" at 32px, 700, on 1.1, in `on-surface`.
    4. A 2px `post-rule` divider.
    5. The date, 4px gap between its lines: "1st November 2026" at 22px, 600, in `on-surface`, then "23:59 IST" at 20px in `post-muted`.
  - **On the last day:** the card reads "Closes tonight at", then the time tiles and "IST", then "Last day" over "Sunday, 1st November 2026".
  - **With the countdown off,** the logo takes the card's place at 320px.

### Logo

`assets/Logos/scipy-india-logo.svg` is the SciPy mark: a `scipy-blue` disc with a white snake.

- **As supplied.** Use the file unchanged. Never recolour, outline, stretch, rotate or crop it, and never place it on a photo or busy pattern.
- **Clear space.** Keep at least a quarter of the disc's diameter clear on every side.
- **Sizes.**
  - Website header: 48px.
  - Posts: 68px on square and portrait, 76px on stories, 52px on the banner.
  - These sizes are the SVG's box, and the disc fills about 90% of it.
  - Never smaller than 24px on screen.
- **Lockup.** Logo, then "SciPy India 2026", vertically centred.
  - Website: 20px at 400, 8px apart.
  - Posts: `post-wordmark` in `on-surface`, 18px apart (20px on stories, 14px on the banner).
- **Grounds.** It reads on `background`, `surface`, `secondary-bg` and `post-banner` in both themes. The faint post grid behind it is fine.

### Icons

- **Website.** The header's social links use Font Awesome brand icons.
- **Graphics.** Use simple outline icons, drawn as inline SVG with round caps and joins.
  - Each sits on a 24-unit viewBox. Sizes below are the rendered size, and stroke widths are in viewBox units.
  - **Event line.** Calendar and map pin in the series colour: 30px with a 2.25px stroke (32px on stories, 24px on the banner).
  - **Footer clock.** `post-muted`, 28px with a 2px stroke.
  - **Arrows on links and pills.** `currentColor`, with a 2.5–2.75px stroke.
- **The set.** Each icon is drawn with `fill="none"`, `stroke="currentColor"`, `stroke-linecap="round"` and `stroke-linejoin="round"`. Set the stroke width and rendered size per use. The shapes:

  ```html
  <!-- calendar -->
  <svg viewBox="0 0 24 24"><rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/></svg>
  <!-- map pin -->
  <svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.6a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.4" r="2.6"/></svg>
  <!-- clock -->
  <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
  <!-- right arrow -->
  <svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
  ```
- **No emoji.** Don't use emoji as icons.

### Motion

The countdown on scipy.in flips each second (FlipDown). Graphics are static. Don't animate the logo.

### Accessibility

- **Contrast.** Text meets the pairs in Colour.
- **Hit areas.** Interactive elements on the website keep a 44px minimum.
- **Alt text.** Every published image has alt text, written as in Voice and copy.
- **Colour alone.** Never carries meaning on its own:
  - The calendar and the day bars say "Today" and "Deadline" in words.
  - The progress strip sets today's date in bold as well as colour.

## Tokens

### Colour

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `background` | `#ffffff` | `#14181e` | Page and post background. Text on it: text-base, text-muted, primary. |
| `on-background` | `#ffffff` | `#222832` | Layers that sit on background (header bar, menus). On posts: the digits on flip-clock tiles (exactly as the countdown on scipy.in colours them), and the text on call-to-action pills and 'Today' markers. |
| `surface` | `#f3f4f5` | `#29313d` | Code blocks and tinted areas on the website. Posts use post-panel instead. |
| `on-surface` | `#222832` | `#f3f4f5` | Strongest text on posts: the wordmark, the event line, headlines, key phrases and the tag. Reads on background, surface, post-panel and secondary-bg in both themes. |
| `text-base` | `#222832` | `#ced6dd` | Body text and headings on the website, card titles, the announcement band and the 'Add to calendar' pill. |
| `heading` | same as `text-base` | same as `text-base` | Headings on the website; same as text-base. |
| `text-muted` | `#48566b` | `#9ca4af` | Secondary text on the website: navigation, dates, captions and metadata on background and surface. |
| `border` | `#d1d5da` | `#48566b` | Card and pill borders and dividers on the website; the 2px outline of panels on posts. |
| `border-muted` | `#17171a33` | `#29313d` | Faint dividers inside cards and tables. |
| `primary` | `#0a7d91` | `#3fb1c5` | Brand teal: links, solid buttons, the flip-clock tiles, and the default series colour on posts (tiles, icons, 'today' markers, call-to-action pills). As text it passes 4.5:1 on background in both themes and on dark surface; on light surface (4.4:1) use it at 24px+ or bold 19px+, or use link-higher-contrast. |
| `primary-highlight` | `#086b7c` | `#319aac` | Hover and focus fill of solid primary buttons on the website. |
| `primary-text` | `#ffffff` | `#14181e` | Text on solid primary buttons on the website. (Pills on posts use on-background.) |
| `primary-bg` | `#d0ecf1` | `#042c33` | Tinted backgrounds behind primary content. |
| `secondary` | `#8045e5` | `#9c5ffd` | Brand purple: outline buttons and link hover. Passes 4.5:1 on background in both themes; on dark surface (3.4:1) use it only for text 24px+, borders or icons. An alternative series colour for countdown posts. |
| `secondary-highlight` | `#651ee0` | `#7c2bfc` | Hover and pressed states of secondary fills. |
| `secondary-text` | `#ffffff` | `#14181e` | Text on secondary fills, including outline buttons on hover. |
| `secondary-bg` | `#e0c7ff` | `#341a61` | The announcement band at the top of scipy.in (text-base text) and the 'Call for proposals' tag on posts (on-surface text). |
| `accent` | `#c132af` | `#e47fd7` | Pink accent, sparingly: an alternative series colour for countdown posts, small highlights. Never for body text. |
| `accent-bg` | `#f8dff5` | `#46123f` | Tinted backgrounds behind accent content. |
| `link` | same as `primary` | same as `primary` | Link text on background. |
| `link-hover` | same as `secondary` | same as `secondary` | Link text on hover. |
| `link-higher-contrast` | `#085d6c` | `#3fb1c5` | Links on surface and tinted backgrounds, such as the announcement band, where primary falls short of 4.5:1. |
| `inline-code` | `#912583` | `#f3c7ee` | Inline code text on the website. |
| `info` | `#276be9` | `#79a3f2` | Note admonitions on the website. Pair with a label or icon. |
| `info-bg` | `#dce7fc` | `#06245d` | Background of info admonitions. |
| `success` | `#00843f` | `#5fb488` | Success and 'open' states. Pair with a word or icon; never told apart from danger by hue alone. |
| `success-bg` | `#d6ece1` | `#002f17` | Background of success admonitions. |
| `warning` | `#f66a0a` | `#ff9245` | Warnings and deadlines in admonitions. Fill or border only in light theme (below 4.5:1 as text on white). |
| `warning-bg` | `#f8e3d0` | `#652a02` | Background of warning admonitions. |
| `danger` | `#d72d47` | `#e78894` | Errors and destructive actions. Pair with a word or icon. |
| `danger-bg` | `#f9e1e4` | `#4e111b` | Background of danger admonitions. |
| `scipy-blue` | `#0054a6` | `#0054a6` | The SciPy logo's disc only. Part of the mark, never a UI or text colour. |
| `tile-low` | `#096c7d` | `#3698a9` | Lower half of a primary flip-clock tile: primary under tile-shade, as scipy.in's countdown draws it. For secondary or accent tiles, lay tile-shade over the tile colour instead. |
| `tile-shade` | `#00000024` | `#00000024` | Black at 14% (rgba(0, 0, 0, 0.14)), laid over the lower half of every flip-clock tile. |
| `tile-fold` | `#00000066` | `#00000066` | Black at 40% (rgba(0, 0, 0, 0.4)): the fold line across the middle of a flip-clock tile, 3px on posts and 2px on the banner. |
| `post-text` | `#48566b` | `#ced6dd` | Supporting lines and running text on posts; the key phrase inside them switches to on-surface at 700. |
| `post-muted` | `#5f6a79` | `#9ca4af` | Small print on posts: progress-strip dates, calendar weekdays and note, chart labels, footer icons, the story's closing line, the banner card's labels. |
| `post-panel` | `#f3f4f5` | `#222832` | Fill of panels on posts: the countdown calendar and the story's day bars. Outline: 2px border. |
| `post-outline` | `#c5cbd3` | `#48566b` | Outline of upcoming days and the strike through past days in the countdown calendar. |
| `post-grid` | `#eef0f3` | `#1b2129` | Graph-paper grid on square, portrait and story posts: 2px lines every 54px over background. |
| `post-rule` | `#e3e6ea` | `#29313d` | Footer divider and elapsed days in the progress strip on square posts; outline of crossed-out days in the countdown calendar; the divider in the banner's countdown card. |
| `post-past` | `#7d8693` | `#7d8693` | Numbers of days already gone in the countdown calendar, crossed out. 3.3:1 on light post-panel and 4.0:1 on dark, so only at 24px+ or bold 19px+. |
| `post-bar-past` | `#dde1e6` | `#29313d` | Fill of elapsed days in the story's day bars. |
| `post-bar-outline` | `#b9c0c9` | `#48566b` | 3px outline of upcoming days in the story's day bars. |
| `post-banner` | `#f7f2ff` | `#341a61` | Background of the 16:9 call-for-proposals banner. Text on it: post-banner-heading, post-banner-text and post-banner-link. |
| `post-banner-grid` | `#eee5fd` | `#3c2070` | Graph-paper grid on the banner: 2px lines every 45px over post-banner. |
| `post-banner-heading` | `#222832` | `#ffffff` | Wordmark, event line and headline on the banner. |
| `post-banner-text` | `#48566b` | `#e6dcff` | Supporting text on the banner. |
| `post-banner-link` | `#0a7d91` | `#d9c8ff` | The link beside the call-to-action pill on the banner. In light it follows the series colour (primary by default); 4.4:1 on post-banner, so keep it bold 19px+. |

### Type families

| Family | Stack |
| --- | --- |
| `sans` | `system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"` |
| `mono` | `ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, "DejaVu Sans Mono", monospace` |
| `export` | `Lato, sans-serif` |

### Type: Website (`sans`)

scipy.in's PyData Sphinx theme: the system font, headings at 600 on 1.15, body 16px on 1.65.

| Style | Size | Line height | Weight | Use |
| --- | --- | --- | --- | --- |
| `h1` | 42px | 1.15 | 600 | Page title. |
| `h2` | 34px | 1.15 | 600 | Section headings. |
| `h3` | 28px | 1.15 | 600 | Sub-sections. |
| `h4` | 24px | 1.15 | 600 | Minor headings. |
| `h5` | 20px | 1.15 | 600 | Small headings. |
| `h6` | 16px | 1.15 | 600 | The smallest heading. |
| `body` | 16px | 1.65 | 400 | Running text. Card titles use it at 700; buttons use it on 1.5. |
| `small` | 14.4px | 1.65 | 400 | Pill buttons, captions, metadata. |

### Type: Social posts (`sans`)

Sizes for 1080px-wide canvases. Where a format differs, the usage gives its size; the banner (1200px wide) has its own, smaller set.

| Style | Size | Line height | Weight | Use |
| --- | --- | --- | --- | --- |
| `post-numeral` | 290px | 1 | 700 | Flip-clock digits: 290px on square, 266px on portrait, 160px on the banner. Last-day time tiles: 190px square, 180px portrait, 78px banner. |
| `post-story-numeral` | 400px | 0.78 | 700 | The single big number on stories, in on-surface, letter-spacing -0.02em. |
| `post-display` | 112px | 0.95 | 700 | 'Days left' and 'Last day' on square and portrait. Stories: 'days left' at 110px in the series colour; 'Last day' at 180px on 0.9. The line under it: 32px post-text on square, 34px on stories; portrait sets one centred 46px/600 line with 'Days left' in the series colour. |
| `post-wordmark` | 38px | 1.15 | 600 | The name beside the logo: 38px on square and portrait, 40px on stories, 28px on the banner. |
| `post-banner-title` | 50px | 1.08 | 700 | The banner's headline, balanced over two lines. |
| `post-headline` | 36px | 1.3 | 400 | Supporting line in post-text; set the key phrase in 700 and on-surface. Square 36px on 1.3; portrait 30px on 1.35; story 36px on 1.35; banner 21px on 1.45. |
| `post-cta` | 30px | 1.2 | 700 | Call-to-action pill text: 30px on portrait, 32px on stories, 22px on the banner. |
| `post-event` | 27px | 1.25 | 600 | Date and venue line, with icons: 27px on square and portrait, 29px on stories, 21px on the banner. |
| `post-tag` | 22px | 1.2 | 600 | Tag pill text on every format; the banner's plain 'Call for proposals' label. |
| `post-footer` | 22px | 1.3 | 400 | Deadline and link in the square post's footer (link at 700). Stories set the closing line at 26px. |
| `post-caption` | 19px | 1.2 | 400 | Progress-strip dates on square posts; the 'Today' pill on stories (at 700). |

### Type: Code (`mono`)

| Style | Size | Line height | Weight | Use |
| --- | --- | --- | --- | --- |
| `code` | 14.4px | 1.65 | 400 | Code on the website. On stories, the chart header is 22px and the bar values 24px at 700. |

### Spacing

The website uses Bootstrap's spacers (0.25, 0.5, 1, 1.5 and 3rem), which are space-1, space-2, space-4, space-5 and space-7. space-3 and space-6 fill the gaps for graphics. The 2026 templates also use a few in-between values (10, 14, 18, 20, 22, 26px) in tight spots; prefer the steps in new work.

| Token | Value | Use |
| --- | --- | --- |
| `space-1` | `4px` | Bootstrap spacer 1. Tight gaps, such as between the two lines of the banner card's date. |
| `space-2` | `8px` | Bootstrap spacer 2. Between the logo and the name in the website header; between buttons in a row; padding of the announcement band. |
| `space-3` | `12px` | Icon-to-label gap in the event line; bar-to-label gap in the progress strip; between the banner's tiles and the story's day bars. |
| `space-4` | `16px` | Bootstrap spacer 3. Card padding on the website; gap between flip-clock tiles on posts. |
| `space-5` | `24px` | Bootstrap spacer 4. Between the lockup and the tag; between the stacked header lines on stories. |
| `space-6` | `32px` | Inner padding of panels on posts (30–40px in the 2026 templates). |
| `space-7` | `48px` | Bootstrap spacer 5. Between the banner's two columns. |
| `post-margin` | `72px` | Outer margin of the 1080×1080 square post, all sides. |
| `post-margin-portrait` | `80px` | Side margin of the 1080×1350 portrait post; top and bottom are 76px. |
| `story-margin` | `88px` | Side margin of 1080×1920 stories. |
| `story-safe-top` | `200px` | Keep text below this on stories (app chrome covers the top). |
| `story-safe-bottom` | `260px` | Keep text above this on stories (reply bar covers the bottom). |
| `post-margin-banner` | `64px` | Side margin of the 1200×675 banner; top and bottom are 56px. |

### Radius

Squared off on the website; softer, larger shapes on posts.

| Token | Value | Use |
| --- | --- | --- |
| `radius-sm` | `4px` | Website cards and buttons; the countdown tiles on scipy.in. |
| `radius-panel` | `12px` | Panels on posts (the countdown calendar, the story's day bars, the banner's countdown card) and the small time tiles on 'Last day' posts. Calendar cells and the banner's day tiles use 10px, its small time tiles 6px. |
| `radius-tile` | `18px` | Flip-clock tiles on square and portrait posts (about 8% of the tile's width). Stories use a single big numeral instead of tiles. |
| `radius-pill` | `999px` | Tags, pill buttons, call-to-action pills, progress-strip bars. |

### Shadow

Cards on the website only, and the shadow differs by theme. Posts are flat.

| Token | Value | Use |
| --- | --- | --- |
| `shadow-card` | `0 3.2px 8px 0 rgba(0, 0, 0, 0.1), 0 0 1px 0 rgba(0, 0, 0, 0.1)` | Cards on the website in light theme. |
| `shadow-card-dark` | `0 2px 4px 0 rgba(0, 0, 0, 0.15)` | Cards on the website in dark theme. |

## Tokens as CSS

Paste this into any HTML graphic, and set `data-theme="light"` or `data-theme="dark"` on the root element. Without it, the block at the end follows the viewer's system setting, which suits the website but not a graphic.

```css
/* SciPy India design tokens, generated from project/tokens.json. Do not edit by hand.
   Light is the default; dark follows scipy.in's data-theme="dark" and the OS setting. */
:root {
  --background: #ffffff;
  --on-background: #ffffff;
  --surface: #f3f4f5;
  --on-surface: #222832;
  --text-base: #222832;
  --heading: var(--text-base);
  --text-muted: #48566b;
  --border: #d1d5da;
  --border-muted: #17171a33;
  --primary: #0a7d91;
  --primary-highlight: #086b7c;
  --primary-text: #ffffff;
  --primary-bg: #d0ecf1;
  --secondary: #8045e5;
  --secondary-highlight: #651ee0;
  --secondary-text: #ffffff;
  --secondary-bg: #e0c7ff;
  --accent: #c132af;
  --accent-bg: #f8dff5;
  --link: var(--primary);
  --link-hover: var(--secondary);
  --link-higher-contrast: #085d6c;
  --inline-code: #912583;
  --info: #276be9;
  --info-bg: #dce7fc;
  --success: #00843f;
  --success-bg: #d6ece1;
  --warning: #f66a0a;
  --warning-bg: #f8e3d0;
  --danger: #d72d47;
  --danger-bg: #f9e1e4;
  --scipy-blue: #0054a6;
  --tile-low: #096c7d;
  --tile-shade: #00000024;
  --tile-fold: #00000066;
  --post-text: #48566b;
  --post-muted: #5f6a79;
  --post-panel: #f3f4f5;
  --post-outline: #c5cbd3;
  --post-grid: #eef0f3;
  --post-rule: #e3e6ea;
  --post-past: #7d8693;
  --post-bar-past: #dde1e6;
  --post-bar-outline: #b9c0c9;
  --post-banner: #f7f2ff;
  --post-banner-grid: #eee5fd;
  --post-banner-heading: #222832;
  --post-banner-text: #48566b;
  --post-banner-link: #0a7d91;
  --font-sans: system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-mono: ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, "DejaVu Sans Mono", monospace;
  --font-export: Lato, sans-serif;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --post-margin: 72px;
  --post-margin-portrait: 80px;
  --story-margin: 88px;
  --story-safe-top: 200px;
  --story-safe-bottom: 260px;
  --post-margin-banner: 64px;
  --radius-sm: 4px;
  --radius-panel: 12px;
  --radius-tile: 18px;
  --radius-pill: 999px;
  --shadow-card: 0 3.2px 8px 0 rgba(0, 0, 0, 0.1), 0 0 1px 0 rgba(0, 0, 0, 0.1);
  --shadow-card-dark: 0 2px 4px 0 rgba(0, 0, 0, 0.15);
  --text-h1-size: 42px;
  --text-h1-line-height: 1.15;
  --text-h1-weight: 600;
  --text-h2-size: 34px;
  --text-h2-line-height: 1.15;
  --text-h2-weight: 600;
  --text-h3-size: 28px;
  --text-h3-line-height: 1.15;
  --text-h3-weight: 600;
  --text-h4-size: 24px;
  --text-h4-line-height: 1.15;
  --text-h4-weight: 600;
  --text-h5-size: 20px;
  --text-h5-line-height: 1.15;
  --text-h5-weight: 600;
  --text-h6-size: 16px;
  --text-h6-line-height: 1.15;
  --text-h6-weight: 600;
  --text-body-size: 16px;
  --text-body-line-height: 1.65;
  --text-body-weight: 400;
  --text-small-size: 14.4px;
  --text-small-line-height: 1.65;
  --text-small-weight: 400;
  --text-post-numeral-size: 290px;
  --text-post-numeral-line-height: 1;
  --text-post-numeral-weight: 700;
  --text-post-story-numeral-size: 400px;
  --text-post-story-numeral-line-height: 0.78;
  --text-post-story-numeral-weight: 700;
  --text-post-display-size: 112px;
  --text-post-display-line-height: 0.95;
  --text-post-display-weight: 700;
  --text-post-wordmark-size: 38px;
  --text-post-wordmark-line-height: 1.15;
  --text-post-wordmark-weight: 600;
  --text-post-banner-title-size: 50px;
  --text-post-banner-title-line-height: 1.08;
  --text-post-banner-title-weight: 700;
  --text-post-headline-size: 36px;
  --text-post-headline-line-height: 1.3;
  --text-post-headline-weight: 400;
  --text-post-cta-size: 30px;
  --text-post-cta-line-height: 1.2;
  --text-post-cta-weight: 700;
  --text-post-event-size: 27px;
  --text-post-event-line-height: 1.25;
  --text-post-event-weight: 600;
  --text-post-tag-size: 22px;
  --text-post-tag-line-height: 1.2;
  --text-post-tag-weight: 600;
  --text-post-footer-size: 22px;
  --text-post-footer-line-height: 1.3;
  --text-post-footer-weight: 400;
  --text-post-caption-size: 19px;
  --text-post-caption-line-height: 1.2;
  --text-post-caption-weight: 400;
  --text-code-size: 14.4px;
  --text-code-line-height: 1.65;
  --text-code-weight: 400;
}
:root[data-theme="dark"] {
  --background: #14181e;
  --on-background: #222832;
  --surface: #29313d;
  --on-surface: #f3f4f5;
  --text-base: #ced6dd;
  --text-muted: #9ca4af;
  --border: #48566b;
  --border-muted: #29313d;
  --primary: #3fb1c5;
  --primary-highlight: #319aac;
  --primary-text: #14181e;
  --primary-bg: #042c33;
  --secondary: #9c5ffd;
  --secondary-highlight: #7c2bfc;
  --secondary-text: #14181e;
  --secondary-bg: #341a61;
  --accent: #e47fd7;
  --accent-bg: #46123f;
  --link-higher-contrast: #3fb1c5;
  --inline-code: #f3c7ee;
  --info: #79a3f2;
  --info-bg: #06245d;
  --success: #5fb488;
  --success-bg: #002f17;
  --warning: #ff9245;
  --warning-bg: #652a02;
  --danger: #e78894;
  --danger-bg: #4e111b;
  --tile-low: #3698a9;
  --post-text: #ced6dd;
  --post-muted: #9ca4af;
  --post-panel: #222832;
  --post-outline: #48566b;
  --post-grid: #1b2129;
  --post-rule: #29313d;
  --post-bar-past: #29313d;
  --post-bar-outline: #48566b;
  --post-banner: #341a61;
  --post-banner-grid: #3c2070;
  --post-banner-heading: #ffffff;
  --post-banner-text: #e6dcff;
  --post-banner-link: #d9c8ff;
  --shadow-card: var(--shadow-card-dark);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --background: #14181e;
    --on-background: #222832;
    --surface: #29313d;
    --on-surface: #f3f4f5;
    --text-base: #ced6dd;
    --text-muted: #9ca4af;
    --border: #48566b;
    --border-muted: #29313d;
    --primary: #3fb1c5;
    --primary-highlight: #319aac;
    --primary-text: #14181e;
    --primary-bg: #042c33;
    --secondary: #9c5ffd;
    --secondary-highlight: #7c2bfc;
    --secondary-text: #14181e;
    --secondary-bg: #341a61;
    --accent: #e47fd7;
    --accent-bg: #46123f;
    --link-higher-contrast: #3fb1c5;
    --inline-code: #f3c7ee;
    --info: #79a3f2;
    --info-bg: #06245d;
    --success: #5fb488;
    --success-bg: #002f17;
    --warning: #ff9245;
    --warning-bg: #652a02;
    --danger: #e78894;
    --danger-bg: #4e111b;
    --tile-low: #3698a9;
    --post-text: #ced6dd;
    --post-muted: #9ca4af;
    --post-panel: #222832;
    --post-outline: #48566b;
    --post-grid: #1b2129;
    --post-rule: #29313d;
    --post-bar-past: #29313d;
    --post-bar-outline: #48566b;
    --post-banner: #341a61;
    --post-banner-grid: #3c2070;
    --post-banner-heading: #ffffff;
    --post-banner-text: #e6dcff;
    --post-banner-link: #d9c8ff;
    --shadow-card: var(--shadow-card-dark);
  }
}
```

## Components

### Lockup

The SciPy logo beside the name, used at the top of the website header and every graphic.

- **Consumer provides:** the edition name ("SciPy India 2026") and the size: website or post.
- **Website size:** logo 48px, name at 20px weight 400 in `text-base`, 8px (`space-2`) apart.
- **Post size:** the name in `post-wordmark` and `on-surface` (`post-banner-heading` on the banner).

  | Format | Logo | Name | Gap |
  | --- | --- | --- | --- |
  | Square and portrait | 68px | 38px | 18px |
  | Story | 76px | 40px | 20px |
  | Banner | 52px | 28px | 14px |

- **Do:** centre the logo and name vertically; keep clear space of a quarter of the disc's diameter around the logo.
- **Don't:** put the name above or below the logo, change the logo's colours, or set the name in a different family from the rest of the graphic.

### EventLine

The date and venue of the edition on one line, each with an outline icon, placed directly under the lockup on every graphic.

- **Consumer provides:** the dates ("19th–20th December 2026") and the venue ("IIT Madras, Chennai").
- **Style:** `post-event` (weight 600, on 1.25) in `on-surface`, with calendar and map-pin icons in the series colour (2.25px stroke).

  | Format | Text | Icons | Icon to text | Between items |
  | --- | --- | --- | --- | --- |
  | Square and portrait | 27px | 30px | 12px | 36px (12px when wrapped) |
  | Story | 29px | 32px | 12px | 36px (12px when wrapped) |
  | Banner | 21px, `post-banner-heading` | 24px | 10px | 28px (8px when wrapped) |

- **Do:** keep the dates first and the venue second; let the items wrap onto two lines on narrow canvases.
- **Don't:** shorten the venue to the city alone, or drop the icons.

### Tag

A small pill that labels what a graphic is about, such as "Call for proposals" or "Registrations open".

- **Consumer provides:** two or three words in sentence case.
- **Style:** `secondary-bg` fill, `on-surface` text in `post-tag` (22px, weight 600), `radius-pill`, padding 12px 22px.
- **Where:** top right of square, portrait and story posts, level with the lockup. The banner sets the same words as a plain label in the series colour instead of a pill.
- **Don't:** use more than one tag per graphic, or turn it into a button.

### FlipClock

Split-flap number tiles, SciPy India's signature graphic, matching the countdown on scipy.in.

- **Consumer provides:** a two-digit number (pad single digits: "07") or a time ("23:59"), and a label beside or below it ("Days left", "Last day").
- **Tile:**
  - Fill: the series colour, with `tile-shade` (black at 14%) over the lower half. On teal this gives `tile-low`.
  - Fold: a `tile-fold` line (black at 40%) across the middle.
  - Digits: `on-background` at weight 700, on line height 1, centred. The font size is about 90% of the tile height; the table gives exact sizes.
- **Sizes:**

  | Use | Tile | Digits | Corners | Gap | Fold |
  | --- | --- | --- | --- | --- | --- |
  | Square, days | 236 × 320 | 290px | `radius-tile` | 16px | 3px |
  | Portrait, days | 224 × 300 | 266px | `radius-tile` | 16px | 3px |
  | Banner, days | 128 × 176 | 160px | 10px | 12px | 2px |
  | Square, time | 150 × 212 | 190px | `radius-panel` | 10px | 3px |
  | Portrait, time | 144 × 200 | 180px | `radius-panel` | 10px | 3px |
  | Banner, time | 60 × 88 | 78px | 6px | 6px | 2px |
  | Website | — | — | `radius-sm` | — | — |

- **Times:** two tiles, two series-colour dots, two tiles, then "IST" in `on-surface`.
  - Square and portrait: 18px dots, "IST" at 64px.
  - Banner: 9px dots, "IST" at 32px.
- **Alternatives:** `secondary` or `accent` may replace `primary` for a whole series, never mixed within one graphic.
- **Do:** say what the number counts in words next to it.
- **Don't:** use more than four tiles, animate tiles in graphics, or put digits in any colour but `on-background`.

### ProgressStrip

A row of short bars, one per day of a campaign, with today highlighted. It runs along the bottom of square countdown posts.

- **Consumer provides:** the campaign's dates (up to nine) and which one is today.
- **Bars:**
  - Shape: 14px tall on a 1080px canvas, fully rounded, equal widths, 10px apart.
  - Days gone: `post-rule`.
  - Today: the series colour.
  - Days to come: the series colour at 35% opacity.
- **Labels:** the date under each bar, 12px below it and left-aligned with it, in `post-caption`. Use `post-muted` at 400, and the series colour at 700 for today.
- **Do:** start the strip on the campaign's first day, not the first day shown elsewhere.
- **Don't:** use it for more than nine days; switch to CountdownCalendar instead.

### CountdownCalendar

A two-week calendar panel that shows a deadline approaching: past days crossed out, today filled, the deadline outlined. It is the timeline on portrait posts.

- **Consumer provides:**
  - The deadline and today's date. The panel shows the two Monday-to-Sunday weeks that end with the deadline's week. For a Sunday deadline of 1st November, that is 19th October to 1st November.
  - A title ("October–November 2026") and a note ("Closes 23:59 IST, 1st November").
- **Panel:**
  - Box: `post-panel` fill, 2px `border` and `radius-panel`, padding 30px 32px, 18px between rows.
  - Header row: the title on the left and the note on the right, baselines aligned, at least 16px apart.
  - Title: 24px at 600 on 1.25, in `on-surface`.
  - Note: 21px on 1.25, in `post-muted`.
  - Weekdays: three letters ("Mon"), 18px at 600 on 1.2, in `post-muted`, centred over the columns.
- **Cells:**
  - Box: seven equal columns, 10px apart. Each cell is 96px tall with 10px corners, a 2px outline and no fill except on today.
  - Content: centred, 2px gap. The number is at 40px, 700, on line height 1. Under it is a label line 18px tall, with the text at 15px and 700. The label line keeps its height even when empty.
- **Day states:**
  - **Past,** including days before the campaign began:
    - `post-rule` outline and the number in `post-past`;
    - struck through by a 3px `post-outline` line, 150px long and centred. It is rotated −40° in CSS (`rotate(-40deg)`), so it rises to the right, and the cell clips it.
  - **Today:** series-colour fill and outline, with the number and "Today" in `on-background`.
  - **Upcoming:** `post-outline` outline and the number in `on-surface`.
  - **Deadline:**
    - a 3px series-colour outline;
    - the number in the series colour;
    - "Deadline" in `on-surface`, because the series colour falls short of 4.5:1 at this size (see Contrast). The 2026 template used the series colour.

    On the deadline day itself, the cell takes the Today fill and reads "Last day".
- **Do:** label today and the deadline in words as well as colour.
- **Don't:** show more than two weeks, or use it for dates without a deadline.

### DayBars

A bar chart of days left, one bar per day of the campaign, each bar as tall as the days it had left. It is the timeline on story posts.

- **Consumer provides:** the campaign's dates (up to nine), their weekdays, and which one is today.
- **Panel:**
  - Box: `post-panel` fill, 2px `border` and `radius-panel`, padding 40px, 28px between the header and the bars.
  - Header: `mono` at 22px in `post-muted`, a code-flavoured label on the left ("cfp.days_left()") and the range on the right ("24 Oct → 1 Nov").
- **Bars:**
  - Layout: equal widths, 12px apart, bottoms aligned.
  - Height: 12px plus 32px per day left.
  - Shape: corners 8px at the top and 3px at the bottom, with a 3px outline.
- **Day states:**
  - Days gone: `post-bar-past` fill.
  - Today: series-colour fill, with a "Today" pill above it (`post-caption` at 700 in `on-background`).
  - Days to come: transparent, with a `post-bar-outline` outline.
- **Labels:**
  - Above each bar: the days left, `mono` at 24px and 700, in `post-muted` (series colour for today).
  - Below each bar: the weekday and date at 20px, in `post-muted` (`on-surface` at 700 for today).
- **Don't:** use it for more than nine days.

### Footer

The deadline and link along the bottom of square posts, below a divider.

- **Consumer provides:** the deadline ("1st November 2026, 23:59 IST") and the link (`cfp.scipy.in/scipy-india-2026`).
- **Box:** a 2px `post-rule` line on top, then 26px of padding above a row. The row puts its two items at either end, vertically centred, at least 24px apart.
- **Left:** a 28px clock icon in `post-muted` (2px stroke), 14px from the text. The text is "Closes **1st November 2026, 23:59 IST**" in `post-footer` (22px on 1.3) and `post-text`, with the bold part at 700 in `on-surface`.
- **Right:** the link in `post-footer` at 700, in the series colour, with a 28px right arrow (2.5px stroke) 10px after it.
- **Don't:** add a call-to-action pill as well; the link is the call to action on square posts.

### Button

Four buttons cover every case. On the website, solid and outline for actions and a pill for small extras; on graphics, the call-to-action pill.

- **Consumer provides:** a verb-first label in sentence case ("Submit your proposal", "Add to calendar") and a link or action.
- **Website buttons.** Solid and outline share their shape:
  - Type and padding: `body` size at 400 on 1.5, padding 5px 12px 7px.
  - Shape: a 1px border and `radius-sm`.
  - Focus: a 3px outline in the button's colour, 2px out.
- **Solid (website).** For the main action on a page ("Submit your proposal", "Buy your tickets").
  - At rest: `primary` fill and border, `primary-text` text.
  - Hover: `primary-highlight` fill.
- **Outline (website).** For secondary links ("Past editions").
  - At rest: transparent, with `secondary` border and text.
  - Hover: `secondary` fill with `secondary-text`.
- **Pill (website).** For small extras ("+ Add to calendar").
  - At rest: transparent, with a 1px `border` and `text-base` in `small` (14.4px on 1.65).
  - Shape: `radius-pill`, padding 6.4px 14.4px.
  - Hover and open: border and text in `primary`.
- **Call-to-action (graphics).** The series colour as fill, with `on-background` text in `post-cta` at 700, then a right arrow (2.75px stroke). One per graphic.

  | Format | Text | Padding | Arrow | Gap |
  | --- | --- | --- | --- | --- |
  | Portrait | 30px | 22px 40px | 32px | 14px |
  | Story | 32px | 26px 40px | 34px | 14px |
  | Banner | 22px | 16px 28px | 24px | 10px |

- **Do:** use a real link or button element on the website; keep hit areas at least 44px tall on touch screens.
- **Don't:** put two call-to-action pills in one graphic, or use `accent` for website buttons.

### Card

A bordered block on the website that introduces one topic and links onward, like "Call for proposals (CFP)" or "Sponsor us".

- **Consumer provides:** a short title, two or three sentences, and a link to the page it introduces.
- **Box:** transparent fill, 1px `border`, `radius-sm` and padding `space-4`. The shadow is `shadow-card` in light and `shadow-card-dark` in dark.
- **Text:** the title in `text-base` at 16px weight 700; the body in `text-base`, `body` size (16px on 1.65).
- **Link:** a solid or outline Button, or a plain `link`.
- **Do:** lay cards in a grid of two or three with equal heights; make the whole card clickable when it leads to one page.
- **Don't:** nest cards, add coloured side borders, or use cards on graphics (use a panel with `radius-panel` there).

### AnnouncementBand

The full-width band above the website header that announces the current edition.

- **Consumer provides:** one sentence about the edition and one link to its website.
- **Style:**
  - Fill and text: `secondary-bg` with centred `text-base` text in `body` (16px on 1.65).
  - Link: `link-higher-contrast`, underlined.
  - Size: 8px (`space-2`) vertical padding and at least 48px tall.
- **Do:** keep it to one sentence that fits two lines on a phone.
- **Don't:** stack more than one band, or use it for anything but the current edition or an urgent notice.

## Logo file

- `scipy-india-logo.svg` — The SciPy mark used by SciPy India: a `scipy-blue` disc with a white snake. Full colour and fixed; never recolour it. Reads on `background`, `surface`, `secondary-bg` and `post-banner` in both themes. Keep a quarter of the disc's diameter clear around it.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="560" height="560" viewBox="0 0 560 560">
<defs><clipPath id="c"><circle cx="280.01196" cy="279.8804" r="252.57939"/></clipPath></defs>
<path fill="#0054a6" d="M 280.01172 27.300781 A 252.57939 252.57939 0 0 0 27.431641 279.88086 A 252.57939 252.57939 0 0 0 57.744141 399.76562 C 59.195235 400.10468 60.587492 400.65816 61.941406 401.28125 C 66.840219 403.53575 71.468686 406.79445 74.214844 411.43555 C 75.587922 413.75609 76.458133 416.39575 76.568359 419.08984 C 76.677567 421.75902 76.009142 424.47294 74.560547 426.7168 A 252.57939 252.57939 0 0 0 280.01172 532.45898 A 252.57939 252.57939 0 0 0 532.5918 279.88086 A 252.57939 252.57939 0 0 0 280.01172 27.300781 z"/>
<path fill="#0054a6" fill-rule="evenodd" d="m 513.56686,184.93081 12.891,-5.996 8.711,-23.809 9.141,3.203 -7.852,21.289 21.758,7.5 -3.281,8.916 -24.297,-8.486 -13.398,6.162"/>
<path fill="#ffffff" fill-rule="evenodd" clip-path="url(#c)" d="m 373.90992,313.03486 c -17.39799,-23.797 -51.77696,-37.63286 -81.2681,-44.12822 -29.49115,-6.49535 -47.44014,-11.51901 -61.77612,-19.27626 -16.36281,-8.85397 -29.22641,-34.96222 -24.20294,-57.598 7.88381,-35.52446 39.61017,-61.08652 75.84117,-56.02752 18.094,2.559 33.438,12.139 43.55499,25.625 l 40.117,52.705 c 22.93,29.531 48.71101,38.32 76.758,24.375 l 13.64756,-6.45002 c 1.133,-0.527 2.50681,-1.59041 4.73081,-0.88308 2.224,0.70733 3.31502,2.62611 4.56297,4.87011 1.24794,2.244 2.56705,4.31231 4.91495,4.87732 2.34789,0.56501 5.6182,0.177 7.14707,-1.28038 10.39551,-9.90944 31.48264,-30.08895 31.48264,-30.08895 5.703,-4.883 4.023,-9.365 4.023,-9.365 l -7.852,-17.881 c 0,0 -2.148,-4.287 -9.57,-3.301 l -43.672,4.014 c -2.539,0.361 -4.805,2.051 -5.781,4.629 -0.586,1.504 -0.625,3.076 -0.195,4.502 l 1.563,5.029 c 0.313,1.045 0.313,2.217 -0.117,3.291 -0.508,1.328 -1.523,2.266 -2.734,2.764 l -12.344,5.225 c -14.22674,4.82612 -27.617,2.734 -37.422,-9.258 l -11.211,-14.893 -31.914,-42.354 c -15.156,-20.098 -38.00799,-34.434 -64.99999,-38.203 -54.043,-7.568 -104.199,29.854 -112.051,83.584 -3.965,27.08 -0.23964,49.98277 20.21927,73.38016 20.45892,23.39738 60.24695,32.31062 94.71373,40.20984 3.688,0.875 14.063,3.438 20.203,5.656 5.676,2.055 18.74999,6.875 29.37499,15.57 v 0 c 12.695,12.906 19.414,31.344 16.563,50.68 -4.805,32.969 -35.586,55.938 -68.74999,51.289 -16.611,-2.305 -30.635,-11.109 -39.922,-23.438 l -38.32,-50.859 c -7.813,-10.367 -19.629,-17.773 -33.594,-19.766 -13.945,-1.953 -27.441,1.914 -37.9,9.75 l -80.043417,59.73605 c 3.392949,9.65154 7.686724,19.24315 16.84366,27.03872 l 82.523757,-61.87477 c 3.779,-2.578 8.467,-3.75 13.33,-3.086 5.176,0.742 9.58,3.461 12.471,7.305 l 40.537,54.477 c 14.277,17.516 35.02,29.922 59.307,33.336 51.09399,7.148 98.51599,-28.242 105.93799,-79.063 3.436,-23.649 -2.345,-46.485 -14.728,-64.844"/>
</svg>
```
