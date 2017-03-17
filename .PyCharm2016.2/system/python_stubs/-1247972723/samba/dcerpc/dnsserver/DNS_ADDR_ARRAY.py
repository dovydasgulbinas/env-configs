# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsserver.so
# by generator 1.143
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DNS_ADDR_ARRAY(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AddrArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AddrCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MatchFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MaxCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    WordReserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



