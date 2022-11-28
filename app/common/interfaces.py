from typing import Protocol, List
from .main import Conference


class ConferenceManagerInterface(Protocol):
    '''
    The container to keep track of all conferences and managing them
    '''
    conferences: List

    @classmethod
    def manager(cls):
        """
        returns a configured ConferenceManager
        """

    def register(self, **kwargs):
        '''
        gets the information of a conference, creates one and adds it to the conference list
        '''

    def buy_ticket(self, conference_index, name, age):
        '''
        buys a ticket from a conference, determined by index
        '''

    def all(self):
        '''returns a list of all the conferences that is available'''

    def latest(self):
        '''returns the last conference that has been registered'''

    def closest(self):
        '''returns the closest conference to current date'''