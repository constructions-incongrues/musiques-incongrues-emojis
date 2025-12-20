# System Patterns - Architecture Technique

## Architecture générale
```
Repository Git
├── collections/          # Dossiers de collections d'emojis
├── .github/workflows/    # GitHub Actions CI/CD
├── scripts/             # Outils de génération
├── memory-bank/         # Documentation système
└── documentation/       # Guides utilisateur
```

## Pattern principal : Collection-Based Generation

### Structure des collections
```
collections/{collection-name}/
├── *.png, *.jpg, *.jpeg, *.gif  # Fichiers d'emojis
├── flamoji.json                  # Généré automatiquement
└── rocketchat.yaml               # Généré automatiquement
```

### Workflow de génération
1. **Scan** : Le script Python parcourt les dossiers de collections
2. **Indexation** : Inventaire des fichiers d'images supportés
3. **Génération** : Création des fichiers JSON et YAML
4. **Sortie** : Écriture dans chaque dossier de collection

## Pattern CI/CD : GitHub Actions

### Workflow principal
- **Déclencheur** : Push sur main ou déclenchement manuel
- **Job principal** : `generate-flamoji`
- **Steps** :
  1. Checkout du code
  2. Installation des dépendances Python
  3. Exécution du script de génération
  4. Commit et push des fichiers générés

### Configuration d'environnement
- **Variable** : `FLAMOJI_BASE_URL`
- **Portée** : Repository secrets/variables
- **Usage** : URL de base pour les chemins d'emojis

## Patterns de format de données

### Format JSON (flamoji.json)
```json
{
  "index": {
    "title": "{collection-name}_{filename}",
    "text_to_replace": ":{collection-name}_{filename}:",
    "path": "/{base-url}/{collection-name}/{filename}.{ext}"
  }
}
```

### Format YAML (rocketchat.yaml)
```yaml
title: {collection-name}
emojis:
- name: {filename}
  src: /{base-url}/{collection-name}/{filename}.{ext}
```

## Pattern de validation

### Validation d'entrée
- **Formats supportés** : .png, .jpg, .jpeg, .gif
- **Nommage** : Noms de fichiers valides pour les plateformes cibles
- **Structure** : Dossiers de collections doivent contenir des images

### Validation de sortie
- **JSON** : Format valide et chemins cohérents
- **YAML** : Syntaxe YAML valide et structure emojipacks
- **Encoding** : UTF-8 pour tous les fichiers texte

## Pattern d'extensibilité

### Ajout de nouvelles collections
1. Créer un dossier dans `collections/`
2. Ajouter les fichiers d'emojis
3. Push sur main → génération automatique
4. Fichiers de configuration générés automatiquement

### Support de nouvelles plateformes
- **Approche** : Templates de format modulaires
- **Configuration** : Ajout de nouveaux générateurs de format
- **Backward compatibility** : Maintien des formats existants

## Patterns de performance

### Optimisation de génération
- **Traitement par lot** : Une seule passe pour tous les formats
- **Cache** : Pas de regeneration inutile des fichiers existants
- **Parallelisation** : Possibilité de traiter plusieurs collections en parallèle

### Gestion de la mémoire
- **Streaming** : Traitement des images sans chargement complet en mémoire
- **Lazy loading** : Chargement à la demande des métadonnées
- **Cleanup** : Nettoyage des fichiers temporaires

## Patterns de monitoring et debugging

### Logs de génération
- **Niveau** : INFO pour succès, ERROR pour échecs
- **Format** : Timestamp + collection + action
- **Sortie** : Console GitHub Actions + logs persistants

### Gestion d'erreurs
- **Validation préventive** : Vérification avant génération
- **Rollback** : Pas de modification en cas d'erreur
- **Notifications** : Logs d'erreur détaillés en cas d'échec

## Patterns de sécurité

### Validation des entrées
- **Sanitisation** : Noms de fichiers sûrs
- **Limites** : Taille et nombre de fichiers par collection
- **Types** : Validation stricte des formats d'image

### Protection du repository
- **CI-only** : Modifications uniquement via workflows GitHub Actions
- **Review** : Pull requests pour changements manuels
- **Backup** : Historique git pour rollback si nécessaire
