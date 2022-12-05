from .registery import get_server
from .utils import send_socket_request
from .exception import RemoteException

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
