
# Suivi-Réseau

## Présentation

Le projet **Suivi-Réseau** est un utilitaire Python conçu pour faciliter la gestion et l'analyse des réseaux locaux. Il permet de vérifier rapidement la disponibilité des équipements réseau grâce à un scan asynchrone utilisant la commande `ping`. Destiné à des administrateurs système ou à toute personne souhaitant réaliser des diagnostics réseau efficaces, Suivi-Réseau propose une prise en main simple et intuitive via la ligne de commande.

## Fonctionnalités

- **Ping asynchrone** : Exécution rapide et simultanée des tests de connectivité.
- **Scan par plage CIDR** : Analyse complète de plages IP.
- **Scan depuis fichier** : Chargement simple des adresses IP à partir d'un fichier texte.
- **Export CSV automatique** : Résultats sauvegardés clairement.

## Prérequis

- Python 3.10 ou supérieur

## Installation

Clonez et préparez le projet rapidement :

```bash
git clone https://github.com/Mevioo/Suivi-Reseau.git
cd Suivi-Reseau
```

## Utilisation

### Scan d'une plage IP

```bash
python .\src\scanner.py --range 192.168.1.x/24
python .\src\scanner.py --range 192.168.1.x
```

### Scan depuis un fichier

Créer un fichier `ips.txt` avec une adresse IP par ligne :

```
192.168.1.1
192.168.1.2
192.168.1.3
```

Exécutez :

```bash
python scanner.py --file ips.txt
```

Les résultats s'affichent dans la console et sont enregistrés dans :

```
data/results/resultat.csv
```

## Documentation

Consultez la documentation complète sur [Suivi-Réseau Documentation](https://Mevioo.github.io/suivi-reseau/).

## Structure du projet

```
SUVI-RESEAU/
├── .github/
│   └── workflows/
│       ├── deploiement-doc.yml
│       └── tests.yml
├── data/
│   ├── results/
│   │   └── resultat.csv
│   └── ips.txt
├── docs/
│   ├── build/
│   ├── source/
│   │   ├── api.rst
│   │   ├── conf.py
│   │   ├── index.rst
│   │   └── introduction.rst
│   ├── make.bat
│   └── Makefile
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   └── scanner.py
├── tests/
│   ├── __pycache__/
│   └── test_scanner.py
├── .coverage
├── .gitignore
├── doc
└── README.md
```

## Auteur

**Lucas Guyon**

## Licence

Ce projet est sous licence MIT.
