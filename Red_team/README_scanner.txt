INSTRUCCIONES DE USO – scanner.py
---------------------------------

Requisitos:
- Python 3.x instalado
- Nmap instalado y agregado al PATH del sistema

En Linux (Debian/Ubuntu/Kali), por ejemplo:
sudo apt update
sudo apt install nmap

En Windows:
- Descargar Nmap desde: https://nmap.org/download.html
- Durante la instalación, marcar "Add Nmap to PATH" y aceptar instalar Npcap.

Estructura recomendada de carpetas:
- Carpeta del proyecto:
Proyecto_progra_avanzada/
Red_team/
scanner.py
docs/
evidencias/   (se crea automáticamente al ejecutar el script)

Ejecución en Linux:
1. Abrir una terminal.
2. Ir a la carpeta principal del proyecto:

cd RUTA/AL/PROYECTO/Proyecto_progra_avanzada

3. Ejecutar el script con:

python3 Red_team/scanner.py <IP_OBJETIVO>

Ejemplo: python3 Red_team/scanner.py 192.168.56.101

Ejecución en Windows (PowerShell o CMD):
1. Abrir PowerShell o Símbolo del sistema.
2. Ir a la carpeta donde está el script:

cd "C:\Users\Isaac\Desktop\Proyecto_progra_avanzada\Red_team"

(o la ruta donde se encuentre el archivo scanner.py)
3. Ejecutar el script con:
py scanner.py <IP_OBJETIVO>

Ejemplo:
py scanner.py 192.168.56.101

Salida generada:
- Carpeta creada automáticamente:
docs\evidencias\
- Archivo de evidencia:
docs\evidencias\nmap_scan.txt

El archivo nmap_scan.txt incluye:
- Fecha y hora del escaneo
- IP objetivo
- Comando nmap ejecutado
- Salida completa (STDOUT y STDERR) del escaneo

Además, en consola se muestra un resumen de los puertos abiertos detectados.
