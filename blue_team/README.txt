INSTRUCCIONES DE USO – os_audit.py
-----------------------------------------

Requisitos:
- Python 3.x instalado
- Permisos suficientes para leer /etc/passwd, ejecutar systemctl y usar ss

Estructura recomendada de carpetas del proyecto:
Proyecto_progra_avanzada/
  blue_team/os_audit.py
  docs/evidencias/   (se crea automáticamente al ejecutar el script)

Ejecución en Visual Studio Code:
1. Abrir VS Code y cargar la carpeta del proyecto.
2. Abrir la terminal integrada: Terminal → New Terminal
3. Navegar a la carpeta:
   cd blue_team
4. Ejecutar el script:
   python3 os_audit.py

Ejecución en Linux (terminal):
1. Abrir una terminal.
2. cd RUTA/AL/PROYECTO/Proyecto_progra_avanzada
3. python3 blue_team/os_audit.py

Salida generada:
- blue_team/log_events.txt
- docs/evidencias/os_audit_log.txt

Ambos incluyen:
- Fecha y hora de la auditoría
- Lista de usuarios del sistema
- Servicios activos
- Puertos abiertos
