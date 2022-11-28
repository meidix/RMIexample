import socket
import pickle

HOST = "127.0.0.1"
PORT = 6454

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print(f"Client {addr} connected")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            request = pickle.loads(data)
            response = f'{request} was recieved at the server'
            conn.sendall(pickle.dumps(response))