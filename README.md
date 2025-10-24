# Musiques Incongrues Emojis

Générateur de fichiers JSON flamoji pour collections d'emojis personnalisés.

## Structure

```
emojis/
  collections/
    collection-name/
      emoji1.png
      emoji2.gif
      flamoji.json  (généré automatiquement)
```

## Utilisation locale

### Générer les fichiers JSON

```bash
# Avec l'URL de base par défaut (/assets/emojis)
python3 generate_flamoji.py

# Avec une URL de base personnalisée
python3 generate_flamoji.py --base-url "https://example.com/emojis"
```

### Formats supportés

Le script supporte les formats d'images suivants :
- PNG (`.png`)
- JPEG (`.jpg`, `.jpeg`)
- GIF (`.gif`)

## Configuration GitHub Actions

Le workflow génère automatiquement les fichiers `flamoji.json` à chaque push sur la branche `main`.

### Configurer l'URL de base

1. Aller dans **Settings** → **Secrets and variables** → **Actions** → **Variables**
2. Créer une nouvelle variable nommée `FLAMOJI_BASE_URL`
3. Définir la valeur (par exemple : `https://musiques-incongrues.net/emojis`)

Si la variable n'est pas définie, l'URL par défaut `/assets/emojis` sera utilisée.

### Déclencher manuellement

Le workflow peut aussi être déclenché manuellement depuis l'onglet **Actions** → **Generate Flamoji JSON** → **Run workflow**.

## Format du JSON généré

Chaque fichier `flamoji.json` suit le format :

```json
{
  "0": {
    "title": "Collection emoji1",
    "text_to_replace": ":emoji1:",
    "path": "/assets/emojis/collection-name/emoji1.png"
  },
  "1": {
    "title": "Collection emoji2",
    "text_to_replace": ":emoji2:",
    "path": "/assets/emojis/collection-name/emoji2.gif"
  }
}
```

Format basé sur [BittyKitty flamoji](https://github.com/zerosonesfun/BittyKitty/blob/main/dist/icons/flamoji/flamoji.json).
