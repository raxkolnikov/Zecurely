import socket
from utils import create_server_context

HOST = "0.0.0.0"
PORT = 9000

def start_server():
    context = create_server_context()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind((HOST, PORT))
    sock.listen(5)

    print("[+] Secure TLS server listening...")

    while True:
        client_sock, addr = sock.accept()
        conn = context.wrap_socket(client_sock, server_side=True)

        print(f"[+] Secure connection from {addr}")

        while True:
            data = conn.recv(4096)
            if not data:
                break
            print("Client:", data.decode())

if __name__ == "__main__":
    start_server()
