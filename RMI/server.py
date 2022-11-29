import socketserver
import pickle


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(f'{self.client_address[0]} connected')


def run_server(socket: tuple, handler):
    with socketserver.TCPServer(socket, handler) as server:
        host, port = socket
        print(f"server started on {host}:{port}")
        server.serve_forever()