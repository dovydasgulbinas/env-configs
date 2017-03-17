# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsblobs.so
# by generator 1.143
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class repsFromTo1(__talloc.Object):
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

    blobsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    consecutive_sync_failures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_attempt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_info_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replica_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    result_last_attempt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dsa_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dsa_obj_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transport_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



