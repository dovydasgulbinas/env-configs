# encoding: utf-8
# module samba.messaging
# from /usr/lib/python2.7/dist-packages/samba/messaging.so
# by generator 1.143
""" Internal RPC """
# no imports

# no functions
# classes

class Messaging(object):
    """
    Messaging(own_id=None)
    Create a new object that can be used to communicate with the peers in the specified messaging path.
    """
    def deregister(self, callback, msg_type): # real signature unknown; restored from __doc__
        """
        S.deregister(callback, msg_type) -> None
        Deregister a message handler
        """
        pass

    def irpc_all_servers(self, *args, **kwargs): # real signature unknown
        """
        S.irpc_servers_byname() -> list
        Get list of all registered names and the associated server_id values
        """
        pass

    def irpc_servers_byname(self, name): # real signature unknown; restored from __doc__
        """
        S.irpc_servers_byname(name) -> list
        Get list of server_id values that are registered for a particular name
        """
        return []

    def register(self, callback, msg_type=None): # real signature unknown; restored from __doc__
        """
        S.register(callback, msg_type=None) -> msg_type
        Register a message handler
        """
        pass

    def send(self, target, msg_type, data): # real signature unknown; restored from __doc__
        """
        S.send(target, msg_type, data) -> None
        Send a message
        """
        pass

    def __init__(self, own_id=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    server_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """local server id"""



