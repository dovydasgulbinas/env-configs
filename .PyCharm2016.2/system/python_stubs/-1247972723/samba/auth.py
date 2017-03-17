# encoding: utf-8
# module samba.auth
# from /usr/lib/python2.7/dist-packages/samba/auth.so
# by generator 1.143
""" Authentication and authorization support. """

# imports
import talloc as __talloc


# Variables with simple values

AUTH_SESSION_INFO_AUTHENTICATED = 2

AUTH_SESSION_INFO_DEFAULT_GROUPS = 1

AUTH_SESSION_INFO_SIMPLE_PRIVILEGES = 4

# functions

def admin_session(*args, **kwargs): # real signature unknown
    pass

def system_session(*args, **kwargs): # real signature unknown
    pass

def user_session(*args, **kwargs): # real signature unknown
    pass

# classes

class AuthContext(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


