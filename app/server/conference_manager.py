from datetime import date
from ..common import ConferenceManagerInterface
from ..common.main import Conference

class ConferenceManager(ConferenceManagerInterface):
    @classmethod
    def manager(cls):
        instance = cls()
        return instance

    def register(self, **kwargs):
        conference = Conference(**kwargs)
        self.conferences.push(conference)

    def buy_ticket(self, conference_index, name, age):
        try:
            conference = self.conferences[conference_index]
        except:
            raise IndexError(f'conference with {conference_index} was not found')

        conference.buy_ticket(name, age)

    def all(self):
        return self.conferences

    def latest(self):
        return self.conferences[-1]

    def closest(self):
        closest = None
        for conference in self.conferences:
            if closest is None:
                closest = conference
                continue
            closest_difference = closest.conference_date - date.today()
            conference_difference = conference.conference_date - date.today()
            if conference_difference < closest_difference:
                closest = conference
        return closest