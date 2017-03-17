# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsReplicaModRequest1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    modify_fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    naming_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replica_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dra = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_dra_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



