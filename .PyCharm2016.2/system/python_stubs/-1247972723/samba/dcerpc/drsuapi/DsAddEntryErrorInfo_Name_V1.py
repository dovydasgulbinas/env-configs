# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsAddEntryErrorInfo_Name_V1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended_err = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id_matched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    problem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



