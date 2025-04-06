
"""
scanner.py

Ce module fournit un utilitaire de scan réseau asynchrone utilisant `ping`.
"""

import asyncio
import csv
import ipaddress
import argparse
import subprocess
import os
import platform


async def ping_ip(ip):
    if platform.system().lower() == "windows":
        command = ['ping', '-n', '1', ip]
    else:
        command = ['ping', '-c', '1', ip]

    result = await asyncio.to_thread(
        subprocess.run,
        command,
        capture_output=True,
        text=True
    )

    if "ttl=" in result.stdout.lower():
        return ip, "Active", None
    return ip, "Inactive", None


async def scan_range(ip_range):
    network = ipaddress.ip_network(ip_range, strict=False)
    tasks = [ping_ip(str(ip)) for ip in network.hosts()]
    return await asyncio.gather(*tasks)


async def scan_file(file_path):
    if not os.path.exists(file_path):
        print(f"Fichier introuvable : {file_path}")
        return []

    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    tasks = [ping_ip(line.strip()) for line in lines if line.strip()]
    return await asyncio.gather(*tasks)


async def run_scanner(args=None):
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
        print(f"{ip} {status}")
    print("Résultats sauvegardés dans data/results/resultat.csv")


def main():
    asyncio.run(run_scanner())


if __name__ == '__main__':  # pragma: no cover
    main()
