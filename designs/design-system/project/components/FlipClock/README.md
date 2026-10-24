# FlipClock

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
