from ..common import ConferenceManagerInterface
from RMI.client import StubMixin
from RMI.registery import REGISTERY_HOST, REGISTERY_PORT


class ConferenceManager(ConferenceManagerInterface, StubMixin):

    _registery_host = REGISTERY_HOST
    _registery_port = REGISTERY_PORT

    def register(self, **kwargs):
        return self.proxy('register', kwargs)

    def buy_ticket(self, conference_index, name, age):
        return self.proxy('buy_ticket', {
            'conference_index': conference_index,
            'name': name,
            'age': age
        })

    def all(self):
        return self.proxy('all', None)

    def latest(self):
        return self.proxy('latest', None)

    def closest(self):
        return self.proxy('closest', None)
