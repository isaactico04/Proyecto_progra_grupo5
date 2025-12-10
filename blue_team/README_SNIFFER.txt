INSTRUCCIONES DE USO – sniffer_defense.py
-----------------------------------------

Requisitos:
- Python 3.x
- pip3 install scapy
- Ejecutar en VM Blue Team (Linux)
- Permisos de administrador (sudo)

Ejecucion:
1. cd Proyecto_progra_grupo5-main
2. sudo python3 blue_team/sniffer_defense.py
3. Ctrl+C para detener

NOTA: El script detecta automaticamente la IP de la maquina donde se ejecuta.

Archivos generados:
- blue_team/defense_log.txt
- blue_team/blocked_ips.txt

Que hace:
- Detecta paquetes SYN a puertos sospechosos
- Registra IPs atacantes
- Sugiere comando UFW para bloquear

Bloquear IP manualmente:
sudo ufw deny from <IP_ATACANTE>
sudo ufw status
