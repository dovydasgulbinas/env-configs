# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_UasInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    auth_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_pw_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    computer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kickoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password_age = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pw_can_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pw_must_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    script_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



