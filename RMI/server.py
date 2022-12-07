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


class Skeleton(TCPHandlerWithException):
    obj_class = None
    extra_kwargs = None

    @classmethod
    def set_object(cls, obj):
        if not hasattr(cls, 'obj'):
            cls.obj = obj
        return cls

    def __init__(self, *args, **kwargs):
        if not self.obj and not self.obj_class:
            raise ValueError('''either the remote object should be given through the set_obj
                                function or the object singleton should be assinged to the
                                obj_class attribute''')

        if not self.obj and self.obj_class:
            if not self.extra_kwargs:
                self.obj = self.obj_class()
            else:
                self.obj = self.obj_class(**self.extra_kwargs)
        return super().__init__(*args, **kwargs)

    def resolve_request(self):
        self.data = pickle.loads(self.request.recv(1024))
        response = self.invoke_method_on(self.obj)
        self.request.sendall(pickle.dumps(response))

    def invoke_method_on(self, obj):
        if hasattr(obj, self.data['function_name']):
            func = getattr(obj, self.data['function_name'])
            kwargs = self.data['args']
            if kwargs:
                result = func(**kwargs)
            else:
                result = func()
            return result
        raise KeyError('Remote Function Does Not Exist')


def run_server(socket: tuple, handler):
    with socketserver.TCPServer(socket, handler) as server:
        host, port = socket
        print(f"server started on {host}:{port}")
        server.serve_forever()