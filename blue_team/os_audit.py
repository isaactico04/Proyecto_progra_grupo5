"""
Blue Team - OS Audit Script
Responsable: Kennan Sanchez (Blue Team)

Este script realiza una auditoría del sistema operativo Ubuntu Server para:
- Listar usuarios del sistema
- Verificar servicios activos
- Detectar puertos abiertos
"""

import subprocess
import os
from datetime import datetime


def main():
    """Función principal que ejecuta la auditoría del sistema."""
    
    print("=" * 60)
    print(" BLUE TEAM - AUDITORIA DEL SISTEMA OPERATIVO")
    print("=" * 60)
    print(f" Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    #Variable para guardar todo el resultado
    resultado_completo = ""
    
    #Agregar encabezado al archivo
    resultado_completo += "=" * 60 + "\n"
    resultado_completo += " AUDITORIA DEL SISTEMA OPERATIVO - UBUNTU SERVER\n"
    resultado_completo += "=" * 60 + "\n"
    resultado_completo += f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    resultado_completo += "\n\n"
    
    #Listar Usuarios
    print("\n1. Obteniendo usuarios del sistema...")
    resultado_completo += "=" * 60 + "\n"
    resultado_completo += "USUARIOS DEL SISTEMA (/etc/passwd)\n"
    resultado_completo += "=" * 60 + "\n\n"
    
    try:
        #Leer el archivo /etc/passwd
        with open("/etc/passwd", "r") as archivo:
            usuarios = archivo.read()
            print(usuarios)
            resultado_completo += usuarios
    except Exception as e:
        print(f"Error al leer usuarios: {e}")
        resultado_completo += f"Error al leer usuarios: {e}\n"
    
    resultado_completo += "\n\n"
    
    #Listar servicios activos
    print("\n2. Obteniendo servicios activos...")
    resultado_completo += "=" * 60 + "\n"
    resultado_completo += "SERVICIOS ACTIVOS (systemctl)\n"
    resultado_completo += "=" * 60 + "\n\n"
    
    try:
        # Ejecutar comando systemctl para listar servicios
        resultado = subprocess.run(
            ["systemctl", "list-units", "--type=service", "--state=running", "--no-pager"],
            capture_output=True,
            text=True
        )
        servicios = resultado.stdout
        print(servicios)
        resultado_completo += servicios
    except Exception as e:
        print(f"Error al obtener servicios: {e}")
        resultado_completo += f"Error al obtener servicios: {e}\n"
    
    resultado_completo += "\n\n"
    
    #Listar puertos abiertos
    print("\n3. Obteniendo puertos abiertos...")
    resultado_completo += "=" * 60 + "\n"
    resultado_completo += "PUERTOS ABIERTOS (ss -tuln)\n"
    resultado_completo += "=" * 60 + "\n\n"
    
    try:
        #Ejecutar comando ss para listar puertos
        resultado = subprocess.run(
            ["ss", "-tuln"],
            capture_output=True,
            text=True
        )
        puertos = resultado.stdout
        print(puertos)
        resultado_completo += puertos
    except Exception as e:
        print(f"Error al obtener puertos: {e}")
        resultado_completo += f"Error al obtener puertos: {e}\n"
    
    resultado_completo += "\n\n"
    resultado_completo += "=" * 60 + "\n"
    resultado_completo += "FIN DE LA AUDITORIA\n"
    resultado_completo += "=" * 60 + "\n"
    
    #Guardar archivos
    print("\n4. Guardando resultados...")
    
    #Crear directorio blue_team si no existe
    if not os.path.exists("blue_team"):
        os.makedirs("blue_team")
        print("✓ Directorio blue_team creado")
    
    #Guardar en blue_team/log_events.txt
    with open("blue_team/log_events.txt", "w") as archivo:
        archivo.write(resultado_completo)
    print("✓ Archivo guardado: blue_team/log_events.txt")
    
    #Crear directorio docs/evidencias si no existe
    if not os.path.exists("docs/evidencias"):
        os.makedirs("docs/evidencias")
        print("✓ Directorio docs/evidencias creado")
    
    # Guardar copia en docs/evidencias/os_audit_log.txt
    with open("docs/evidencias/os_audit_log.txt", "w") as archivo:
        archivo.write(resultado_completo)
    print("✓ Archivo guardado: docs/evidencias/os_audit_log.txt")
    
    print("\n" + "=" * 60)
    print(" ✓ AUDITORIA COMPLETADA")
    print("=" * 60)
    print("\n Archivos generados:")
    print("   - blue_team/log_events.txt")
    print("   - docs/evidencias/os_audit_log.txt\n")


# Ejecutar el script
main()