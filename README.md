# Reverse Shell Script for Linux

This Python script sets up a reverse shell and configures it to run on startup as a systemd service. It connects to a remote server and listens for incoming commands. The script is designed for Linux systems.

## Features
- **Reverse Shell**: The script establishes a reverse shell connection to a remote host on a specified IP and port.
- **Startup Configuration**: It creates a systemd service that ensures the script runs on system startup.
- **Error Handling**: Basic error handling is implemented for socket and systemd service creation.

## Prerequisites
- Linux-based operating system.
- Python 3 installed.
- `systemd` for creating the service.

## Configuration
Before running the script, make sure to update the following variables:
- `RHOST`: The IP address or domain of the remote host where the reverse shell will connect.
- `RPORT`: The port on the remote host to connect to.

### Example:
```python
RHOST = "192.168.1.xxx"
RPORT = 8080
```

## Usage

### 1. Run the script:
To run the script, execute the Python file:

```bash
python3 /path/to/script.py
```

### 2. Service Configuration:
The script will automatically create a systemd service to run the reverse shell script on system startup.

- The service will be created at `/etc/systemd/system/revshell.service`.
- The service will run as the `root` user and restart if it fails.

### 3. Enable and Start the Service:
Once the script is executed, it will configure the service to run at startup using `systemd`.

## Security Warning
This script is intended for educational purposes only. Unauthorized access to computer systems is illegal and unethical. Always ensure you have permission before running any scripts that interact with external networks.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
