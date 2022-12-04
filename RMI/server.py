import socketserver


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(f'request from {self.client_address[0]}":{self.client_address[1]} recieved')
        return


def run_server(socket: tuple, handler):
    with socketserver.TCPServer(socket, handler) as server:
        host, port = socket
        print(f"server started on {host}:{port}")
        server.serve_forever()