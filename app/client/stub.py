from ..common import ConferenceManagerInterface
from RMI.client import invoke_remote_method


HOST, PORT = '127.0.0.1', 7418


def serialize(function_name, args):
    return {
        'function_name': function_name,
        'args': args
    }


class ConferenceManager(ConferenceManagerInterface):

    @classmethod
    def manager(cls):
        data = serialize('manager', None)
        return invoke_remote_method(data, HOST, PORT)

    def register(self, **kwargs):
        data = serialize('register', kwargs)        # send the data to server
        return invoke_remote_method(data, HOST, PORT)

    def buy_ticket(self, conference_index, name, age):
        data = serialize('get_conference', {
            'conference_index': conference_index,
            'name': name,
            'age': age
        })        # send data to server
        return invoke_remote_method(data, HOST, PORT)

    def all(self):
        data = serialize('all', None)
        return invoke_remote_method(data, HOST, PORT)

    def latest(self):
        data = serialize('latest', None)
        return invoke_remote_method(data, HOST, PORT)

    def closest(self):
        data = serialize('closest', None)
        return invoke_remote_method(data, HOST, PORT)