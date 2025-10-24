#!/usr/bin/env python3
"""
Génère des fichiers JSON flamoji et YAML RocketChat pour chaque collection d'emojis.
Format JSON basé sur https://github.com/zerosonesfun/BittyKitty/blob/main/dist/icons/flamoji/flamoji.json
Format YAML basé sur https://github.com/lambtron/emojipacks
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List
import yaml


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
        Shortcode au format :collection-name_filename:
    """
    # Retire l'extension du fichier
    name = Path(emoji_filename).stem
    return f":{collection_name}_{name}:"


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
    return f"{name}"


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


def generate_rocketchat_yaml(collection_name: str, collection_path: Path, base_url: str = "/assets/emojis") -> Dict:
    """Génère le contenu YAML RocketChat pour une collection.

    Args:
        collection_name: Nom de la collection
        collection_path: Chemin vers la collection
        base_url: URL de base pour les paths (par défaut: /assets/emojis)

    Returns:
        Dictionnaire au format emojipacks pour RocketChat
    """
    emoji_files = get_emoji_files(collection_path)
    emojis = []

    for emoji_file in emoji_files:
        filename = emoji_file.name
        name = Path(filename).stem

        emojis.append({
            "name": name,
            "src": f"{base_url}/{collection_name}/{filename}"
        })

    return {
        "title": collection_name,
        "emojis": emojis
    }


def main():
    """Fonction principale."""
    # Parser les arguments
    parser = argparse.ArgumentParser(
        description="Génère des fichiers JSON flamoji et YAML RocketChat pour chaque collection d'emojis"
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
        json_output_file = collection_path / "flamoji.json"
        with open(json_output_file, "w", encoding="utf-8") as f:
            json.dump(flamoji_data, f, indent=2, ensure_ascii=False)

        print(f"  ✓ Généré: {json_output_file} ({len(flamoji_data)} emojis)")

        # Générer le YAML RocketChat
        rocketchat_data = generate_rocketchat_yaml(collection_name, collection_path, args.base_url)

        # Sauvegarder le fichier YAML dans le dossier de la collection
        yaml_output_file = collection_path / "rocketchat.yaml"
        with open(yaml_output_file, "w", encoding="utf-8") as f:
            yaml.dump(rocketchat_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        print(f"  ✓ Généré: {yaml_output_file} ({len(rocketchat_data['emojis'])} emojis)")

    print(f"\n✓ Fichiers JSON et YAML générés dans chaque collection")


if __name__ == "__main__":
    main()
