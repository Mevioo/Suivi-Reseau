# -*- coding: utf-8 -*-
"""
scanner.py

Ce module fournit un utilitaire de scan réseau asynchrone utilisant ping.

Il permet de scanner une plage d'adresses IP ou une liste provenant d'un
fichier
et sauvegarde les résultats dans un fichier CSV. Ce script est conçu pour être
exécuté depuis la ligne de commande avec des arguments `--range` ou `--file`.

Fonctionnalités :
- Ping asynchrone d'adresses IP via subprocess dans un thread.
- Scan d'une plage IP (`CIDR`) ou de fichiers contenant des IP.
- Export CSV des IP actives/inactives.
- Affichage en console des résultats.

Exemple :
    $ python scanner.py --range 192.168.1.0/24
    $ python scanner.py --file ips.txt

Auteurs:
    Lucas Guyon

Date:
    Avril 2025
"""

import asyncio
import csv
import ipaddress
import argparse
import subprocess
import os

# Fonction pour effectuer un ping sur une adresse IP


async def ping_ip(ip):
    """
    Effectue un ping asynchrone sur une adresse IP.

    Args:
        ip (str): Adresse IP à tester.

    Returns:
        tuple: Une tuple contenant l'IP (str), le statut ("Active"/"Inactive"),
               et None pour une éventuelle extension.
    """
    result = await asyncio.to_thread(
        subprocess.run,
        ['ping', '-n', '1', ip],
        capture_output=True,
        text=True
    )

    if "TTL=" in result.stdout:
        return ip, "Active", None
    return ip, "Inactive", None

# Fonction pour scanner une plage d'adresses IP


async def scan_range(ip_range):
    """
    Scanne une plage d'adresses IP.

    Args:
        ip_range (str): Plage d'IP au format CIDR (e.g., "192.168.1.0/24").

    Returns:
        list: Liste de tuples (ip, statut, None) pour chaque IP scannée.
    """
    network = ipaddress.ip_network(ip_range, strict=False)
    tasks = [ping_ip(str(ip)) for ip in network.hosts()]
    return await asyncio.gather(*tasks)

# Fonction pour scanner des adresses IP à partir d'un fichier


async def scan_file(file_path):
    """
    Scanne des adresses IP lues depuis un fichier texte.

    Args:
        file_path (str): Chemin du fichier contenant les adresses IP
          (une par ligne).

    Returns:
        list: Liste de tuples (ip, statut, None) pour chaque IP scannée.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    tasks = [ping_ip(line.strip()) for line in lines if line.strip()]
    return await asyncio.gather(*tasks)

# Fonction principale qui gère les entrées et lance le scan


async def run_scanner(args=None):
    """
    Point d'entrée logique du scanner (séparé de __main__ pour être testable).

    Args:
        args (list, optional): Liste d'arguments pour argparse. Si None,
         utilise sys.argv.
    """

    parser = argparse.ArgumentParser(
        description='Asynchronous Network Scanner'
    )

    parser.add_argument(
        '--range',
        help='IP range to scan (e.g., 192.168.1.0/24)'
    )

    parser.add_argument('--file', help='File containing IP addresses to scan')
    parsed_args = parser.parse_args(args)

    if parsed_args.range:
        results = await scan_range(parsed_args.range)
    elif parsed_args.file:
        results = await scan_file(parsed_args.file)
    else:
        print("Please specify either --range or --file.")
        return

    if not any(status == "Active" for _, status, _ in results):
        print("Le programme n'a pas trouvé d'autre adresse IP.")
        return

    os.makedirs('data/results', exist_ok=True)
    with open(
        'data/results/resultat.csv',
        mode='w',
        newline='',
        encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Status", "Ping (ms)"])
        for row in results:
            writer.writerow(row)

    for ip, status, _ in results:
        if status == "Active":
            print(f"{ip} Active")
        else:
            print(f"{ip} Inactive")
    print("Résultats sauvegardés dans data/results/resultat.csv")


def main():
    """Lance l'application scanner en mode CLI."""
    asyncio.run(run_scanner())


if __name__ == '__main__':  # pragma: no cover
    main()
