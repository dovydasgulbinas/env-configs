# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsReplicaKccDsaFailure(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dsa_obj_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dsa_obj_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_failure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_failures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



