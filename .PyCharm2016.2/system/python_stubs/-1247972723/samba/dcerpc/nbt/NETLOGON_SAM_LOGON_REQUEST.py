# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NETLOGON_SAM_LOGON_REQUEST(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    acct_control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    computer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm20_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lmnt_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mailslot_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    request_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



