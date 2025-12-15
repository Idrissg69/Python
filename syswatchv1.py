import platform
import psutil

def bytes_to_gigabytes(bytes_value):
    gigabytes = bytes_value / (1024 ** 3)
    return round(gigabytes, 2)

def systeme_exploitation():
    os_name = platform.system()
    print("f{os_name}")
    
    if os_name == "Windows":
        
        version = platform.release()
        print(f"{version}")
        
        architecture = platform.machine()
        print(f"{architecture}")
        
        version_python = platform.version()
        print(f"{version_python}")
        
        nom_hostname = platform.node()
        print(f"{nom_hostname}")

        coeurs_physiques = psutil.cpu_count(logical=False)
        print(f"{coeurs_physiques}")

        coeurs_logiques = psutil.cpu_count(logical=True)
        print(f"{coeurs_logiques}")

        utilisation_cpu = psutil.cpu_percent(interval=None)
        print(f"{utilisation_cpu}%")

        ram = psutil.virtual_memory()

        ram_totale_go = bytes_to_gigabytes(ram.total)
        print(f"{ram_totale_go} Go")

        ram_disponible_go = bytes_to_gigabytes(ram.available)
        print(f"{ram_disponible_go} Go")

        pourcentage_utilisation = ram.percent
        print(f"{pourcentage_utilisation}%")

systeme_exploitation()