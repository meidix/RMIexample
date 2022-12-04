import socket
import pickle

def send_socket_request(data, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(pickle.dumps(data))
        result = sock.recv(1024)
        return pickle.loads(result)
