
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = ROOT / "data" / "contributions.json"
OUTPUT_FILE = ROOT / "cards" / "contribution-graph.svg"

# Contribution colors
COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353"
]

CELL = 10
GAP = 3
STEP = CELL + GAP

LEFT = 35
TOP = 38

with DATA_FILE.open(encoding="utf-8") as file:
    data = json.load(file)

weeks = data["weeks"]
total = data["total_contributions"]

def get_level(count):
    if count == 0:
        return 0
    if count <= 3:
        return 1
    if count <= 6:
        return 2
    if count <= 9:
        return 3
    return 4

elements = []
months = []
previous_month = None

for week_index, week in enumerate(weeks):
    days = week["contributionDays"]

    for day_index, day in enumerate(days):
        count = day["contributionCount"]
        day_date = date.fromisoformat(day["date"])

        x = LEFT + week_index * STEP
        y = TOP + day_index * STEP

        level = get_level(count)
        color = COLORS[level]

        delay = min(
            (week_index * 7 + day_index) * 0.012,
            4.5
        )

        elements.append(
            f'''
            <rect x="{x}" y="{y}"
                  width="{CELL}" height="{CELL}"
                  rx="2.5" fill="{color}"
                  class="cell"
                  style="animation-delay:{delay:.3f}s">
                <title>{day["date"]}: {count} contributions</title>
            </rect>
            '''
        )

        if day_index == 0 and day_date.month != previous_month:
            months.append(
                f'<text x="{x}" y="25" class="month">'
                f'{day_date.strftime("%b")}</text>'
            )
            previous_month = day_date.month

width = LEFT + len(weeks) * STEP + 15
height = TOP + 7 * STEP + 30

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     width="100%" viewBox="0 0 {width} {height}">

<style>
    .title {{
        fill: #e6edf3;
        font-size: 17px;
        font-weight: bold;
        font-family: Arial, sans-serif;
    }}

    .month {{
        fill: #8b949e;
        font-size: 10px;
        font-family: Arial, sans-serif;
    }}

    .cell {{
        opacity: 0;
        animation: appear 0.7s ease forwards;
        transform-box: fill-box;
        transform-origin: center;
    }}

    @keyframes appear {{
        from {{
            opacity: 0;
            transform: scale(0.4);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
</style>

<rect width="100%" height="100%" rx="12"
      fill="#0d1117"/>

<text x="{LEFT}" y="15" class="title">
    {total} Contributions
</text>

{''.join(months)}
{''.join(elements)}

</svg>'''

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(svg, encoding="utf-8")

print("Animated contribution graph created!")
print("Total contributions:", total)
print("Saved at:", OUTPUT_FILE)
