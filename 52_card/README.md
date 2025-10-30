# Générateur de Cartes à Jouer SVG

Ce script génère un jeu complet de 52 cartes à jouer en format SVG.

## Description

Le script crée :
- 52 fichiers SVG (un pour chaque carte, de l'As au Roi dans les 4 couleurs)
- Un fichier JSON contenant les images encodées en base64 (data URI)

Les cartes sont générées avec un design simple et élégant :
- Rectangle arrondi blanc avec bordure noire
- Valeur en haut à gauche et en bas à droite (inversée)
- Symbole de la couleur au centre
- Couleurs rouge pour les cœurs et les carreaux, noire pour les piques et les trèfles

## Prérequis

- Python 3.x

## Utilisation

```bash
python3 52-card.py
```

## Structure des fichiers générés

### Dossier `cards_svgs/`
Contient les 52 fichiers SVG nommés selon le format : `[VALEUR]_[COULEUR].svg`
Exemple : `A_pique.svg`, `10_coeur.svg`, etc.

### Fichier `cards_images.json`
Contient un objet JSON avec :
- Clés au format : `[VALEUR]_de_[COULEUR]`
- Valeurs contenant :
  - rank : valeur de la carte
  - suit : couleur de la carte
  - filename : nom du fichier SVG
  - data_uri : image SVG encodée en base64 (data URI)