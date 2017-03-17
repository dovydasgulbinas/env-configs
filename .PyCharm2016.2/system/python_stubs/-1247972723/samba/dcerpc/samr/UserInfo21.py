# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/samr.so
# by generator 1.143
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class UserInfo21(__talloc.Object):
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

    allow_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_password_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buf_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    country_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fields_present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm_owf_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm_password_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_owf_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_password_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password_expired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primary_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_data_sensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    workstations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



