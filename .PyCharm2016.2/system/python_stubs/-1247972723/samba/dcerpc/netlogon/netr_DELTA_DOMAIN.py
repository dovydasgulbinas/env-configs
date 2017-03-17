# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_DELTA_DOMAIN(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account_lockout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_create_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_logoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_to_chgpass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_password_age = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_password_age = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_password_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    oem_information = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password_history_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sdbuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecurityInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sequence_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



