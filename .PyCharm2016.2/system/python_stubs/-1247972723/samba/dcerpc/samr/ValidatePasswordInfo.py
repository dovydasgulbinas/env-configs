# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/samr.so
# by generator 1.143
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class ValidatePasswordInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    bad_password_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_pwd_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fields_present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lockout_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwd_history = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwd_history_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



