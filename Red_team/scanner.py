
# RED TEAM — scanner.py
# Escáner básico de puertos con Nmap

# Uso:
#   python3 red_team/scanner.py (IP OBJETIVO)

# Requiere:
#   - nmap instalado en la máquina
#   - Python 3.x

# Funciones:
#   1) Recibe una IP como argumento.
#   2) Ejecuta nmap con flags -sS -sV -Pn.
#   3) Guarda la salida completa en docs/evidencias/nmap_scan.txt.
#   4) Muestra un resumen con los puertos abiertos.


import sys
import os
import subprocess
from datetime import datetime

# ---------------------------------------
# Verifica que se haya pasado una IP
# ---------------------------------------
def verificar_argumentos() -> str:
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python3 red_team/scanner.py <IP_OBJETIVO>")
        sys.exit(1)

    return sys.argv[1]

# ------------------------
# Ejecuta el comando nmap 
# ------------------------
def ejecutar_nmap(ip: str) -> subprocess.CompletedProcess:
    comando = [
        "nmap",
        "-sS",           # Escaneo SYN
        "-sV",           # Detecta versiones de servicios
        "-Pn",           # Omite ping (asume host activo)
        "-p", "22,80,443",
        ip
    ]

    print("[INFO] Ejecutando nmap...")
    print("[CMD] " + " ".join(comando))

    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )
        return resultado
    except FileNotFoundError:
        print("[ERROR] Nmap no está instalado. Instale con:")
        print("        sudo apt install nmap")
        sys.exit(1)

# ---------------------------------------
# Guarda la evidencia en docs/evidencias/
# ---------------------------------------
def guardar_evidencia(ip: str, resultado: subprocess.CompletedProcess) -> str:
    evidencia_dir = os.path.join("docs", "evidencias")
    os.makedirs(evidencia_dir, exist_ok=True)

    salida_path = os.path.join(evidencia_dir, "nmap_scan.txt")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(salida_path, "w", encoding="utf-8") as f:
        f.write("===== NMAP SCAN =====\n")
        f.write(f"Fecha y hora: {timestamp}\n")
        f.write(f"IP objetivo: {ip}\n")
        f.write(f"Comando: nmap -sS -sV -Pn -p 22,80,443 {ip}\n\n")

        f.write("===== STDOUT =====\n")
        f.write(resultado.stdout)
        f.write("\n===== STDERR =====\n")
        f.write(resultado.stderr)

    print(f"[OK] Evidencia guardada en: {salida_path}")
    return salida_path

# ---------------------------------------
# Muestra un resumen rápido en consola
# ---------------------------------------
def mostrar_resumen(resultado: subprocess.CompletedProcess) -> None:
    print("\n[INFO] Puertos abiertos detectados:")

    encontrados = False
    for linea in resultado.stdout.splitlines():
        if "/tcp" in linea and "open" in linea:
            print("  - " + linea.strip())
            encontrados = True

    if not encontrados:
        print("  (No se detectaron puertos abiertos o revisar el archivo .txt)")

# --------
# MAIN
# -----------
def main():
    ip = verificar_argumentos()
    resultado = ejecutar_nmap(ip)
    guardar_evidencia(ip, resultado)
    mostrar_resumen(resultado)
    print("\n[LISTO] Escaneo completado.")

if __name__ == "__main__":
    main()
