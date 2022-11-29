import socket
import pickle


def invoke_remote_method(data, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(pickle.dumps(data))
        return pickle.loads(sock.recv(1024))


def serialize(function_name, args):
    return {
        'function_name': function_name,
        'args': args
    }