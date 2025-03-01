# SilentShell

SilentShell is a lightweight tool designed to provide a secure and discreet remote shell. Its goal is to enable stealthy command execution on remote systems.

## Features
- Secure remote shell
- Low resource consumption
- Easy to set up and deploy
- Encrypted communication

## Installation

Clone the repository:

```sh
git clone https://github.com/T4skor/SilentShell.git
cd SilentShell
```

Compile the project if necessary:

```sh
make
```

## Usage

Run the server on the target machine:

```sh
./SilentShell -s
```

Connect from the client:

```sh
./SilentShell -c <SERVER_IP>
```

## Requirements
- Linux or Windows
- Dependencies: `openssl`, `libssh`, `gcc`

## Contributions

Contributions are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-new`).
3. Commit and push your changes (`git commit -m "Description" && git push origin feature-new`).
4. Open a Pull Request.

## Security

SilentShell employs encryption to secure communications, but it is recommended to use it in controlled environments and review the code to adapt it to your needs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or suggestions, feel free to open an issue in the repository.
