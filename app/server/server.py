from RMI.server import TCPHandler, run_server
from .conference_manager import ConferenceManager
import pickle

def deserialize_data(data_bytes):
    return pickle.loads(data_bytes)

def serialize_data(data):
    return pickle.dumps(data)

class Skeleton(TCPHandler):

    def handle(self):
        super().handle()
        self.data = deserialize_data(self.request.recv(1024))
        manager = ConferenceManager()
        response = self.invoke_method_on(manager)
        self.request.sendall(serialize_data(response))

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
    run_server((HOST, PORT), Skeleton)
