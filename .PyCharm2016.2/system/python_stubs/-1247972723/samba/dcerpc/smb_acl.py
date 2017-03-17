# encoding: utf-8
# module samba.dcerpc.smb_acl
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/smb_acl.so
# by generator 1.143
""" smb_acl DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

SMB_ACL_EXECUTE = 1

SMB_ACL_FIRST_ENTRY = 0

SMB_ACL_GROUP = 3

SMB_ACL_GROUP_OBJ = 4

SMB_ACL_MASK = 6

SMB_ACL_NEXT_ENTRY = 1

SMB_ACL_OTHER = 5
SMB_ACL_READ = 4

SMB_ACL_TAG_INVALID = 0

SMB_ACL_TYPE_ACCESS = 0
SMB_ACL_TYPE_DEFAULT = 1

SMB_ACL_USER = 1

SMB_ACL_USER_OBJ = 2

SMB_ACL_WRITE = 2

# no functions
# classes

class entry(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    a_perm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    a_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class group(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class t(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    acl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class user(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wrapper(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    access_acl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_acl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



