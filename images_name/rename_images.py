"""
Script de renommage automatique des fichiers images.
Ce script supprime le préfixe 'asset ' des noms de fichiers PNG dans un dossier spécifié.
Utile pour nettoyer les noms de fichiers après export depuis certains logiciels.
"""

import os

def main():
    # Définition du chemin du dossier contenant les images
    # Le dossier doit être situé dans le même répertoire que le script
    image_folder = "./images/"

    # Vérification de l'existence du dossier
    if not os.path.exists(image_folder):
        print(f"Erreur : Le dossier {image_folder} n'existe pas.")
        print("Créez d'abord un dossier 'images' dans le même répertoire que ce script.")
        return

    # Compteur pour le suivi des fichiers traités
    files_renamed = 0

    # Parcours de tous les fichiers dans le dossier
    for filename in os.listdir(image_folder):
        # Filtre uniquement les fichiers PNG commençant par "asset"
        if filename.startswith("asset") and filename.endswith(".png"):
            # Création du nouveau nom en supprimant "asset "
            new_name = filename.replace("asset ", "")
            
            # Construction des chemins complets pour le renommage
            old_path = os.path.join(image_folder, filename)
            new_path = os.path.join(image_folder, new_name)
            
            try:
                # Tentative de renommage du fichier
                os.rename(old_path, new_path)
                print(f"Renommé : {filename} -> {new_name}")
                files_renamed += 1
            except OSError as e:
                print(f"Erreur lors du renommage de {filename} : {e}")

    # Affichage du résumé des opérations
    if files_renamed > 0:
        print(f"\nRenommage terminé ! {files_renamed} fichier(s) traité(s).")
    else:
        print("\nAucun fichier à renommer trouvé.")
        print("Note : Seuls les fichiers PNG commençant par 'asset ' sont traités.")

if __name__ == "__main__":
    main()
