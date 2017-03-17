# encoding: utf-8
# module samba.dcerpc.winbind
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/winbind.so
# by generator 1.143
""" winbind DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    winbind parent-child protocol
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class wbint_Principal(__talloc.Object):
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_Principals(__talloc.Object):
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

    num_principals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    principals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_RidArray(__talloc.Object):
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

    num_rids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_SidArray(__talloc.Object):
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

    num_sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_TransID(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    domain_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_TransIDArray(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    ids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_ids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_userinfo(__talloc.Object):
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

    acct_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    group_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    homedir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primary_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class wbint_userinfos(__talloc.Object):
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

    num_userinfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    userinfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class winbind(__dcerpc.ClientConnection):
    """
    winbind(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    winbind parent-child protocol
    """
    def DsrUpdateReadOnlyServerDnsRecords(self, site_name, dns_ttl, dns_names): # real signature unknown; restored from __doc__
        """ S.DsrUpdateReadOnlyServerDnsRecords(site_name, dns_ttl, dns_names) -> dns_names """
        pass

    def GetForestTrustInformation(self, trusted_domain_name, flags): # real signature unknown; restored from __doc__
        """ S.GetForestTrustInformation(trusted_domain_name, flags) -> forest_trust_info """
        pass

    def LogonControl(self, function_code, level, data): # real signature unknown; restored from __doc__
        """ S.LogonControl(function_code, level, data) -> query """
        pass

    def SamLogon(self, logon_level, logon, validation_level): # real signature unknown; restored from __doc__
        """ S.SamLogon(logon_level, logon, validation_level) -> (validation, authoritative) """
        pass

    def wbint_AllocateGid(self): # real signature unknown; restored from __doc__
        """ S.wbint_AllocateGid() -> gid """
        pass

    def wbint_AllocateUid(self): # real signature unknown; restored from __doc__
        """ S.wbint_AllocateUid() -> uid """
        pass

    def wbint_ChangeMachineAccount(self): # real signature unknown; restored from __doc__
        """ S.wbint_ChangeMachineAccount() -> None """
        pass

    def wbint_CheckMachineAccount(self): # real signature unknown; restored from __doc__
        """ S.wbint_CheckMachineAccount() -> None """
        pass

    def wbint_DsGetDcName(self, domain_name, domain_guid, site_name, flags): # real signature unknown; restored from __doc__
        """ S.wbint_DsGetDcName(domain_name, domain_guid, site_name, flags) -> dc_info """
        pass

    def wbint_Gid2Sid(self, gid): # real signature unknown; restored from __doc__
        """ S.wbint_Gid2Sid(gid) -> sid """
        pass

    def wbint_LookupGroupMembers(self, sid, type): # real signature unknown; restored from __doc__
        """ S.wbint_LookupGroupMembers(sid, type) -> members """
        pass

    def wbint_LookupName(self, domain, name, flags): # real signature unknown; restored from __doc__
        """ S.wbint_LookupName(domain, name, flags) -> (type, sid) """
        pass

    def wbint_LookupRids(self, domain_sid, rids): # real signature unknown; restored from __doc__
        """ S.wbint_LookupRids(domain_sid, rids) -> (domain_name, names) """
        pass

    def wbint_LookupSid(self, sid): # real signature unknown; restored from __doc__
        """ S.wbint_LookupSid(sid) -> (type, domain, name) """
        pass

    def wbint_LookupSids(self, sids): # real signature unknown; restored from __doc__
        """ S.wbint_LookupSids(sids) -> (domains, names) """
        pass

    def wbint_LookupUserAliases(self, sids): # real signature unknown; restored from __doc__
        """ S.wbint_LookupUserAliases(sids) -> rids """
        pass

    def wbint_LookupUserGroups(self, sid): # real signature unknown; restored from __doc__
        """ S.wbint_LookupUserGroups(sid) -> sids """
        pass

    def wbint_Ping(self, in_data): # real signature unknown; restored from __doc__
        """ S.wbint_Ping(in_data) -> out_data """
        pass

    def wbint_PingDc(self): # real signature unknown; restored from __doc__
        """ S.wbint_PingDc() -> dcname """
        pass

    def wbint_QueryGroupList(self): # real signature unknown; restored from __doc__
        """ S.wbint_QueryGroupList() -> groups """
        pass

    def wbint_QuerySequenceNumber(self): # real signature unknown; restored from __doc__
        """ S.wbint_QuerySequenceNumber() -> sequence """
        return ()

    def wbint_QueryUser(self, sid): # real signature unknown; restored from __doc__
        """ S.wbint_QueryUser(sid) -> info """
        pass

    def wbint_QueryUserList(self): # real signature unknown; restored from __doc__
        """ S.wbint_QueryUserList() -> users """
        pass

    def wbint_Sids2UnixIDs(self, domains, ids): # real signature unknown; restored from __doc__
        """ S.wbint_Sids2UnixIDs(domains, ids) -> ids """
        pass

    def wbint_Uid2Sid(self, uid): # real signature unknown; restored from __doc__
        """ S.wbint_Uid2Sid(uid) -> sid """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


