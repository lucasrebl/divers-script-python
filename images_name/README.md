# Script de Renommage d'Images

Ce script permet de nettoyer automatiquement les noms de fichiers images en supprimant le préfixe "asset " des fichiers PNG.

## Description

Le script parcourt un dossier d'images et :
- Identifie tous les fichiers PNG commençant par "asset "
- Supprime ce préfixe du nom de fichier
- Conserve le reste du nom et l'extension
- Affiche un rapport des changements effectués

## Prérequis

- Python 3.x
- Un dossier `images` dans le même répertoire que le script

## Utilisation

1. Créez un dossier `images` dans le même répertoire que le script
2. Placez vos images PNG à renommer dans ce dossier
3. Exécutez le script :
```bash
python3 rename_images.py
```

## Structure des fichiers

### Dossier `images/`
- Doit contenir les fichiers PNG à renommer
- Les fichiers doivent commencer par "asset " pour être traités

### Exemple de renommage
```
Avant :
images/asset 1.png
images/asset photo.png

Après :
images/1.png
images/photo.png
```

## Note de sécurité
- Le script ne traite que les fichiers PNG
- Les fichiers originaux sont renommés (pas de copie de sauvegarde)
- Assurez-vous d'avoir une sauvegarde de vos fichiers avant d'exécuter le script