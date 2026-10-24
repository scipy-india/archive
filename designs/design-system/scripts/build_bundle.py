"""Generate scipy-india-design-spec.md, the whole spec in one file to hand to Claude. Run from anywhere: python3 scripts/build_bundle.py"""
import json
import re
import runpy
from pathlib import Path

root = Path(__file__).resolve().parent.parent
project = root / 'project'

# Refresh the CSS first so the bundle always carries the current variables.
runpy.run_path(str(root / 'scripts/build_css.py'))

COMPONENTS = ['Lockup', 'EventLine', 'Tag', 'FlipClock', 'ProgressStrip', 'CountdownCalendar', 'DayBars', 'Footer', 'Button', 'Card', 'AnnouncementBand']


def demote(text, levels):
    return re.sub(r'^(#+) ', lambda m: '#' * (len(m.group(1)) + levels) + ' ', text, flags=re.M).strip()


def table(header, rows):
    lines = ['| ' + ' | '.join(header) + ' |', '|' + ' --- |' * len(header)]
    lines += ['| ' + ' | '.join(str(c).replace('|', '\\|') for c in row) + ' |' for row in rows]
    return '\n'.join(lines)


def colour(v, theme):
    if isinstance(v, dict):
        v = v[theme]
    m = re.fullmatch(r'\{([a-z-]+)\}', v)
    return f'same as `{m.group(1)}`' if m else f'`{v}`'


t = json.loads((project / 'tokens.json').read_text())
blocks = [(root / 'scripts/bundle_intro.md').read_text().strip()]

blocks += ['## Brand book', demote((project / 'README.md').read_text(), 1)]

blocks += ['## Tokens', '### Colour', table(
    ['Token', 'Light', 'Dark', 'Use'],
    [[f'`{x["name"]}`', colour(x['value'], 'light'), colour(x['value'], 'dark'), x['usage']] for x in t['color']['tokens']])]
blocks += ['### Type families', table(['Family', 'Stack'], [[f'`{k}`', f'`{v}`'] for k, v in t['type']['families'].items()])]
for g in t['type']['groups']:
    blocks.append(f'### Type: {g["name"]} (`{g["family"]}`)')
    if g.get('note'):
        blocks.append(g['note'])
    blocks.append(table(
        ['Style', 'Size', 'Line height', 'Weight', 'Use'],
        [[f'`{s["name"]}`', s['fontSize'], s['lineHeight'], s['fontWeight'], s['usage']] for s in g['styles']]))
for key, title in (('spacing', 'Spacing'), ('radius', 'Radius'), ('shadow', 'Shadow')):
    blocks += [f'### {title}', t[key]['note'], table(
        ['Token', 'Value', 'Use'],
        [[f'`{x["name"]}`', f'`{x["value"]}`', x['usage']] for x in t[key]['tokens']])]

css = (root / 'css/scipy-india-tokens.css').read_text().strip()
blocks += ['## Tokens as CSS',
           'Paste this into any HTML graphic, and set `data-theme="light"` or `data-theme="dark"` on the root element. Without it, the block at the end follows the viewer\'s system setting, which suits the website but not a graphic.',
           '```css\n' + css + '\n```']

blocks.append('## Components')
blocks += [demote((project / 'components' / name / 'README.md').read_text(), 2) for name in COMPONENTS]

logo_note = re.sub(r'^# .*\n+', '', (project / 'assets/Logos/README.md').read_text()).strip()
svg = (project / 'assets/Logos/scipy-india-logo.svg').read_text().strip()
blocks += ['## Logo file', logo_note, '```svg\n' + svg + '\n```']

text = '\n\n'.join(blocks) + '\n'
(root / 'scipy-india-design-spec.md').write_text(text)
print(f'wrote scipy-india-design-spec.md ({len(text):,} characters, {len(text.splitlines())} lines)')
