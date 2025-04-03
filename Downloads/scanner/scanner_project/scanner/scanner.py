import asyncio
import csv
import ipaddress
import argparse
import subprocess

# Fonction pour effectuer un ping sur une adresse IP
async def ping_ip(ip):
    # Utilisation de subprocess pour appeler 'ping' de manière synchrone, dans un thread séparé
    result = await asyncio.to_thread(subprocess.run, 
                                      ['ping', '-n', '1', ip],
                                      capture_output=True, text=True)
    if "TTL=" in result.stdout:
        return ip, "Active", None
    return ip, "Inactive", None

# Fonction pour scanner une plage d'adresses IP
async def scan_range(ip_range):
    network = ipaddress.ip_network(ip_range, strict=False)
    tasks = [ping_ip(str(ip)) for ip in network.hosts()]
    return await asyncio.gather(*tasks)

# Fonction pour scanner des adresses IP à partir d'un fichier
async def scan_file(file_path):
    with open(file_path, mode='r') as file:
        lines = file.readlines()
    tasks = [ping_ip(line.strip()) for line in lines if line.strip()]
    return await asyncio.gather(*tasks)

# Fonction principale qui gère les entrées et lance le scan
async def main():
    parser = argparse.ArgumentParser(description='Asynchronous Network Scanner')
    parser.add_argument('--range', help='IP range to scan (e.g., 192.168.1.0/24)')
    parser.add_argument('--file', help='File containing IP addresses to scan')
    args = parser.parse_args()
    
    if args.range:
        results = await scan_range(args.range)
    elif args.file:
        results = await scan_file(args.file)
    else:
        print("Please specify either --range or --file.")
        return
    
    # Vérifie si des résultats ont été trouvés
    if not any(status == "Active" for _, status, _ in results):
        print("Le programme n'a pas trouvé d'autre adresse IP.")
        return
    
    # Sauvegarde des résultats dans un fichier CSV
    with open('results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Status", "Ping (ms)"])
        for row in results:
            writer.writerow(row)
    
    # Affichage des résultats
    for ip, status, _ in results:
        if status == "Active":
            print(f"{ip} Active")
        else:
            print(f"{ip} Inactive")
    print("Résultats sauvegardés dans results.csv")

# Lancer l'application
if __name__ == '__main__':
    asyncio.run(main())
