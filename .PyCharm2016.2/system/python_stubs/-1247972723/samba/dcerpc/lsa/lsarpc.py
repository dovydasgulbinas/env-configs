# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/lsa.so
# by generator 1.143
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class lsarpc(__dcerpc.ClientConnection):
    """
    lsarpc(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Local Security Authority
    """
    def AddAccountRights(self, handle, sid, rights): # real signature unknown; restored from __doc__
        """ S.AddAccountRights(handle, sid, rights) -> None """
        pass

    def AddPrivilegesToAccount(self, handle, privs): # real signature unknown; restored from __doc__
        """ S.AddPrivilegesToAccount(handle, privs) -> None """
        pass

    def Close(self, handle): # real signature unknown; restored from __doc__
        """ S.Close(handle) -> handle """
        pass

    def CloseTrustedDomainEx(self, handle): # real signature unknown; restored from __doc__
        """ S.CloseTrustedDomainEx(handle) -> handle """
        pass

    def CreateAccount(self, handle, sid, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateAccount(handle, sid, access_mask) -> acct_handle """
        pass

    def CreateSecret(self, handle, name, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateSecret(handle, name, access_mask) -> sec_handle """
        pass

    def CreateTrustedDomain(self, policy_handle, info, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateTrustedDomain(policy_handle, info, access_mask) -> trustdom_handle """
        pass

    def CreateTrustedDomainEx(self, policy_handle, info, auth_info, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateTrustedDomainEx(policy_handle, info, auth_info, access_mask) -> trustdom_handle """
        pass

    def CreateTrustedDomainEx2(self, policy_handle, info, auth_info_internal, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateTrustedDomainEx2(policy_handle, info, auth_info_internal, access_mask) -> trustdom_handle """
        pass

    def Delete(self, handle): # real signature unknown; restored from __doc__
        """ S.Delete(handle) -> None """
        pass

    def DeleteObject(self, handle): # real signature unknown; restored from __doc__
        """ S.DeleteObject(handle) -> handle """
        pass

    def DeleteTrustedDomain(self, handle, dom_sid): # real signature unknown; restored from __doc__
        """ S.DeleteTrustedDomain(handle, dom_sid) -> None """
        pass

    def EnumAccountRights(self, handle, sid): # real signature unknown; restored from __doc__
        """ S.EnumAccountRights(handle, sid) -> rights """
        pass

    def EnumAccounts(self, handle, resume_handle, num_entries): # real signature unknown; restored from __doc__
        """ S.EnumAccounts(handle, resume_handle, num_entries) -> (resume_handle, sids) """
        pass

    def EnumAccountsWithUserRight(self, handle, name): # real signature unknown; restored from __doc__
        """ S.EnumAccountsWithUserRight(handle, name) -> sids """
        pass

    def EnumPrivs(self, handle, resume_handle, max_count): # real signature unknown; restored from __doc__
        """ S.EnumPrivs(handle, resume_handle, max_count) -> (resume_handle, privs) """
        pass

    def EnumPrivsAccount(self, handle): # real signature unknown; restored from __doc__
        """ S.EnumPrivsAccount(handle) -> privs """
        pass

    def EnumTrustDom(self, handle, resume_handle, max_size): # real signature unknown; restored from __doc__
        """ S.EnumTrustDom(handle, resume_handle, max_size) -> (resume_handle, domains) """
        pass

    def EnumTrustedDomainsEx(self, handle, resume_handle, max_size): # real signature unknown; restored from __doc__
        """ S.EnumTrustedDomainsEx(handle, resume_handle, max_size) -> (resume_handle, domains) """
        pass

    def GetSystemAccessAccount(self, handle): # real signature unknown; restored from __doc__
        """ S.GetSystemAccessAccount(handle) -> access_mask """
        pass

    def GetUserName(self, system_name, account_name, authority_name): # real signature unknown; restored from __doc__
        """ S.GetUserName(system_name, account_name, authority_name) -> (account_name, authority_name) """
        pass

    def LookupNames(self, handle, names, sids, level, count): # real signature unknown; restored from __doc__
        """ S.LookupNames(handle, names, sids, level, count) -> (domains, sids, count) """
        pass

    def LookupNames2(self, handle, names, sids, level, count, lookup_options, client_revision): # real signature unknown; restored from __doc__
        """ S.LookupNames2(handle, names, sids, level, count, lookup_options, client_revision) -> (domains, sids, count) """
        pass

    def LookupNames3(self, handle, names, sids, level, count, lookup_options, client_revision): # real signature unknown; restored from __doc__
        """ S.LookupNames3(handle, names, sids, level, count, lookup_options, client_revision) -> (domains, sids, count) """
        pass

    def LookupNames4(self, names, sids, level, count, lookup_options, client_revision): # real signature unknown; restored from __doc__
        """ S.LookupNames4(names, sids, level, count, lookup_options, client_revision) -> (domains, sids, count) """
        pass

    def LookupPrivDisplayName(self, handle, name, language_id, language_id_sys): # real signature unknown; restored from __doc__
        """ S.LookupPrivDisplayName(handle, name, language_id, language_id_sys) -> (disp_name, returned_language_id) """
        pass

    def LookupPrivName(self, handle, luid): # real signature unknown; restored from __doc__
        """ S.LookupPrivName(handle, luid) -> name """
        pass

    def LookupPrivValue(self, handle, name): # real signature unknown; restored from __doc__
        """ S.LookupPrivValue(handle, name) -> luid """
        pass

    def LookupSids(self, handle, sids, names, level, count): # real signature unknown; restored from __doc__
        """ S.LookupSids(handle, sids, names, level, count) -> (domains, names, count) """
        pass

    def LookupSids2(self, handle, sids, names, level, count, lookup_options, client_revision): # real signature unknown; restored from __doc__
        """ S.LookupSids2(handle, sids, names, level, count, lookup_options, client_revision) -> (domains, names, count) """
        pass

    def LookupSids3(self, sids, names, level, count, lookup_options, client_revision): # real signature unknown; restored from __doc__
        """ S.LookupSids3(sids, names, level, count, lookup_options, client_revision) -> (domains, names, count) """
        pass

    def lsaRQueryForestTrustInformation(self, handle, trusted_domain_name, highest_record_type): # real signature unknown; restored from __doc__
        """ S.lsaRQueryForestTrustInformation(handle, trusted_domain_name, highest_record_type) -> forest_trust_info """
        pass

    def lsaRSetForestTrustInformation(self, handle, trusted_domain_name, highest_record_type, forest_trust_info, check_only): # real signature unknown; restored from __doc__
        """ S.lsaRSetForestTrustInformation(handle, trusted_domain_name, highest_record_type, forest_trust_info, check_only) -> collision_info """
        pass

    def OpenAccount(self, handle, sid, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenAccount(handle, sid, access_mask) -> acct_handle """
        pass

    def OpenPolicy(self, system_name, attr, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenPolicy(system_name, attr, access_mask) -> handle """
        pass

    def OpenPolicy2(self, system_name, attr, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenPolicy2(system_name, attr, access_mask) -> handle """
        pass

    def OpenSecret(self, handle, name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenSecret(handle, name, access_mask) -> sec_handle """
        pass

    def OpenTrustedDomain(self, handle, sid, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenTrustedDomain(handle, sid, access_mask) -> trustdom_handle """
        pass

    def OpenTrustedDomainByName(self, handle, name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenTrustedDomainByName(handle, name, access_mask) -> trustdom_handle """
        pass

    def QueryDomainInformationPolicy(self, handle, level): # real signature unknown; restored from __doc__
        """ S.QueryDomainInformationPolicy(handle, level) -> info """
        pass

    def QueryInfoPolicy(self, handle, level): # real signature unknown; restored from __doc__
        """ S.QueryInfoPolicy(handle, level) -> info """
        pass

    def QueryInfoPolicy2(self, handle, level): # real signature unknown; restored from __doc__
        """ S.QueryInfoPolicy2(handle, level) -> info """
        pass

    def QuerySecret(self, sec_handle, new_val, new_mtime, old_val, old_mtime): # real signature unknown; restored from __doc__
        """ S.QuerySecret(sec_handle, new_val, new_mtime, old_val, old_mtime) -> (new_val, new_mtime, old_val, old_mtime) """
        pass

    def QuerySecurity(self, handle, sec_info): # real signature unknown; restored from __doc__
        """ S.QuerySecurity(handle, sec_info) -> sdbuf """
        pass

    def QueryTrustedDomainInfo(self, trustdom_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryTrustedDomainInfo(trustdom_handle, level) -> info """
        pass

    def QueryTrustedDomainInfoByName(self, handle, trusted_domain, level): # real signature unknown; restored from __doc__
        """ S.QueryTrustedDomainInfoByName(handle, trusted_domain, level) -> info """
        pass

    def QueryTrustedDomainInfoBySid(self, handle, dom_sid, level): # real signature unknown; restored from __doc__
        """ S.QueryTrustedDomainInfoBySid(handle, dom_sid, level) -> info """
        pass

    def RemoveAccountRights(self, handle, sid, remove_all, rights): # real signature unknown; restored from __doc__
        """ S.RemoveAccountRights(handle, sid, remove_all, rights) -> None """
        pass

    def RemovePrivilegesFromAccount(self, handle, remove_all, privs): # real signature unknown; restored from __doc__
        """ S.RemovePrivilegesFromAccount(handle, remove_all, privs) -> None """
        pass

    def RetrievePrivateData(self, handle, name, val): # real signature unknown; restored from __doc__
        """ S.RetrievePrivateData(handle, name, val) -> val """
        pass

    def SetDomainInformationPolicy(self, handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetDomainInformationPolicy(handle, level, info) -> None """
        pass

    def SetInfoPolicy(self, handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetInfoPolicy(handle, level, info) -> None """
        pass

    def SetInfoPolicy2(self, handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetInfoPolicy2(handle, level, info) -> None """
        pass

    def SetInformationTrustedDomain(self, trustdom_handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetInformationTrustedDomain(trustdom_handle, level, info) -> None """
        pass

    def SetSecObj(self, handle, sec_info, sdbuf): # real signature unknown; restored from __doc__
        """ S.SetSecObj(handle, sec_info, sdbuf) -> None """
        pass

    def SetSecret(self, sec_handle, new_val, old_val): # real signature unknown; restored from __doc__
        """ S.SetSecret(sec_handle, new_val, old_val) -> None """
        pass

    def SetSystemAccessAccount(self, handle, access_mask): # real signature unknown; restored from __doc__
        """ S.SetSystemAccessAccount(handle, access_mask) -> None """
        pass

    def SetTrustedDomainInfo(self, handle, dom_sid, level, info): # real signature unknown; restored from __doc__
        """ S.SetTrustedDomainInfo(handle, dom_sid, level, info) -> None """
        pass

    def SetTrustedDomainInfoByName(self, handle, trusted_domain, level, info): # real signature unknown; restored from __doc__
        """ S.SetTrustedDomainInfoByName(handle, trusted_domain, level, info) -> None """
        pass

    def StorePrivateData(self, handle, name, val): # real signature unknown; restored from __doc__
        """ S.StorePrivateData(handle, name, val) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


