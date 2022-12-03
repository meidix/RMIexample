import pickle

from ..server import *
from .registery import Registrey



REGISTERY_HOST = '127.0.0.1'
REGISTERY_PORT  = 7894


class RegisteryTCPHandler(TCPHandler):

    def __init__(self, *args, **kwargs):
        self.registery = Registrey()

    def handle(self):
        super().handle()
        self.data = pickle.loads(self.request.recv(1024))
        result = self.dispatch_action()
        return pickle.dumps(result)

    def dispatch_action(self):
        if self.data['action'] == 'add':
            pass

def run():
    print(f'''
    The Registery Is Running On Host {REGISTERY_HOST} With Port {REGISTERY_PORT}
    ''')
    run_server((REGISTERY_HOST, REGISTERY_PORT), RegisteryTCPHandler)