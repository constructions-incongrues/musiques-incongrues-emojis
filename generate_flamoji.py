#!/usr/bin/env python3
"""
Génère des fichiers JSON flamoji pour chaque collection d'emojis.
Format basé sur https://github.com/zerosonesfun/BittyKitty/blob/main/dist/icons/flamoji/flamoji.json
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List


def get_collections_dir() -> Path:
    """Retourne le chemin vers le répertoire des collections."""
    return Path(__file__).parent / "collections"


def get_emoji_files(collection_path: Path) -> List[Path]:
    """Récupère tous les fichiers d'images (PNG, JPG, GIF) d'une collection."""
    emoji_files = []
    for extension in ["*.png", "*.jpg", "*.jpeg", "*.gif"]:
        emoji_files.extend(collection_path.glob(extension))
    return sorted(emoji_files)


def create_shortcode(collection_name: str, emoji_filename: str) -> str:
    """Crée un shortcode pour l'emoji.

    Args:
        collection_name: Nom de la collection
        emoji_filename: Nom du fichier (avec extension)

    Returns:
        Shortcode au format :filename:
    """
    # Retire l'extension du fichier
    name = Path(emoji_filename).stem
    return f":{name}:"


def create_title(collection_name: str, emoji_filename: str) -> str:
    """Crée un titre lisible pour l'emoji.

    Args:
        collection_name: Nom de la collection
        emoji_filename: Nom du fichier (avec extension)

    Returns:
        Titre formaté
    """
    # Retire l'extension du fichier
    name = Path(emoji_filename).stem
    # Capitalise le nom de la collection
    collection_title = collection_name.capitalize()
    return f"{collection_title} : {name}"


def generate_flamoji_json(collection_name: str, collection_path: Path, base_url: str = "/assets/emojis") -> Dict:
    """Génère le contenu JSON flamoji pour une collection.

    Args:
        collection_name: Nom de la collection
        collection_path: Chemin vers la collection
        base_url: URL de base pour les paths (par défaut: /assets/emojis)

    Returns:
        Dictionnaire au format flamoji
    """
    emoji_files = get_emoji_files(collection_path)
    flamoji_data = {}

    for index, emoji_file in enumerate(emoji_files):
        filename = emoji_file.name

        flamoji_data[str(index)] = {
            "title": create_title(collection_name, filename),
            "text_to_replace": create_shortcode(collection_name, filename),
            "path": f"{base_url}/{collection_name}/{filename}"
        }

    return flamoji_data


def main():
    """Fonction principale."""
    # Parser les arguments
    parser = argparse.ArgumentParser(
        description="Génère des fichiers JSON flamoji pour chaque collection d'emojis"
    )
    parser.add_argument(
        "--base-url",
        default="/assets/emojis",
        help="URL de base pour les paths des emojis (défaut: /assets/emojis)"
    )
    args = parser.parse_args()

    collections_dir = get_collections_dir()

    if not collections_dir.exists():
        print(f"Erreur: Le répertoire {collections_dir} n'existe pas.")
        return

    print(f"URL de base: {args.base_url}\n")

    # Parcourir chaque collection
    for collection_path in sorted(collections_dir.iterdir()):
        if not collection_path.is_dir():
            continue

        collection_name = collection_path.name
        print(f"Traitement de la collection: {collection_name}")

        # Générer le JSON flamoji
        flamoji_data = generate_flamoji_json(collection_name, collection_path, args.base_url)

        if not flamoji_data:
            print(f"  ⚠️  Aucun emoji trouvé dans {collection_name}")
            continue

        # Sauvegarder le fichier JSON dans le dossier de la collection
        output_file = collection_path / "flamoji.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(flamoji_data, f, indent=2, ensure_ascii=False)

        print(f"  ✓ Généré: {output_file} ({len(flamoji_data)} emojis)")

    print(f"\n✓ Fichiers générés dans chaque collection")


if __name__ == "__main__":
    main()
