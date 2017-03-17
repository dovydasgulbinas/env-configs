# encoding: utf-8
# module samba.dcerpc.wkssvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/wkssvc.so
# by generator 1.143
""" wkssvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NetrWkstaUserInfo1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    logon_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_domains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



