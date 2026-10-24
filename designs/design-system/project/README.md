SciPy India is an international scientific computing and open source software conference, held annually since 2009 and run by its community. This system covers everything that carries the SciPy India name: the website at scipy.in (built on the PyData Sphinx theme) and the conference's graphics, such as social posts, stories and banners. Colours, type and radii come straight from scipy.in's theme, so a graphic made with these tokens sits naturally next to the website. Post values come from the 2026 countdown templates, measured file by file.

## Voice and copy

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

## Colour

Two themes, matching scipy.in's light and dark modes. Graphics default to the light theme; every template also works in dark.

### Website

- **Grounds.** `background` for pages, `surface` for code blocks and tinted areas, `border` for card and pill outlines.
- **Text.** `text-base` for body, headings and card titles; `text-muted` for navigation, dates and metadata.
- **Teal, the brand colour.** `primary` marks what matters: links, solid buttons, the countdown tiles. Solid buttons put `primary-text` on `primary` and hover to `primary-highlight`.
- **Purple.** `secondary` is for outline buttons and link hover. `secondary-bg` is the announcement band at the top of scipy.in, with `text-base` text and `link-higher-contrast` links.
- **Status.** `info`, `success`, `warning` and `danger`, with their `-bg` tints, are for admonitions. Always pair them with a word or icon.

### Posts

- **Grounds.** `background` under a `post-grid`; panels in `post-panel` with a 2px `border`. The banner sits on `post-banner` under a `post-banner-grid`.
- **Text.** `on-surface` for the strongest words (wordmark, event line, headlines, key phrases); `post-text` for supporting lines; `post-muted` for small print. On the banner: `post-banner-heading`, `post-banner-text` and `post-banner-link`.
- **Series colour.** Each post series picks one colour for its tiles, icons, "today" markers and call-to-action pill: `primary` by default, `secondary` or `accent` as alternatives. Never mix them in one graphic. Text on the series colour is `on-background`.
- **Tag.** `secondary-bg` with `on-surface` text.
- **Timelines.** `post-rule` for elapsed days, `post-outline` for upcoming ones, `post-past` for crossed-out numbers; the story's day bars use `post-bar-past` and `post-bar-outline`.
- **SciPy blue.** `scipy-blue` belongs to the logo only. Don't use it for UI or text.

### Contrast

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

### Countdown tiles

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

## Type

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

## Layout, shape and depth

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

### Social formats

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

### Format recipes

Measured from the 2026 templates. In each recipe, the post is a column with `justify-content: space-between` inside its margins, and each numbered item is one direct child. Gaps inside an item are given.

#### Square (1080 × 1080)

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

#### Portrait (1080 × 1350)

1. **Header** as on square.
2. **Hero,** centred, 26px gap: the FlipClock days tiles, then one centred line at 46px, 600, on 1.15, in `on-surface`: "Days left" in the series colour, then "to submit your proposal".
3. **The CountdownCalendar.**
4. **Supporting line:** the "What we want" line at 30px on 1.35, full width, centred and balanced.
5. **Call-to-action pill,** centred: "Submit at cfp.scipy.in/scipy-india-2026".

**Last day:** the hero is a centred column with 24px gap: "Last day" in `post-display`, then the time row (144 × 200 tiles, dots 40px apart).

#### Story (1080 × 1920)

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

#### Banner (1200 × 675)

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

## Logo

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

## Icons

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

## Motion

The countdown on scipy.in flips each second (FlipDown). Graphics are static. Don't animate the logo.

## Accessibility

- **Contrast.** Text meets the pairs in Colour.
- **Hit areas.** Interactive elements on the website keep a 44px minimum.
- **Alt text.** Every published image has alt text, written as in Voice and copy.
- **Colour alone.** Never carries meaning on its own:
  - The calendar and the day bars say "Today" and "Deadline" in words.
  - The progress strip sets today's date in bold as well as colour.
