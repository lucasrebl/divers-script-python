# Importation des modules nécessaires pour la gestion des fichiers, l'encodage Base64 et la création du JSON
import os, base64, json
from pathlib import Path

# Création du dossier de sortie 'cards_svgs' pour stocker les fichiers SVG générés
out_dir = Path("cards_svgs")
out_dir.mkdir(parents=True, exist_ok=True)

# Définition des valeurs possibles des cartes (As → Roi)
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

# Définition des 4 couleurs avec leur symbole et leur couleur d’affichage
suits = [
    ("pique","♠","black"),
    ("coeur","♥","red"),
    ("carreau","♦","red"),
    ("trèfle","♣","black")
]

# Fonction qui génère le contenu SVG pour une carte donnée (valeur, symbole et couleur)
def svg_for_card(rank, suit_symbol, color):
    # Création du SVG avec le fond, les textes (valeurs) et le symbole centré
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

# Initialisation du dictionnaire qui contiendra toutes les cartes et leurs informations encodées
cards_json = {}

# Boucle principale : génération des 52 fichiers SVG et encodage en base64 dans le JSON
for rank in ranks:
    for suit_name, suit_symbol, color in suits:
        # Création du nom de fichier propre et suppression des caractères accentués
        filename = f"{rank}_{suit_name}.svg".replace("è","e").replace("ê","e").replace(" ","_")
        path = out_dir / filename

        # Génération du contenu SVG pour la carte
        svg = svg_for_card(rank, suit_symbol, color)

        # Écriture du fichier SVG sur le disque
        path.write_text(svg, encoding="utf-8")

        # Encodage du SVG en base64 pour créer une data URI réutilisable directement dans le JSON
        b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
        data_uri = f"data:image/svg+xml;base64,{b64}"

        # Création de la clé et ajout de la carte dans le dictionnaire JSON
        key = f"{rank}_de_{suit_name}"
        cards_json[key] = {
            "rank": rank,
            "suit": suit_name,
            "filename": filename,
            "data_uri": data_uri
        }

# Sauvegarde du dictionnaire complet dans un fichier JSON formaté et encodé en UTF-8
json_path = Path("cards_images.json")
json_path.write_text(json.dumps(cards_json, ensure_ascii=False, indent=2), encoding="utf-8")

# Affichage d’un message de confirmation avec les chemins des fichiers générés
print("Génération terminée.")
print("Fichiers créés:")
print(f"- Dossier SVG : {out_dir}")
print(f"- JSON (data URIs) : {json_path}")
