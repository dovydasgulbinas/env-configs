# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsReplicaAttrValMetaData(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    attribute_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    created = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_usn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    originating_change_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    originating_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    originating_usn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __ndr_size_binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



