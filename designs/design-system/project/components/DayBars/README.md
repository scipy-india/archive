# DayBars

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
