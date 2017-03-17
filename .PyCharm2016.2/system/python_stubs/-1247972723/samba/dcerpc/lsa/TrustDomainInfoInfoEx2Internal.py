# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/lsa.so
# by generator 1.143
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class TrustDomainInfoInfoEx2Internal(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    forest_trust_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forest_trust_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info_ex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



