import socket
import pickle




def serialize(function_name, args):
    return {
        'function_name': function_name,
        'args': args or None
    }