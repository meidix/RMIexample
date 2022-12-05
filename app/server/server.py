from RMI.server import Skeleton, run_server
from RMI.registery import register_server, remove_server, REGISTERY_HOST, REGISTERY_PORT
from .conference_manager import ConferenceManager


class ConferenceManagerSkeleton(Skeleton):
    obj_class = ConferenceManager
    extra_kwargs = None


def run():
    HOST, PORT = '127.0.0.1', 7418
    register_server(ConferenceManager, HOST, PORT, REGISTERY_HOST, REGISTERY_PORT)
    try:
        run_server((HOST, PORT), ConferenceManagerSkeleton)
    finally:
        remove_server('ConferenceManager', '127.0.0.1', 7894)