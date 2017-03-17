# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class browse_election_request(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Criteria = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ServerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UpTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



