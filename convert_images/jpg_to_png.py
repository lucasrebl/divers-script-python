"""
Script de conversion d'images JPG vers PNG.
Utilise la bibliothèque Pillow pour convertir toutes les images JPG d'un dossier
en format PNG, en préservant la qualité d'image.
"""

from PIL import Image
import os
import sys

def convert_jpg_to_png(input_folder, output_folder):
    """
    Convertit toutes les images JPG d'un dossier en PNG et les enregistre dans un autre dossier.

    Args:
        input_folder (str): Chemin du dossier contenant les images JPG
        output_folder (str): Chemin du dossier où enregistrer les images PNG

    Returns:
        tuple: (nb_success, nb_errors) Nombre de conversions réussies et échouées
    """
    # Compteurs pour le suivi des opérations
    successful_conversions = 0
    failed_conversions = 0

    # Vérification de l'existence du dossier d'entrée
    if not os.path.exists(input_folder):
        print(f"Erreur : Le dossier source '{input_folder}' n'existe pas.")
        return successful_conversions, failed_conversions

    # Création du dossier de sortie s'il n'existe pas
    try:
        os.makedirs(output_folder, exist_ok=True)
    except OSError as e:
        print(f"Erreur lors de la création du dossier de sortie : {e}")
        return successful_conversions, failed_conversions

    # Parcours des fichiers du dossier d'entrée
    for file_name in os.listdir(input_folder):
        # Vérification de l'extension (jpg ou jpeg, insensible à la casse)
        if file_name.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, file_name)
            png_file_name = os.path.splitext(file_name)[0] + ".png"
            output_path = os.path.join(output_folder, png_file_name)

            try:
                # Ouverture et conversion de l'image
                with Image.open(input_path) as img:
                    # Conversion en RGB si nécessaire (pour gérer les images RGBA)
                    if img.mode in ('RGBA', 'LA'):
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, mask=img.split()[-1])
                        img = background
                    
                    # Sauvegarde en PNG
                    img.save(output_path, "PNG")
                    print(f"Converti : {file_name} -> {png_file_name}")
                    successful_conversions += 1

            except Exception as e:
                print(f"Erreur lors de la conversion de {file_name} : {e}")
                failed_conversions += 1

    return successful_conversions, failed_conversions

def main():
    """
    Fonction principale qui gère les paramètres et lance la conversion.
    """
    # Dossiers par défaut
    input_folder = "./images"
    output_folder = "./images_png"

    # Lancement de la conversion
    print(f"\nDébut de la conversion JPG -> PNG")
    print(f"Dossier source : {input_folder}")
    print(f"Dossier destination : {output_folder}")
    
    success, failed = convert_jpg_to_png(input_folder, output_folder)
    
    # Affichage du résumé
    print(f"\nRésumé de la conversion :")
    print(f"✓ Conversions réussies : {success}")
    if failed > 0:
        print(f"✗ Conversions échouées : {failed}")
    
    if success == 0 and failed == 0:
        print("\nAucun fichier JPG trouvé dans le dossier source.")
        print("Note : Seuls les fichiers .jpg et .jpeg sont traités.")

if __name__ == "__main__":
    main()
