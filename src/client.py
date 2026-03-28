import socket
from utils import create_client_context

HOST = "127.0.0.1"
PORT = 9000

def start_client():
    context = create_client_context()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = context.wrap_socket(sock, server_hostname=HOST)

    conn.connect((HOST, PORT))
    print("[+] Connected securely via TLS")

    while True:
        msg = input("You: ")
        conn.sendall(msg.encode())

if __name__ == "__main__":
    start_client()
