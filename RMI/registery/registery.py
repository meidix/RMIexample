import random


class Server:

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.setdefault('name', 'Unknown')
        self.host = kwargs.setdefault('host', '127.0.0.1')
        self.port = kwargs.setdefault('port', random.randint(1024, 10000))


class Registrey:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Registrey, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, 'servers'):
            self.servers - []

    def get_server(self, name):
        index = self.servers.index(name)
        if index:
            server = self.servers[index]
            return server
        return

    def add_server(self, **kwargs):
        index = self.servers.index(kwargs['name'])
        if not index:
            server = Server(**kwargs)
            self.servers.append(server)
        else:
            raise ValueError("a server with this name has already been registered")

    def remove_server(self, name):
        index = self.servers.index(name)
        if index:
            server = self.servers.pop(index)
            return server
        return
