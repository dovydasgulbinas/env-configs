# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsGetNCChangesRequest5(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    destination_dsa_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended_op = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fsmo_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_ndr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_object_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    naming_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replica_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dsa_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uptodateness_vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



