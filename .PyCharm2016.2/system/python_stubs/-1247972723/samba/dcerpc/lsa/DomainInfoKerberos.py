# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/lsa.so
# by generator 1.143
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DomainInfoKerberos(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    authentication_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock_skew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_tkt_lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_tkt_lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_tkt_renewaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



