# Tech Context - Technologies et Environnement

## Stack technologique principal

### Backend/Automation
- **Python 3.x** : Langage principal pour la génération d'emojis
- **Standard Library** : 
  - `pathlib` : Manipulation des chemins de fichiers
  - `json` : Sérialisation JSON
  - `argparse` : Parsing des arguments en ligne de commande
  - `os`, `sys` : Operations système
- **Dépendances** : Minimal, principalement libraries standard

### CI/CD
- **GitHub Actions** : Automatisation des workflows
- **Actionscheckout** : `actions/checkout@v4` - Checkout du code
- **ActionssetupPython** : `actions/setup-python@v4` - Environment Python
- **Git** : Versioning et déploiement automatique

### Formats de données
- **JSON** : Format flamoji (compatible BittyKitty)
- **YAML** : Format RocketChat/emojipacks
- **Images** : PNG, JPEG, GIF supportés

## Environnement de développement

### Structure du repository
```
musiques-incongrues-emojis/
├── .github/workflows/          # GitHub Actions
├── collections/                # Collections d'emojis
├── memory-bank/               # Documentation système
├── generate_flamoji.py        # Script principal
├── requirements.txt           # Dépendances Python
└── README.md                  # Documentation
```

### Configuration de développement
- **Python** : Version 3.x recommandée
- **OS Support** : Cross-platform (Linux, macOS, Windows)
- **Encoding** : UTF-8 pour tous les fichiers

### Dépendances Python
```txt
# requirements.txt
# Vide ou dépendances minimales
# Le projet utilise principalement la standard library
```

### GitHub Actions Environment
```yaml
# Variables d'environnement
FLAMOJI_BASE_URL: Optional, défaut="/assets/emojis"

# Permissions requises
contents: write  # Pour push des fichiers générés
```

## Configuration d'exécution

### Script principal : generate_flamoji.py
- **Usage** : `python3 generate_flamoji.py [options]`
- **Options** :
  - `--base-url` : URL de base personnalisée (optionnel)
  - Défaut : `/assets/emojis`

### Processus de génération
1. **Découverte** : Scan du dossier `collections/`
2. **Filtrage** : Sélection des fichiers image supportés
3. **Génération** : Création des fichiers de configuration
4. **Écriture** : Sauvegarde dans chaque dossier de collection

## Intégrations externes

### Plateformes supportées
- **Flamoji/BittyKitty** : Format JSON
- **RocketChat** : Format YAML via emojipacks
- **Générique** : Format extensible pour autres plateformes

### Services de déploiement
- **GitHub Pages** : Hébergement des assets
- **CDN** : Distribution des emojis (configurable via base URL)

## Patterns de déploiement

### Développement local
```bash
# Installation
pip install -r requirements.txt

# Génération locale
python3 generate_flamoji.py

# Avec URL personnalisée
python3 generate_flamoji.py --base-url "https://mon-site.com/emojis"
```

### Production (GitHub Actions)
- **Trigger** : Push sur main ou workflow manuel
- **Environment** : Ubuntu latest
- **Output** : Commit automatique des fichiers générés

## Contraintes techniques

### Limitations connues
- **Formats image** : PNG, JPEG, GIF uniquement
- **Taille** : Pas de limite stricte définie
- **Nombre** : Pas de limite sur le nombre d'emojis par collection

### Optimisations
- **Performance** : Traitement en mémoire pour collections de taille moyenne
- **Scalabilité** : Architecture modulaire pour ajouts futurs
- **Reliability** : Validation avant écriture des fichiers

## Outils de développement

### Utilitaires système
- **Git** : Versioning et collaboration
- **GitHub** : Hosting et CI/CD
- **Python** : Interpréteur et standard library

### Outils optionnels
- **ImageMagick** : Pour обработка d'images (si extensión future)
- **Pre-commit hooks** : Pour validation avant commit (futur)
- **Linting** : black, flake8 pour formatage Python (futur)

## Monitoring et logging

### Logs de développement
- **Console** : Sortie standard pour debugging
- **GitHub Actions** : Logs persistants dans l'interface

### Métriques de performance
- **Temps de génération** : Mesuré et loggé
- **Nombre de fichiers** : Compteurs par collection
- **Erreurs** : Validation et rapport d'erreurs

## Sécurité

### Validation des entrées
- **Sanitisation** : Noms de fichiers nettoyés
- **Limites** : Validation des tailles et types
- **Encoding** : UTF-8 strict

### Permissions
- **GitHub Actions** : Permissions minimales requises
- **Filesystem** : Lecture/écriture contrôlée
