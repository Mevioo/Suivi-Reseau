Introduction
============

**Suivi-Réseau** est une application Python permettant de détecter les adresses IP
actives sur un réseau local en utilisant des pings asynchrones.

Fonctionnalités :
-----------------

- Scan d'une plage IP (notation CIDR).
- Scan via fichier d'IP.
- Résultats dans un fichier CSV.
- Compatible avec l'interface ligne de commande.

Exemples :
----------

Scan d'une plage IP :

.. code-block:: bash

    python scanner.py --range 192.168.1.0/24

Scan à partir d'un fichier texte :

.. code-block:: bash

    python scanner.py --file ips.txt
