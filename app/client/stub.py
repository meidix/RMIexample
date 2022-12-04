from ..common import ConferenceManagerInterface
from RMI.client import serialize, invoke_method_on_remote
from RMI.registery import REGISTERY_HOST, REGISTERY_PORT


class ConferenceManager(ConferenceManagerInterface):

    @classmethod
    def manager(cls):
        data = serialize('manager', None)
        return invoke_method_on_remote(data, 'ConferenceManager', (REGISTERY_HOST, REGISTERY_PORT))

    def register(self, **kwargs):
        data = serialize('register', kwargs)        # send the data to server
        return invoke_method_on_remote(data, 'ConferenceManager', (REGISTERY_HOST, REGISTERY_PORT))

    def buy_ticket(self, conference_index, name, age):
        data = serialize('buy_ticket', {
            'conference_index': conference_index,
            'name': name,
            'age': age
        })        # send data to server
        return invoke_method_on_remote(data, 'ConferenceManager', (REGISTERY_HOST, REGISTERY_PORT))

    def all(self):
        data = {
            'function_name': 'all',
            'args': None
        }
        return invoke_method_on_remote(data, 'ConferenceManager', (REGISTERY_HOST, REGISTERY_PORT))

    def latest(self):
        data = serialize('latest', None)
        return invoke_method_on_remote(data, 'ConferenceManager', (REGISTERY_HOST, REGISTERY_PORT))

    def closest(self):
        data = serialize('closest', None)
        return invoke_method_on_remote(data, 'ConferenceManager', (REGISTERY_HOST, REGISTERY_PORT))
