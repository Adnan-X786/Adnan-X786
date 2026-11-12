
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "cards"
OUTPUT.mkdir(exist_ok=True)

cards = [
    {
        "file": "build.svg",
        "title": "BUILD",
        "subtitle": "Turning ideas into projects",
        "tag": "PYTHON  •  C++  •  CODE",
        "color": "#00D9FF",
        "number": "01"
    },
    {
        "file": "ai.svg",
        "title": "EXPLORE AI",
        "subtitle": "Learning artificial intelligence",
        "tag": "AI  •  MACHINE LEARNING",
        "color": "#A78BFA",
        "number": "02"
    },
    {
        "file": "learn.svg",
        "title": "KEEP LEARNING",
        "subtitle": "Growing one project at a time",
        "tag": "LEARN  •  CREATE  •  REPEAT",
        "color": "#FBBF24",
        "number": "03"
    }
]

template = """<svg xmlns="http://www.w3.org/2000/svg"
width="460" height="180" viewBox="0 0 460 180">

<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#111827"/>
    <stop offset="100%" stop-color="#080D18"/>
  </linearGradient>

  <linearGradient id="shine">
    <stop offset="0%" stop-color="COLOR" stop-opacity="0"/>
    <stop offset="50%" stop-color="COLOR" stop-opacity=".8"/>
    <stop offset="100%" stop-color="COLOR" stop-opacity="0"/>
  </linearGradient>

  <style>
    .card {{
      animation: appear .9s ease-out both;
    }}
    .title {{
      animation: slide 1s ease-out both;
    }}
    .glow {{
      animation: pulse 2.5s ease-in-out infinite;
    }}
    .shine {{
      animation: sweep 4s ease-in-out infinite;
    }}
    @keyframes appear {{
      from {{ opacity: 0; transform: translateY(18px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes slide {{
      from {{ opacity: 0; letter-spacing: 8px; }}
      to {{ opacity: 1; letter-spacing: 2px; }}
    }}
    @keyframes pulse {{
      50% {{ opacity: .35; }}
    }}
    @keyframes sweep {{
      0%, 65% {{ transform: translateX(-500px); }}
      100% {{ transform: translateX(500px); }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; }}
    }}
  </style>
</defs>

<g class="card">
  <rect x="2" y="2" width="456" height="176"
        rx="18" fill="url(#bg)"
        stroke="COLOR" stroke-opacity=".65"/>

  <circle class="glow" cx="405" cy="35" r="32"
          fill="COLOR" opacity=".18"/>

  <rect class="shine" x="0" y="0" width="90"
        height="180" fill="url(#shine)" opacity=".25"/>

  <text x="28" y="35" fill="COLOR"
        font-size="12" font-family="monospace"
        letter-spacing="3">ADNAN / PORTFOLIO</text>

  <text class="title" x="28" y="91"
        fill="#FFFFFF" font-size="34"
        font-weight="bold" font-family="Arial">
        TITLE
  </text>

  <text x="28" y="120" fill="#CBD5E1"
        font-size="14" font-family="Arial">
        SUBTITLE
  </text>

  <text x="28" y="153" fill="COLOR"
        font-size="11" font-family="monospace">
        TAG
  </text>

  <text x="425" y="155" fill="#64748B"
        font-size="13" text-anchor="end"
        font-family="monospace">#NUMBER</text>
</g>
</svg>
"""

for card in cards:
    svg = template.replace("COLOR", card["color"])
    svg = svg.replace("TITLE", card["title"])
    svg = svg.replace("SUBTITLE", card["subtitle"])
    svg = svg.replace("TAG", card["tag"])
    svg = svg.replace("NUMBER", card["number"])

    (OUTPUT / card["file"]).write_text(svg, encoding="utf-8")

print("Success! 3 animated SVG cards created.")
print("Check your cards folder.")
