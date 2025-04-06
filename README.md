🌐 Scanner Réseau 

Ce projet Python permet de scanner un réseau local de manière asynchrone pour détecter les machines actives à l’aide de pings ICMP. Il est possible de scanner :

Une plage d’adresses IP (ex: 192.168.1.0/24)


⚙️ Fonctionnalités
🔁 Scan asynchrone rapide via asyncio

💾 Export automatique des résultats vers un fichier results.csv

✅ Indique si chaque hôte est actif ou inactif

📦 Prérequis
Python 3.7+

Fonctionne sous Windows (commande ping -n)


🚀 Installation
bash
Copier
Modifier
git clone https://github.com/Mevioo/Suivi-Reseau
cd scanner-reseau
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt  # si nécessaire
▶️ Utilisation
1. 📁 Scanner depuis un fichier texte
Le fichier doit contenir une IP par ligne. Exemple :

Copier
Modifier
192.168.1.10
192.168.1.20
Commande :

bash
Copier
Modifier
python scanner.py --file chemin/vers/fichier.txt


2. 🌐 Scanner une plage IP
Utilise une notation CIDR, comme :

bash
Copier
Modifier
python scanner.py --range 192.168.1.0/24
💾 Résultats
Les résultats sont enregistrés dans un fichier results.csv automatiquement, au format :

IP	Status	Ping (ms)
192.168.1.10	Active	-
192.168.1.20	Inactive	-
🛠 Exemple complet
bash
Copier
Modifier
python scanner.py --range 192.168.1.0/24
python-repl
Copier
Modifier
192.168.1.1 Active
192.168.1.2 Inactive
...
Résultats sauvegardés dans results.csv


⚠️ Avertissement légal
❗ N’effectuez pas de scans sur des réseaux sans autorisation. Le scan de ports ou d’adresses IP sans consentement est interdit dans de nombreux pays et peut être considéré comme une tentative d’intrusion.
