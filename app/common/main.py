from typing import  List


class Participant:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ConferenceFullException(Exception):
    pass


class Conference:
    '''
    The main container to keep track of Conference and their tickets
    '''
    total_tickets: int
    confrence_info: str
    remaining_tickets: int
    participants: List(Participant)
    conference_date: str

    def __init__(self, **kwargs):
        self.total_tickets = self.remaining_tickets = kwargs.setdefault('total_tickets', '50')
        self.conference_info = kwargs.setdefault('conference_info', 'Unknown')
        self.conference_date = kwargs.setdefault('conference_date', 'Unknown')

    def buy_ticket(self, participant_name, participant_age):
        '''
        reserves a ticket for a participant
        '''
        if self.remaining_tickets == 0:
            raise ConferenceFullException("no more tickets is available")
        participant = Participant(participant_name, participant_age)
        self.remaining_tickets -= 1
        self.participants.push(participant)