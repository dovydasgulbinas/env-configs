# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/lsa.so
# by generator 1.143
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DefaultQuotaInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    max_wss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_wss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    non_paged_pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paged_pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pagefile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



