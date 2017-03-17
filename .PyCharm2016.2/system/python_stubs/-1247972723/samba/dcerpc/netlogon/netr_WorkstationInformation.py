# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_WorkstationInformation(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dns_hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_long3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_long4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_string3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_string4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lsa_policy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    os_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    os_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sitename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supported_enc_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    workstation_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



