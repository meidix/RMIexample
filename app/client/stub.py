from common import ConferenceManagerInterface

def serialize(function_name, args):
    return {
        'function_name': function_name,
        'args': args
    }


class ConferenceManager(ConferenceManagerInterface):
    def register(self, **kwargs):
        data = serialize('register', kwargs)        # send the data to server

    def buy_ticket(self, conference_index, name, age):
        data = serialize('get_conference', {
            'conference_index': conference_index,
            'name': name,
            'age': age
        })        # send data to server

    def all(self):
        data = serialize('all', None)

    def latest(self):
        data = serialize('latest', None)

    def closest(self):
        data = serialize('closest', None)