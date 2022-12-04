from .registery import get_server
from .utils import send_socket_request

def serialize(function_name, args):
    return {
        'function_name': function_name,
        'args': args or None
    }


def invoke_method_on_remote(data, remote_obj, registery_address):
    rhost, rport = registery_address
    server_host, server_port = get_server(remote_obj, rhost, rport)
    return send_socket_request(data, server_host, server_port)
