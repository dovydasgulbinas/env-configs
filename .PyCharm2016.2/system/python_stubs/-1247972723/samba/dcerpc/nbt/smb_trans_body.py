# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class smb_trans_body(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    byte_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mailslot_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_data_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_param_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_setup_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    opcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    param_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    param_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    setup_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_data_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_param_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trans_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



