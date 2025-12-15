import collector
import datetime

VERSION_SCRIPT = "2.0"

def octets_vers_go(octets: int) -> str:
    
    if octets is None:
        return "N/A"
    gigabytes = octets / (1024 ** 3)
    return f"{gigabytes:.2f} Go"

def afficher_infos_systeme(data_systeme: dict):
    print("Informations Système")
    print(f"Système d'exploitation : {data_systeme.get('os', 'N/A')}")
    print(f"Version du système : {data_systeme.get('version', 'N/A')}")
    print(f"Architecture : {data_systeme.get('architecture', 'N/A')}")
    print(f"Nom de la machine (Hostname) : {data_systeme.get('hostname', 'N/A')}")
    print("-" * 40)

def afficher_cpu(data_cpu: dict):
    print("Métriques CPU")
    print(f"Cœurs physiques : {data_cpu.get('coeurs_physiques', 'N/A')}")
    print(f"Cœurs logiques : {data_cpu.get('coeurs_logiques', 'N/A')}")
    print(f"Utilisation actuelle : {data_cpu.get('utilisation', 'N/A')}%")
    print("-" * 40)

def afficher_memoire(data_memoire: dict):

    print("Métriques Mémoire (RAM)")
    
    total_go = octets_vers_go(data_memoire.get('total'))
    disponible_go = octets_vers_go(data_memoire.get('disponible'))

    print(f"Mémoire totale : {total_go}")
    print(f"Mémoire disponible : {disponible_go}")
    print(f"Pourcentage d'utilisation : {data_memoire.get('pourcentage', 'N/A')}%")
    print("-" * 40)

def afficher_disques(data_disques: list):

    print("Utilisation des Disques")
    
    if not data_disques:
        print("* Aucune partition accessible trouvée.")
        print("-" * 40)
        return

    print("| Point de Montage | Total | Utilisé | Pourcentage |")

    for partition in data_disques:
        point = partition.get('point_montage', 'N/A')
        total = octets_vers_go(partition.get('total'))
        utilise = octets_vers_go(partition.get('utilise'))
        pourcentage = f"{partition.get('pourcentage', 'N/A')}%"
        
        print(f"| {point} | {total} | {utilise} | {pourcentage} |")
            
    print("-" * 40)

def main():

    print("=" * 50)
    print(f"RAPPORT DE SUPERVISION SYSTÈME V{VERSION_SCRIPT}")
    print("=" * 50)

    data_global = collector.collecter_tout()
    
    timestamp_iso = data_global.get('timestamp')
    if timestamp_iso:
        try:
            dt_obj = datetime.datetime.fromisoformat(timestamp_iso)
            print(f"Heure de la collecte : {dt_obj.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError:
             print(f"Timestamp brut : {timestamp_iso}")
    print("-" * 50)

    afficher_infos_systeme(data_global.get('systeme', {}))
    afficher_cpu(data_global.get('cpu', {}))
    afficher_memoire(data_global.get('memoire', {}))
    afficher_disques(data_global.get('disques', []))

if __name__ == "__main__":
    main()