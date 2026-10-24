# CountdownCalendar

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
