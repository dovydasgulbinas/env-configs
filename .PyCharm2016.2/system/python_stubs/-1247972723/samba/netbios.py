# encoding: utf-8
# module samba.netbios
# from /usr/lib/python2.7/dist-packages/samba/netbios.so
# by generator 1.143
""" NetBIOS over TCP/IP support """
# no imports

# no functions
# classes

class Node(object):
    """
    Node()
    Create a new NetBIOS node
    """
    def name_status(self, name, dest, timeout=0, retries=0): # real signature unknown; restored from __doc__
        """
        S.name_status(name, dest, timeout=0, retries=0) -> (reply_from, name, status)
        Find the status of a name
        """
        pass

    def query_name(self, name, dest, broadcast=True, wins=False, timeout=0, retries=3): # real signature unknown; restored from __doc__
        """
        S.query_name(name, dest, broadcast=True, wins=False, timeout=0, retries=3) -> (reply_from, name, reply_addr)
        Query for a NetBIOS name
        """
        pass

    def refresh_name(self, name, address, dest, nb_flags=0, broadcast=True, ttl=0, timeout=0, retries=0): # real signature unknown; restored from __doc__
        """
        S.refresh_name(name, address, dest, nb_flags=0, broadcast=True, ttl=0, timeout=0, retries=0) -> (reply_from, name, reply_addr, rcode)
        release a previously registered name
        """
        pass

    def register_name(self, name, address, dest, register_demand=True, broadcast=True, multi_homed=True, ttl=0, timeout=0, retries=0): # real signature unknown; restored from __doc__
        """
        S.register_name(name, address, dest, register_demand=True, broadcast=True, multi_homed=True, ttl=0, timeout=0, retries=0) -> (reply_from, name, reply_addr, rcode)
        Register a new name
        """
        pass

    def release_name(self, name, address, dest, nb_flags=0, broadcast=None, timeout=0, retries=3): # real signature unknown; restored from __doc__
        """
        S.release_name(name, address, dest, nb_flags=0, broadcast=true, timeout=0, retries=3) -> (reply_from, name, reply_addr, rcode)
        release a previously registered name
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


