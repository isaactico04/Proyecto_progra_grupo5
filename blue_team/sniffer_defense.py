
# BLUE TEAM — sniffer_defense.py
# Sniffer de defensa para detectar paquetes SYN sospechosos

# Uso:
#   sudo python3 blue_team/sniffer_defense.py

# Requiere:
#   - scapy instalado (pip install scapy)
#   - Permisos de administrador (sudo)
#   - Python 3.x

# Funciones:
#   1) Monitorea trafico TCP dirigido a la IP protegida
#   2) Detecta paquetes SYN a puertos fuera del rango comun
#   3) Registra IPs atacantes en blocked_ips.txt
#   4) Genera logs en defense_log.txt
#   5) Sugiere comando UFW para bloquear

# Limitaciones:
#   - Solo soporta IPv4
#   - Detecta solo la IP principal

import os
import socket
from datetime import datetime
from scapy.all import sniff, IP, TCP

# Detecta IP local automaticamente

def obtener_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# IP de la maquina a defender
IP_PROTEGIDA = obtener_ip_local()

# Puertos comunes
PUERTOS_COMUNES = {80, 443, 3306, 5432, 8080, 8443}

# Archivos de log
ARCHIVO_LOG = "blue_team/defense_log.txt"
ARCHIVO_BLOQUEADOS = "blue_team/blocked_ips.txt"

# IPs ya bloqueadas
ips_bloqueadas = set()

# Inicializa archivos de log

def inicializar_logs():
    os.makedirs("blue_team", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear defense_log.txt
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 60 + "\n")
        f.write(f"NUEVA SESION - {timestamp}\n")
        f.write(f"IP Protegida: {IP_PROTEGIDA}\n")
        f.write("=" * 60 + "\n\n")
    
    # Crear blocked_ips.txt si no existe
    if not os.path.exists(ARCHIVO_BLOQUEADOS):
        with open(ARCHIVO_BLOQUEADOS, "w", encoding="utf-8") as f:
            f.write("# IPS BLOQUEADAS\n")
            f.write("# Formato: IP  # Fecha de bloqueo\n")
            f.write(f"# Creado: {timestamp}\n\n")
    
    # Cargar IPs ya bloqueadas
    if os.path.exists(ARCHIVO_BLOQUEADOS):
        with open(ARCHIVO_BLOQUEADOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    # Extraer solo la IP
                    ip = linea.split("#")[0].strip()
                    if ip:
                        ips_bloqueadas.add(ip)
    
    print(f"[OK] Logs inicializados")
    print(f"[OK] IPs bloqueadas: {len(ips_bloqueadas)}")


# Registra evento sospechoso

def registrar_evento(ip_origen, puerto_destino):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] SYN SOSPECHOSO\n")
        f.write(f"  IP: {ip_origen}\n")
        f.write(f"  Puerto: {puerto_destino}\n")
        f.write(f"  Razon: Puerto fuera del rango comun\n\n")
    
    print(f"[ALERTA] SYN desde {ip_origen} al puerto {puerto_destino}")


# Bloquea IP sospechosa

def bloquear_ip(ip_origen):
    # Evitar duplicados
    if ip_origen in ips_bloqueadas:
        return
    
    ips_bloqueadas.add(ip_origen)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Registrar en blocked_ips.txt
    with open(ARCHIVO_BLOQUEADOS, "a", encoding="utf-8") as f:
        f.write(f"{ip_origen}  # {timestamp}\n")
    
    # Sugerir comando UFW
    print("\n" + "=" * 60)
    print(f"[ACCION] IP Sospechosa: {ip_origen}")
    print(f"Registrada en: {ARCHIVO_BLOQUEADOS}")
    print(f"\nBloquear con UFW:")
    print(f"  sudo ufw deny from {ip_origen}")
    print("=" * 60 + "\n")

# Analiza paquetes capturados

def analizar_paquete(paquete):
    if not paquete.haslayer(IP) or not paquete.haslayer(TCP):
        return
    
    ip_layer = paquete[IP]
    tcp_layer = paquete[TCP]
    
    ip_origen = ip_layer.src
    ip_destino = ip_layer.dst
    puerto_destino = tcp_layer.dport
    flags = tcp_layer.flags
    
    # Solo paquetes a nuestra IP
    if ip_destino != IP_PROTEGIDA:
        return
    
    # Detectar SYN puro
    if flags == 0x02:  # Solo SYN, sin ACK ni otros flags
        # Puerto sospechoso
        if puerto_destino not in PUERTOS_COMUNES:
            registrar_evento(ip_origen, puerto_destino)
            bloquear_ip(ip_origen)


# Inicia el sniffer

def iniciar_sniffer():
    print("\n" + "=" * 60)
    print(" BLUE TEAM - SNIFFER DE DEFENSA")
    print("=" * 60)
    print(f" IP Protegida: {IP_PROTEGIDA}")
    print(f" Puertos Comunes: {sorted(PUERTOS_COMUNES)}")
    print(f" Log: {ARCHIVO_LOG}")
    print(f" Bloqueados: {ARCHIVO_BLOQUEADOS}")
    print("=" * 60)
    print("\n[INFO] Capturando paquetes...")
    print("[INFO] Ctrl+C para detener\n")
    
    try:
        sniff(filter="tcp", prn=analizar_paquete, store=0)
    except KeyboardInterrupt:
        print("\n[INFO] Sniffer detenido")
        print(f"[INFO] IPs bloqueadas: {len(ips_bloqueadas)}")
    except PermissionError:
        print("\n[ERROR] Requiere permisos de administrador")
        print("[ERROR] Ejecute: sudo python3 blue_team/sniffer_defense.py")
    except Exception as e:
        print(f"\n[ERROR] {e}")


# Funcion principal

def main():
    inicializar_logs()
    iniciar_sniffer()


if __name__ == "__main__":
    main()
