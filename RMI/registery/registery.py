import random
from ..utils import send_socket_request

class Server:

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.setdefault('name', 'Unknown')
        self.host = kwargs.setdefault('host', '127.0.0.1')
        self.port = kwargs.setdefault('port', random.randint(1024, 10000))


class Registery(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Registery, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, 'servers'):
            self.servers = []

    def _retrieve(self, name):
        for server in self.servers:
            if server.name == name:
                return server
        return None

    def get_server(self, name):
        server = self._retrieve(name)
        if server:
            return (server.host, server.port)
        raise ValueError("There is no entry for this object")

    def add_server(self, **kwargs):
        server = self._retrieve(kwargs['name'])
        if server:
            raise ValueError("an object with this name has already been registered")
        server = Server(**kwargs)
        self.servers.append(server)
        return "success"

    def remove_server(self, name):
        server = self._retrieve(name)
        if not server:
            raise ValueError("This object has no record on the registery")
        index = self.servers.index(server)
        server = self.servers.pop(index)
        return server


def register_server(server_name, host, port, registery_host, registery_port):
    request = {
        'action': 'add',
        'payload': {
            'name': server_name,
            'host': host,
            'port': port
        }
    }
    return send_socket_request(request, registery_host, registery_port)


def remove_server(server_name, registery_host, registery_port):
    request = {
        'action': 'remove',
        'payload': {
            'name': server_name
        }
    }
    return send_socket_request(request, registery_host, registery_port)

def get_server(server_name, registery_host, registery_port):
    request = {
        'action': "get",
        'payload': {
            'name': server_name
        }
    }
    return send_socket_request(request, registery_host, registery_port)