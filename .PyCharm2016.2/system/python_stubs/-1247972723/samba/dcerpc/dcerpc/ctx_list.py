# encoding: utf-8
# module samba.dcerpc.dcerpc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dcerpc.so
# by generator 1.143
""" dcerpc DCE/RPC """

# imports
import talloc as __talloc


class ctx_list(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    abstract_syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_transfer_syntaxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transfer_syntaxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



