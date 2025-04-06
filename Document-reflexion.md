
# Document de réflexion

## Introduction

### Présentation du sujet choisi

Le projet **Suivi-Réseau** est un utilitaire Python destiné à effectuer des diagnostics réseau efficaces en scannant de manière asynchrone des plages ou listes d'adresses IP. Ce choix est motivé par l'intérêt croissant de disposer d'outils rapides et fiables pour identifier les équipements actifs ou inactifs dans un réseau local.

### Objectifs et organisation du projet

Les objectifs principaux du projet sont :

- Développer un outil simple et performant pour les diagnostics réseau.
- Utiliser Python pour son accessibilité et sa richesse de librairies.
- Automatiser le processus via une intégration CI/CD complète.
- Produire une documentation claire et accessible.

L'organisation du projet est structurée en plusieurs étapes :

- Conception et développement du code.
- Mise en place des tests unitaires.
- Création d'une documentation technique détaillée.
- Déploiement continu via GitHub Actions.

## Développement

### Étapes principales réalisées

- **Phase initiale :** Conception et structuration du projet (architecture).
- **Développement :** Développement du scanner réseau asynchrone, gestion du format CSV.
- **Tests unitaires :** Couverture complète des fonctionnalités critiques pour assurer la robustesse du code.
- **Documentation :** Génération automatique d'une documentation technique via Sphinx, hébergée sur GitHub Pages.
- **CI/CD :** Configuration des workflows GitHub Actions pour automatiser les tests et le déploiement.

### Problèmes rencontrés et solutions apportées


- **Intégration continue :** Problèmes liés à la configuration initiale de GitHub Actions. Solution : revue de documentation et validation progressive par tests intermédiaires.

- **Problèmes de tests :** Différents problèmes de test notemment ceux de flake8 qui ont été assez longs à corriger

- **Problèmes de code :** Différents problèmes lors de l'écriture du code de scanner.py ont été rencontrés

## Pipeline CI/CD

### Explication des étapes configurées dans le workflow

Le pipeline CI/CD est composé des workflows suivants :

- **Tests.yml :**
  - Vérification du code (`Flake8` et `Pylint`).
  - Exécution des tests unitaires (`unittest`).
  - Couverture de code minimale exigée (90%), résultats affichés à 94%.
- **Deploiement-doc.yml :**
  - Installation automatique des dépendances de documentation.
  - Génération automatique de la documentation via Sphinx.
  - Déploiement automatique sur GitHub Pages dès la validation sur la branche principale.

### Comment le pipeline répond aux objectifs du projet

Le pipeline assure une vérification constante de la qualité du code et garantit que la documentation est toujours à jour. Il permet :

- Une maintenance facilitée grâce à l'automatisation.
- Une visibilité constante sur la qualité et la fiabilité du projet.
- Un déploiement immédiat et continu de la documentation technique.

## Conclusion et auto-évaluation

### Bilan personnel

#### Points réussis
- Automatisation réussie grâce au pipeline CI/CD.
- Documentation claire et utile pour les utilisateurs finaux.

#### Points à améliorer
- Optimisation supplémentaire des performances pour des scans très larges.
- Problèmes de développement.
- Exploration plus approfondie de solutions alternatives pour l'exécution des processus.

En conclusion, ce projet a permis d'approfondir significativement mes compétences en automatisation, développement et plus largement de Github.
