# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsGetNCChangesCtr1(__talloc.Object):
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

    extended_ret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mapping_ctr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    more_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    naming_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    old_highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dsa_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dsa_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uptodateness_vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __ndr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



