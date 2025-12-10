INSTRUCCIONES DE USO – packet_attack.py
--------------------------------------

Descripción general:
El script packet_attack.py simula un ataque SYN controlado contra una máquina virtual
de laboratorio. El objetivo del script es generar tráfico TCP SYN de forma limitada,
permitiendo que el Blue Team pruebe mecanismos de detección y respuesta sin afectar
la disponibilidad de los servicios.

Requisitos:
- Python 3.x instalado
- Scapy instalado
- Ejecutar el script con privilegios de administrador (sudo)

Instalación de dependencias:

En Linux (Debian / Ubuntu / Kali):
sudo apt update
sudo apt install python3-pip
sudo pip3 install scapy

Estructura recomendada de carpetas:
- Carpeta del proyecto:
Proyecto_progra_avanzada/
red_team/
packet_attack.py
readme_packet_attack.txt


Uso del script:

Ejecutar siempre desde la raíz del proyecto y con permisos elevados.

Ejecución en Linux (Kali recomendado):
1. Abrir una terminal.
2. Ir a la carpeta principal del proyecto:

cd RUTA/AL/PROYECTO/Proyecto_progra_avanzada

3. Ejecutar el script con el siguiente formato:

sudo python3 red_team/packet_attack.py <IP_OBJETIVO> [PUERTO] [CANTIDAD]

---------------------------windows (mejor con kali) ---------------------------

cd "C:\Users\Isaac\Desktop\Proyecto_progra_avanzada"

py red_team\packet_attack.py <IP_OBJETIVO> <PUERTO> <CANTIDAD>


Parámetros:
- IP_OBJETIVO : Dirección IP de la máquina virtual.
- PUERTO      : Puerto de destino (opcional, por defecto 80).
- CANTIDAD    : Número de paquetes SYN a enviar (opcional, por defecto 20).

Ejemplo:
sudo python3 red_team/packet_attack.py 192.168.56.101 80 20

Funcionamiento del programa:
- Genera paquetes TCP con la bandera SYN.
- Envía los paquetes de forma controlada (con retrasos entre envíos).
- No realiza flood ni denegación de servicio.
- El tráfico generado puede ser detectado por un sniffer del Blue Team.

Salida del programa:
- En consola se muestra:
  - IP objetivo
  - Puerto destino
  - Cantidad de paquetes enviados
  - Confirmación de cada paquete SYN enviado
  - Fecha y hora de la ejecución

Este script no genera archivos automáticamente, ya que su propósito es producir
tráfico de red que será detectado y registrado por el Blue Team en su propio log.


Autores:
Red Team – Proyecto Programación Avanzada
