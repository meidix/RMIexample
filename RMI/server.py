import socketserver
import pickle


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(f'connection with {self.client_address[0]} established')
        self.data = pickle.loads(self.request.recv(1024))
        response = pickle.dumps(f'fuck {self.data}')
        self.request.sendall(response)
