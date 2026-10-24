# ProgressStrip

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
