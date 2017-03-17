# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsGetDCInfo3(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    computer_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    computer_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dns_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_pdc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_rodc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    netbios_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntds_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntds_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



