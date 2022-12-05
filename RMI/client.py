from .registery import get_server
from .utils import send_socket_request
from .exception import RemoteException


class StubMixin:
    _registery_host = None
    _registery_port = None
    _remote_obj = None

    def proxy(self, method, args):
        data_bytes = serialize(method, args)
        if not self._remote_obj:
            self._remote_obj = self.__class__.__name__
        return invoke_method_on_remote(data_bytes, self._remote_obj, (self._registery_host, self._registery_port))


def serialize(function_name, args):
    return {
        'function_name': function_name,
        'args': args or None
    }


def unwrap_exception(response):
    if isinstance(response, dict) and 'type' in response and response['type'] == 'error':
            raise RemoteException(f"the following error occured on the remote server:\n{response['error']}")
    return response


def invoke_method_on_remote(data, remote_obj, registery_address):
    rhost, rport = registery_address
    server_host, server_port = unwrap_exception(get_server(remote_obj, rhost, rport))
    response = unwrap_exception(send_socket_request(data, server_host, server_port))
    return response
