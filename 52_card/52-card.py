# Génère 52 fichiers SVG (As -> Roi pour les 4 couleurs) et un JSON contenant les images encodées en base64 (data URI).
import os, base64, json, textwrap
from pathlib import Path

# Use current directory instead of /mnt/data which requires root permissions
out_dir = Path("cards_svgs")
out_dir.mkdir(parents=True, exist_ok=True)

ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = [
    ("pique","♠","black"),
    ("coeur","♥","red"),
    ("carreau","♦","red"),
    ("trèfle","♣","black")
]

def svg_for_card(rank, suit_symbol, color):
    # Simple, clean SVG card: rounded rectangle, rank top-left, suit center large, rank bottom-right (rotated)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="600" viewBox="0 0 400 600">
  <defs>
    <style>
      .card{{fill:#fff;stroke:#000;stroke-width:3;rx:20;ry:20}}
      .rank{{font-family: "DejaVu Sans", "Arial", sans-serif; font-size:48px; font-weight:700; }}
      .suit{{font-family: "DejaVu Sans", "Arial", sans-serif; font-size:180px; }}
    </style>
  </defs>
  <rect x="2" y="2" width="396" height="596" rx="20" ry="20" class="card"/>
  <text x="26" y="70" class="rank" fill="{color}">{rank}</text>
  <text x="200" y="330" text-anchor="middle" dominant-baseline="middle" class="suit" fill="{color}">{suit_symbol}</text>
  <g transform="translate(374,530) rotate(180)">
    <text x="0" y="0" class="rank" fill="{color}">{rank}</text>
  </g>
</svg>'''
    return svg

# Generate files and build JSON with data URIs
cards_json = {}
for rank in ranks:
    for suit_name, suit_symbol, color in suits:
        filename = f"{rank}_{suit_name}.svg".replace("è","e").replace("ê","e").replace(" ","_")
        path = out_dir / filename
        svg = svg_for_card(rank, suit_symbol, color)
        path.write_text(svg, encoding="utf-8")
        # encode as data URI (base64)
        b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
        data_uri = f"data:image/svg+xml;base64,{b64}"
        key = f"{rank}_de_{suit_name}"
        cards_json[key] = {
            "rank": rank,
            "suit": suit_name,
            "filename": filename,
            "data_uri": data_uri
        }

# Save JSON
json_path = Path("cards_images.json")
json_path.write_text(json.dumps(cards_json, ensure_ascii=False, indent=2), encoding="utf-8")

print("Génération terminée.")
print("Fichiers créés:")
print(f"- Dossier SVG : {out_dir}")
print(f"- JSON (data URIs) : {json_path}")
