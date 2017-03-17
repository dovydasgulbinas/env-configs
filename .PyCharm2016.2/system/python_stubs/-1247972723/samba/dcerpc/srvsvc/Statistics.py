# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/srvsvc.so
# by generator 1.143
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class Statistics(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    avresponse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bigbufneed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytesrcvd_high = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytesrcvd_low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytessent_high = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytessent_low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    devopens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fopens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jobsqueued = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    permerrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwerrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reqbufneed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serrorout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sopens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stimeouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    syserrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



