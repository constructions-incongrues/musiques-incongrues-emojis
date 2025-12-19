# Tronches Incongrues

Générateur de fichiers JSON flamoji et YAML RocketChat pour collections d'emojis personnalisés.

## Structure

```
emojis/
  collections/
    collection-name/
      emoji1.png
      emoji2.gif
      flamoji.json       (généré automatiquement)
      rocketchat.yaml    (généré automatiquement)
```

## Utilisation locale

### Prérequis

```bash
pip install -r requirements.txt
```

### Générer les fichiers JSON et YAML

```bash
# Avec l'URL de base par défaut (/assets/emojis)
python3 generate_flamoji.py

# Avec une URL de base personnalisée
python3 generate_flamoji.py --base-url "https://example.com/emojis"
```

Le script génère automatiquement deux fichiers pour chaque collection :
- `flamoji.json` - Format pour Flamoji
- `rocketchat.yaml` - Format compatible avec RocketChat/emojipacks

### Formats supportés

Le script supporte les formats d'images suivants :
- PNG (`.png`)
- JPEG (`.jpg`, `.jpeg`)
- GIF (`.gif`)

## Configuration GitHub Actions

Le workflow génère automatiquement les fichiers `flamoji.json` et `rocketchat.yaml` à chaque push sur la branche `main`.

### Configurer l'URL de base

1. Aller dans **Settings** → **Secrets and variables** → **Actions** → **Variables**
2. Créer une nouvelle variable nommée `FLAMOJI_BASE_URL`
3. Définir la valeur (par exemple : `https://musiques-incongrues.net/emojis`)

Si la variable n'est pas définie, l'URL par défaut `/assets/emojis` sera utilisée.

### Déclencher manuellement

Le workflow peut aussi être déclenché manuellement depuis l'onglet **Actions** → **Generate Flamoji JSON and RocketChat YAML** → **Run workflow**.

## Formats générés

### Format JSON (flamoji.json)

Chaque fichier `flamoji.json` suit le format :

```json
{
  "0": {
    "title": "collection-name_emoji1",
    "text_to_replace": ":collection-name_emoji1:",
    "path": "/assets/emojis/collection-name/emoji1.png"
  },
  "1": {
    "title": "collection-name_emoji2",
    "text_to_replace": ":collection-name_emoji2:",
    "path": "/assets/emojis/collection-name/emoji2.gif"
  }
}
```

Format basé sur [BittyKitty flamoji](https://github.com/zerosonesfun/BittyKitty/blob/main/dist/icons/flamoji/flamoji.json).

### Format YAML (rocketchat.yaml)

Chaque fichier `rocketchat.yaml` suit le format [emojipacks](https://github.com/lambtron/emojipacks) :

```yaml
title: collection-name
emojis:
- name: emoji1
  src: /assets/emojis/collection-name/emoji1.png
- name: emoji2
  src: /assets/emojis/collection-name/emoji2.gif
```
