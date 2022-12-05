from RMI.server import TCPHandlerWithException, run_server
from RMI.registery import register_server, remove_server, REGISTERY_HOST, REGISTERY_PORT
from .conference_manager import ConferenceManager
import pickle


class Skeleton(TCPHandlerWithException):

    def __init__(self, *args, **kwargs):
        self.manager = ConferenceManager()
        return super().__init__(*args, **kwargs)

    def resolve_request(self):
        self.data = pickle.loads(self.request.recv(1024))
        response = self.invoke_method_on(self.manager)
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


def run():
    HOST, PORT = '127.0.0.1', 7418
    register_server('ConferenceManager', HOST, PORT, REGISTERY_HOST, REGISTERY_PORT)
    try:
        run_server((HOST, PORT), Skeleton)
    finally:
        remove_server('ConferenceManager', '127.0.0.1', 7894)