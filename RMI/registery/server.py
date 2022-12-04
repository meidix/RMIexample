import pickle

from ..server import *
from .registery import Registery



REGISTERY_HOST = '127.0.0.1'
REGISTERY_PORT  = 7894


class RegisteryTCPHandler(TCPHandler):

    def __init__(self, *args, **kwargs):
        self.registery = Registery()
        return super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()
        self.data = pickle.loads(self.request.recv(1024))
        result = self.dispatch_action()
        response = pickle.dumps(result)
        self.request.sendall(response)

    def _get_args(self, data):
        args = data.get('payload', None)
        if not args:
            raise KeyError("server information not available")
        return args

    def dispatch_action(self):
        if not 'action' in self.data:
            raise KeyError(f'request body has no action')

        if self.data['action'] == 'add':
            args = self._get_args(self.data)
            return self.registery.add_server(**args)
        elif self.data['action'] == 'remove':
            args = self._get_args(self.data)
            return self.registery.remove_server(**args)
        elif self.data['action'] == 'get':
            args = self._get_args(self.data)
            return self.registery.get_server(**args)
        else:
            raise KeyError(f"action '{self.data['action']}' not available")


def run():
    print(f'''
    The Registery Is Running On Host {REGISTERY_HOST} With Port {REGISTERY_PORT}
    ''')
    run_server((REGISTERY_HOST, REGISTERY_PORT), RegisteryTCPHandler)