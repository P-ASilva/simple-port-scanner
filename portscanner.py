import socket

def scan_ports(host, start_port, end_port):
    print(f"Scaneando p: {host} da porta {start_port} até a porta {end_port}")
    print("Isso pode levar um tempo, por favor aguarde...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # timeout of 1 second
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    print("Bem vindo ao scanner de portas!")
    print('\n')
    print("Que domínio IP quer scanear?")
    ip = input("Digite o IP: ")
    print("Agora digite o intervalo de portas que deseja scanear")
    start = int(input("Digite a porta inicial: "))
    end = int(input("Digite a porta final: "))
    scan_ports(ip, start, end)