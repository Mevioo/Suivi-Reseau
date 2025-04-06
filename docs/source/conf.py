# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))


project = 'Suivi-Reseau'
copyright = '2025, Lucas Guyon'
author = 'Lucas Guyon'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

html_theme = 'alabaster'
html_static_path = ['_static']
