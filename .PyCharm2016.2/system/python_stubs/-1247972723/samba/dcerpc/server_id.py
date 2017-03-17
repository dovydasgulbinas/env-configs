# encoding: utf-8
# module samba.dcerpc.server_id
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/server_id.so
# by generator 1.143
""" server_id DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

NONCLUSTER_VNN = 4294967295

SERVERID_UNIQUE_ID_NOT_TO_VERIFY = 18446744073709551615L

# no functions
# classes

class server_id(__talloc.Object):
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

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    task_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unique_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vnn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



