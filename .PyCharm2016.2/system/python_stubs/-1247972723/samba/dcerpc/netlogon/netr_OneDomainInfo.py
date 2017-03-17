# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_OneDomainInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dns_domainname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dns_forestname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domainname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_long1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_long2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_long3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_long4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_string2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_string3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_string4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trust_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



