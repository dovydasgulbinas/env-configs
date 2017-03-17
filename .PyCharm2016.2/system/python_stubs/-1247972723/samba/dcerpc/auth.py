# encoding: utf-8
# module samba.dcerpc.auth
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/auth.so
# by generator 1.143
""" auth DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

SEC_AUTH_METHOD_KERBEROS = 2
SEC_AUTH_METHOD_NTLM = 1
SEC_AUTH_METHOD_UNAUTHENTICATED = 0

# no functions
# classes

class session_info(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    credentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    security_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    torture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unix_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unix_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class session_info_transport(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    exported_gssapi_credentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class user_info(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    acct_expiry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    acct_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    authenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bad_password_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    home_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_password_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logon_server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class user_info_dc(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm_session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class user_info_torture(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dc_sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_dc_sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class user_info_unix(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    sanitized_username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unix_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



