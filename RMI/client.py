import socket
import pickle


HOST = '127.0.0.1'
PORT = 6454

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(pickle.dumps("hello world"))
    data = pickle.loads(sock.recv(1024))


print(f"recieved {data}!")