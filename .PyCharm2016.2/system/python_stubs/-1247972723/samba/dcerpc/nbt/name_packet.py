# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class name_packet(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    additional = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ancount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    answers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    arcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_trn_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nscount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nsrecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    questions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



