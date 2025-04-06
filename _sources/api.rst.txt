Documentation de l'API
======================

Ce module contient les fonctions principales pour effectuer un scan réseau.

.. automodule:: src.scanner
   :members:
   :undoc-members:
   :show-inheritance:

Exemples d'utilisation
----------------------

Appel d'une fonction de scan :

.. code-block:: python

    import asyncio
    from src import scanner

    # Scan d'une plage
    results = asyncio.run(scanner.scan_range("192.168.0.0/30"))
    for ip, status, _ in results:
        print(f"{ip}: {status}")

    # Scan à partir d'un fichier
    results = asyncio.run(scanner.scan_file("ips.txt"))
