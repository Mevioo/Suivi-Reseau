import os
import sys

# Ajoute le chemin du projet pour que Sphinx trouve les modules Python
sys.path.insert(0, os.path.abspath("../.."))

# Configuration de base
project = 'Suivi-Reseau'
author = 'Mevioo'
release = '1.0'

# Définir la source directory
source_suffix = '.rst'
master_doc = 'index'  # Sphinx cherche "index.rst" comme point d'entrée

# Extensions utiles
extensions = [
    'sphinx.ext.autodoc',  # Génère la doc automatiquement depuis les docstrings
    'sphinx.ext.napoleon',  # Supporte le style Google et NumPy pour les docstrings
]

# Définition du dossier de sortie
html_theme = 'alabaster'  # Ou un autre thème comme 'sphinx_rtd_theme'
