import platform
import psutil

VERSION_SCRIPT = "1.0"

def bytes_to_gigabytes(bytes_value):
    gigabytes = bytes_value / (1024 ** 3)
    return round(gigabytes, 2)

def afficher_infos_systeme():
    print("Informations Système")
    print(f"Système d'exploitation : {platform.system()}")
    print(f"Version du système : {platform.release()}")
    print(f"Architecture : {platform.machine()} ({platform.architecture()[0]})")
    print(f"Nom de la machine (Hostname) : {platform.node()}")
    print(f"Version de Python : {platform.python_version()}")
    print("-" * 40)



def afficher_cpu():
    print("Métriques CPU")
    
    coeurs_physiques = psutil.cpu_count(logical=False)
    coeurs_logiques = psutil.cpu_count(logical=True)
    
    print(f"Nombre de coeurs physiques : {coeurs_physiques}")
    print(f"Nombre de coeurs logiques (Threads) : {coeurs_logiques}")

    utilisation_cpu = psutil.cpu_percent(interval=None) 
    print(f"Pourcentage d'utilisation actuel : {utilisation_cpu}%")
    print("-" * 40)



def afficher_memoire():
    print("Métriques Mémoire (RAM)")
    
    ram = psutil.virtual_memory()

    ram_totale_go = bytes_to_gigabytes(ram.total)
    ram_disponible_go = bytes_to_gigabytes(ram.available)

    print(f"Mémoire totale * {ram_totale_go} Go")
    print(f"Mémoire disponible : {ram_disponible_go} Go")
    
    pourcentage_utilisation = ram.percent
    print(f"Pourcentage d'utilisation : {pourcentage_utilisation}%")
    print("-" * 40)



def afficher_disques():
    print("Utilisation des Disques")

    try:
        partitions = psutil.disk_partitions(all=False)
    except Exception as e:
        print(f"Erreur lors de la récupération des partitions : {e}")
        return

    print("Point de Montage, Pourcentage d'Utilisation ")

    for partition in partitions:
        point_de_montage = partition.mountpoint
        
        try:
            usage = psutil.disk_usage(point_de_montage)
            pourcentage_utilisation = f"{usage.percent:.1f}%"
            
            print(f"| {point_de_montage} | {pourcentage_utilisation} |")

        except PermissionError:
            print(f"| {point_de_montage} | Erreur de permission |")
        except FileNotFoundError:
            print(f"| {point_de_montage} | Point introuvable |")
        except Exception as e:
            print(f"| {point_de_montage} | Erreur ({e}) |")
            
    print("-" * 40)

if __name__ == "__main__":
    
    afficher_infos_systeme()
    afficher_cpu()
    afficher_memoire()
    afficher_disques()