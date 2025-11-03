# Convertisseur JPG vers PNG

Ce script permet de convertir automatiquement des images JPG/JPEG en format PNG tout en préservant leur qualité.

## Description

Le script effectue les opérations suivantes :
- Parcourt un dossier source contenant des images JPG/JPEG
- Convertit chaque image en format PNG
- Sauvegarde les nouvelles images dans un dossier distinct
- Gère automatiquement les images avec transparence
- Fournit un rapport détaillé des conversions

## Prérequis

- Python 3.x
- Bibliothèque Pillow (PIL)
  ```bash
  pip install Pillow
  ```
- Un dossier `images` contenant vos images JPG/JPEG

## Utilisation

1. Créez un dossier `images` dans le même répertoire que le script
2. Placez vos images JPG/JPEG dans le dossier `images`
3. Exécutez le script :
```bash
python3 jpg_to_png.py
```

## Structure des dossiers

### Dossier d'entrée : `images/`
- Contient les images source au format JPG/JPEG
- Les sous-dossiers ne sont pas traités

### Dossier de sortie : `images_png/`
- Créé automatiquement si nécessaire
- Contient les images converties au format PNG
- Conserve les noms de fichiers originaux (seule l'extension change)

### Exemple de conversion
```
Avant (dans images/) :
  photo.jpg
  image.jpeg

Après (dans images_png/) :
  photo.png
  image.png
```

## Fonctionnalités

- Conversion automatique JPG/JPEG → PNG
- Préservation de la qualité d'image
- Gestion des images avec canal alpha (RGBA)
- Rapport détaillé des conversions réussies/échouées
- Création automatique du dossier de destination

## Notes techniques
- Les images RGBA sont converties en RGB avec un fond blanc
- Les erreurs sont gérées individuellement (une erreur sur une image n'arrête pas le processus)
- Seuls les fichiers .jpg et .jpeg sont traités (insensible à la casse)