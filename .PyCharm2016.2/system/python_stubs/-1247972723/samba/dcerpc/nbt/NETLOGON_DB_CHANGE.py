# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NETLOGON_DB_CHANGE(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dbchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    db_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_format_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pulse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    random = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serial_lo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unicode_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unicode_pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



