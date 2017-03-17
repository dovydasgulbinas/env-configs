# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_OsVersionInfoEx(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BuildNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CSDVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OSVersionInfoSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PlatformId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProductType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ServicePackMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ServicePackMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SuiteMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



