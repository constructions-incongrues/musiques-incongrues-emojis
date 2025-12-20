# Project Brief - Tronches Incongrues

## Vue d'ensemble
**Projet** : Générateur de collections d'emojis musicaux incongrus  
**Nom** : Tronches Incongrues  
**Type** : Générateur automatisé d'emojis pour plateformes de communication  

## Objectif principal
Créer un système automatisé qui génère des fichiers de configuration JSON (flamoji) et YAML (RocketChat) à partir de collections d'emojis personnalisés organisés par thème.

## Fonctionnalités clés
- **Génération automatique** : Script Python qui scanne les collections et génère les fichiers de configuration
- **Support multi-format** : PNG, JPEG, GIF
- **Sorties multiples** : 
  - `flamoji.json` pour Flamoji/BittyKitty
  - `rocketchat.yaml` pour RocketChat/emojipacks
- **CI/CD intégré** : GitHub Actions pour génération automatique à chaque push
- **URL configurable** : Base URL personnalisable via variable d'environnement

## Collections existantes
- **amour** : Émojis thématiques amour
- **ballounes** : Collection de ballons
- **boodlofi** : Série étendue d'emojis (50+)
- **boodme** : Collection complémentaire (90+)
- **discutons** : Émojis de conversation (20+)
- **gargamelle** : Collection thématique (10+)
- **geocities** : Style rétro GeoCities (5+)
- **millemilliards** : Identités visuelles (25+)
- **n8n** : Émojis techniques n8n (2+)
- **otro** : Collection personnalisée (15+)

## Architecture technique
- **Langage** : Python 3
- **Automatisation** : GitHub Actions
- **Structure** : Collections organisées par dossiers
- **Génération** : Script `generate_flamoji.py`

## Déploiement
- **URL de base** : Configurable via `FLAMOJI_BASE_URL`
- **Valeur par défaut** : `/assets/emojis`
- **Déclenchement** : Automatique sur push main ou manuel

## Livrables attendus
- Fichiers de configuration JSON/YAML pour chaque collection
- Documentation d'utilisation
- Workflow GitHub Actions fonctionnel
- Collections d'emojis organisées et documentées
