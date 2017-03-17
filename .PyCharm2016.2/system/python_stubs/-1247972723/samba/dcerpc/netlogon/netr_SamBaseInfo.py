# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_SamBaseInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    acct_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_password_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    failed_logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kickoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_failed_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_successful_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LMSessKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primary_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sub_auth_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



