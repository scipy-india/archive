"""Generate css/scipy-india-tokens.css from project/tokens.json. Run from the repo root: python3 scripts/build_css.py"""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
t = json.loads((root / 'project/tokens.json').read_text())


def val(v, theme):
    if isinstance(v, dict):
        v = v[theme]
    m = re.fullmatch(r'\{([a-z-]+)\}', v)
    return f'var(--{m.group(1)})' if m else v


light, dark, rest = [], [], []
for x in t['color']['tokens']:
    light.append(f'  --{x["name"]}: {val(x["value"], "light")};')
    if isinstance(x['value'], dict):
        dark.append(f'  --{x["name"]}: {val(x["value"], "dark")};')
for k, v in t['type']['families'].items():
    rest.append(f'  --font-{k}: {v};')
for g in ('spacing', 'radius', 'shadow'):
    for x in t[g]['tokens']:
        rest.append(f'  --{x["name"]}: {x["value"]};')
for g in t['type']['groups']:
    for s in g['styles']:
        rest.append(f'  --text-{s["name"]}-size: {s["fontSize"]};')
        rest.append(f'  --text-{s["name"]}-line-height: {s["lineHeight"]};')
        rest.append(f'  --text-{s["name"]}-weight: {s["fontWeight"]};')

css = f'''/* SciPy India design tokens, generated from project/tokens.json. Do not edit by hand.
   Light is the default; dark follows scipy.in's data-theme="dark" and the OS setting. */
:root {{
{chr(10).join(light + rest)}
}}
:root[data-theme="dark"] {{
{chr(10).join(dark)}
  --shadow-card: var(--shadow-card-dark);
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
{chr(10).join('  ' + l for l in dark)}
    --shadow-card: var(--shadow-card-dark);
  }}
}}
'''
(root / 'css').mkdir(exist_ok=True)
(root / 'css/scipy-india-tokens.css').write_text(css)
print('wrote css/scipy-india-tokens.css')
