# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_DELTA_USER(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    acct_expiry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    acct_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_password_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    country_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lmpassword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm_password_present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntpassword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_password_present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password_expired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primary_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sdbuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecurityInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_private_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    workstations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



