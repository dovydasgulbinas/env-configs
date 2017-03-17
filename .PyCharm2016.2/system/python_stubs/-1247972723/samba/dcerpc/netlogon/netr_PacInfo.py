# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_PacInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    auth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    auth_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expansionroom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pac_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    principal_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



