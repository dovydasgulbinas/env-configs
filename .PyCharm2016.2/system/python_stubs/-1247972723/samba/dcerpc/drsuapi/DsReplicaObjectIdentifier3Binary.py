# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsReplicaObjectIdentifier3Binary(__talloc.Object):
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

    binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __ndr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __ndr_size_binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __ndr_size_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __ndr_size_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



