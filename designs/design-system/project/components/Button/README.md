# Button

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
