import platform
import psutil
import datetime
import json

def collecter_info_systeme():
    architecture_info = platform.architecture()
    
    infos_systeme = {
        'os': platform.system(),
        'version': platform.release(),
        'architecture': f"{platform.machine()} ({architecture_info[0]})",
        'hostname': platform.node(),
    }
    
    return infos_systeme

def collecter_cpu():
    coeurs_physiques = psutil.cpu_count(logical=False)
    coeurs_logiques = psutil.cpu_count(logical=True)
    utilisation = psutil.cpu_percent(interval=1)
    
    return {
        'coeurs_physiques': coeurs_physiques,
        'coeurs_logiques': coeurs_logiques,
        'utilisation': utilisation
    }

def collecter_memoire():
    memoire = psutil.virtual_memory()
    
    return {
        'total': memoire.total,
        'disponible': memoire.available,
        'pourcentage': memoire.percent
    }

def collecter_disques():
    partitions_data = []
    
    try:
        partitions = psutil.disk_partitions(all=False)
    except Exception:
        return partitions_data

    for partition in partitions:
        point_montage = partition.mountpoint
        
        try:
            usage = psutil.disk_usage(point_montage)
            partitions_data.append({
                'point_montage': point_montage,
                'total': usage.total,
                'utilise': usage.used,
                'pourcentage': usage.percent
            })
        except (PermissionError, FileNotFoundError, Exception):
            continue
            
    return partitions_data

def collecter_tout():
    timestamp = datetime.datetime.now().isoformat()
    
    resultat_global = {
        'timestamp': timestamp,
        'systeme': collecter_info_systeme(),
        'cpu': collecter_cpu(),
        'memoire': collecter_memoire(),
        'disques': collecter_disques()
    }
    
    return resultat_global

if __name__ == "__main__":
    
    donnees_globales = collecter_tout()
    
    print(json.dumps(donnees_globales, indent=4))