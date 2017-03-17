# encoding: utf-8
# module samba.dcerpc.irpc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/irpc.so
# by generator 1.143
""" irpc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

DREPL_INFRASTRUCTURE_MASTER = 2

DREPL_NAMING_MASTER = 3

DREPL_PDC_MASTER = 4

DREPL_RID_MASTER = 1

DREPL_SCHEMA_MASTER = 0

IRPC_FLAG_REPLY = 1

NBTD_INFO_STATISTICS = 0

SMBSRV_INFO_SESSIONS = 0
SMBSRV_INFO_TCONS = 1

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """ abstract_syntax() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class creds(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class header(__talloc.Object):
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

    callid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    creds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    if_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class irpc(__dcerpc.ClientConnection):
    """
    irpc(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    """
    def dnssrv_reload_dns_zones(self): # real signature unknown; restored from __doc__
        """ S.dnssrv_reload_dns_zones() -> None """
        pass

    def dnsupdate_RODC(self, dom_sid, site_name, dns_ttl, dns_names): # real signature unknown; restored from __doc__
        """ S.dnsupdate_RODC(dom_sid, site_name, dns_ttl, dns_names) -> dns_names """
        pass

    def dreplsrv_refresh(self): # real signature unknown; restored from __doc__
        """ S.dreplsrv_refresh() -> None """
        pass

    def drepl_takeFSMORole(self, role): # real signature unknown; restored from __doc__
        """ S.drepl_takeFSMORole(role) -> None """
        pass

    def drepl_trigger_repl_secret(self, user_dn): # real signature unknown; restored from __doc__
        """ S.drepl_trigger_repl_secret(user_dn) -> None """
        pass

    def kdc_check_generic_kerberos(self, generic_request): # real signature unknown; restored from __doc__
        """ S.kdc_check_generic_kerberos(generic_request) -> generic_reply """
        pass

    def nbtd_getdcname(self, domainname, ip_address, my_computername, my_accountname, account_control, domain_sid): # real signature unknown; restored from __doc__
        """ S.nbtd_getdcname(domainname, ip_address, my_computername, my_accountname, account_control, domain_sid) -> dcname """
        pass

    def nbtd_information(self, level): # real signature unknown; restored from __doc__
        """ S.nbtd_information(level) -> info """
        pass

    def nbtd_proxy_wins_challenge(self, name, num_addrs, addrs): # real signature unknown; restored from __doc__
        """ S.nbtd_proxy_wins_challenge(name, num_addrs, addrs) -> (num_addrs, addrs) """
        pass

    def nbtd_proxy_wins_release_demand(self, name, num_addrs, addrs): # real signature unknown; restored from __doc__
        """ S.nbtd_proxy_wins_release_demand(name, num_addrs, addrs) -> None """
        pass

    def samba_terminate(self, reason): # real signature unknown; restored from __doc__
        """ S.samba_terminate(reason) -> None """
        pass

    def smbsrv_information(self, level): # real signature unknown; restored from __doc__
        """ S.smbsrv_information(level) -> info """
        pass

    def uptime(self): # real signature unknown; restored from __doc__
        """ S.uptime() -> start_time """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class name_record(__talloc.Object):
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

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class name_records(__talloc.Object):
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

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class nbtd_proxy_wins_addr(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class nbtd_statistics(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    query_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    register_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    release_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_sent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class smbsrv_sessions(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    num_sessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class smbsrv_session_info(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    auth_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    client_ip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connect_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_use_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class smbsrv_tcons(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    num_tcons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tcons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class smbsrv_tcon_info(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    client_ip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connect_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_use_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    share_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



