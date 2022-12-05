import socketserver
import pickle


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(f'request from {self.client_address[0]}":{self.client_address[1]} recieved')
        return


class TCPHandlerWithException(TCPHandler):

    def handle(self) -> None:
        try:
            self.resolve_request()
        except Exception as error:
            self.handle_exception(error)

    def resolve_request(self):
        print(f'request from {self.client_address[0]}":{self.client_address[1]} recieved')
        self.request.sendall(b'')

    def handle_exception(self, error):
        response = {
            'type': 'error',
            'error': error
        }
        self.request.sendall(pickle.dumps(response))



def run_server(socket: tuple, handler):
    with socketserver.TCPServer(socket, handler) as server:
        host, port = socket
        print(f"server started on {host}:{port}")
        server.serve_forever()