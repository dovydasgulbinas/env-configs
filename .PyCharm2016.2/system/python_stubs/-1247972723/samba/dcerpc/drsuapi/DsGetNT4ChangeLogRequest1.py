# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsGetNT4ChangeLogRequest1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preferred_maximum_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    restart_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    restart_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



