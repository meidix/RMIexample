from ..common import ConferenceManagerInterface
from RMI.client import serialize, invoke_remote_method
from RMI import SERVER_HOST, SERVER_PORT


class ConferenceManager(ConferenceManagerInterface):

    @classmethod
    def manager(cls):
        data = serialize('manager', None)
        return invoke_remote_method(data, SERVER_HOST, SERVER_PORT)

    def register(self, **kwargs):
        data = serialize('register', **kwargs)        # send the data to server
        return invoke_remote_method(data, SERVER_HOST, SERVER_PORT)

    def buy_ticket(self, conference_index, name, age):
        data = serialize('get_conference', {
            'conference_index': conference_index,
            'name': name,
            'age': age
        })        # send data to server
        return invoke_remote_method(data, SERVER_HOST, SERVER_PORT)

    def all(self):
        data = {
            'function_name': 'all',
            'args': None
        }
        return invoke_remote_method(data, SERVER_HOST, SERVER_PORT)

    def latest(self):
        data = serialize('latest', None)
        return invoke_remote_method(data, SERVER_HOST, SERVER_PORT)

    def closest(self):
        data = serialize('closest', None)
        return invoke_remote_method(data, SERVER_HOST, SERVER_PORT)