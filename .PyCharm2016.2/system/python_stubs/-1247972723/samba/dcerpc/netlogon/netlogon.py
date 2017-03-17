# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netlogon(__dcerpc.ClientConnection):
    """
    netlogon(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    """
    def netr_AccountDeltas(self, logon_server, computername, credential, return_authenticator, uas, count, level, buffersize): # real signature unknown; restored from __doc__
        """ S.netr_AccountDeltas(logon_server, computername, credential, return_authenticator, uas, count, level, buffersize) -> (return_authenticator, buffer, count_returned, total_entries, recordid) """
        pass

    def netr_AccountSync(self, logon_server, computername, credential, return_authenticator, reference, level, buffersize, recordid): # real signature unknown; restored from __doc__
        """ S.netr_AccountSync(logon_server, computername, credential, return_authenticator, reference, level, buffersize, recordid) -> (return_authenticator, buffer, count_returned, total_entries, next_reference, recordid) """
        pass

    def netr_DatabaseDeltas(self, logon_server, computername, credential, return_authenticator, database_id, sequence_num, preferredmaximumlength): # real signature unknown; restored from __doc__
        """ S.netr_DatabaseDeltas(logon_server, computername, credential, return_authenticator, database_id, sequence_num, preferredmaximumlength) -> (return_authenticator, sequence_num, delta_enum_array) """
        pass

    def netr_DatabaseRedo(self, logon_server, computername, credential, return_authenticator, change_log_entry, change_log_entry_size): # real signature unknown; restored from __doc__
        """ S.netr_DatabaseRedo(logon_server, computername, credential, return_authenticator, change_log_entry, change_log_entry_size) -> (return_authenticator, delta_enum_array) """
        pass

    def netr_DatabaseSync(self, logon_server, computername, credential, return_authenticator, database_id, sync_context, preferredmaximumlength): # real signature unknown; restored from __doc__
        """ S.netr_DatabaseSync(logon_server, computername, credential, return_authenticator, database_id, sync_context, preferredmaximumlength) -> (return_authenticator, sync_context, delta_enum_array) """
        pass

    def netr_DatabaseSync2(self, logon_server, computername, credential, return_authenticator, database_id, restart_state, sync_context, preferredmaximumlength): # real signature unknown; restored from __doc__
        """ S.netr_DatabaseSync2(logon_server, computername, credential, return_authenticator, database_id, restart_state, sync_context, preferredmaximumlength) -> (return_authenticator, sync_context, delta_enum_array) """
        pass

    def netr_DsRAddressToSitenamesExW(self, server_name, addresses): # real signature unknown; restored from __doc__
        """ S.netr_DsRAddressToSitenamesExW(server_name, addresses) -> ctr """
        pass

    def netr_DsRAddressToSitenamesW(self, server_name, addresses): # real signature unknown; restored from __doc__
        """ S.netr_DsRAddressToSitenamesW(server_name, addresses) -> ctr """
        pass

    def netr_DsrDeregisterDNSHostRecords(self, server_name, domain, domain_guid, dsa_guid, dns_host): # real signature unknown; restored from __doc__
        """ S.netr_DsrDeregisterDNSHostRecords(server_name, domain, domain_guid, dsa_guid, dns_host) -> None """
        pass

    def netr_DsrEnumerateDomainTrusts(self, server_name, trust_flags): # real signature unknown; restored from __doc__
        """ S.netr_DsrEnumerateDomainTrusts(server_name, trust_flags) -> trusts """
        pass

    def netr_DsRGetDCName(self, server_unc, domain_name, domain_guid, site_guid, flags): # real signature unknown; restored from __doc__
        """ S.netr_DsRGetDCName(server_unc, domain_name, domain_guid, site_guid, flags) -> info """
        pass

    def netr_DsRGetDCNameEx(self, server_unc, domain_name, domain_guid, site_name, flags): # real signature unknown; restored from __doc__
        """ S.netr_DsRGetDCNameEx(server_unc, domain_name, domain_guid, site_name, flags) -> info """
        pass

    def netr_DsRGetDCNameEx2(self, server_unc, client_account, mask, domain_name, domain_guid, site_name, flags): # real signature unknown; restored from __doc__
        """ S.netr_DsRGetDCNameEx2(server_unc, client_account, mask, domain_name, domain_guid, site_name, flags) -> info """
        pass

    def netr_DsrGetDcSiteCoverageW(self, server_name): # real signature unknown; restored from __doc__
        """ S.netr_DsrGetDcSiteCoverageW(server_name) -> ctr """
        pass

    def netr_DsRGetForestTrustInformation(self, server_name, trusted_domain_name, flags): # real signature unknown; restored from __doc__
        """ S.netr_DsRGetForestTrustInformation(server_name, trusted_domain_name, flags) -> forest_trust_info """
        pass

    def netr_DsRGetSiteName(self, computer_name): # real signature unknown; restored from __doc__
        """ S.netr_DsRGetSiteName(computer_name) -> site """
        pass

    def netr_DsrUpdateReadOnlyServerDnsRecords(self, server_name, computer_name, credential, site_name, dns_ttl, dns_names): # real signature unknown; restored from __doc__
        """ S.netr_DsrUpdateReadOnlyServerDnsRecords(server_name, computer_name, credential, site_name, dns_ttl, dns_names) -> (return_authenticator, dns_names) """
        pass

    def netr_GetAnyDCName(self, logon_server, domainname): # real signature unknown; restored from __doc__
        """ S.netr_GetAnyDCName(logon_server, domainname) -> dcname """
        pass

    def netr_GetDcName(self, logon_server, domainname): # real signature unknown; restored from __doc__
        """ S.netr_GetDcName(logon_server, domainname) -> dcname """
        pass

    def netr_GetForestTrustInformation(self, server_name, computer_name, credential, flags): # real signature unknown; restored from __doc__
        """ S.netr_GetForestTrustInformation(server_name, computer_name, credential, flags) -> (return_authenticator, forest_trust_info) """
        pass

    def netr_LogonControl(self, logon_server, function_code, level): # real signature unknown; restored from __doc__
        """ S.netr_LogonControl(logon_server, function_code, level) -> query """
        pass

    def netr_LogonControl2(self, logon_server, function_code, level, data): # real signature unknown; restored from __doc__
        """ S.netr_LogonControl2(logon_server, function_code, level, data) -> query """
        pass

    def netr_LogonControl2Ex(self, logon_server, function_code, level, data): # real signature unknown; restored from __doc__
        """ S.netr_LogonControl2Ex(logon_server, function_code, level, data) -> query """
        pass

    def netr_LogonGetCapabilities(self, server_name, computer_name, credential, return_authenticator, query_level): # real signature unknown; restored from __doc__
        """ S.netr_LogonGetCapabilities(server_name, computer_name, credential, return_authenticator, query_level) -> (return_authenticator, capabilities) """
        pass

    def netr_LogonGetDomainInfo(self, server_name, computer_name, credential, return_authenticator, level, query): # real signature unknown; restored from __doc__
        """ S.netr_LogonGetDomainInfo(server_name, computer_name, credential, return_authenticator, level, query) -> (return_authenticator, info) """
        pass

    def netr_LogonGetTrustRid(self, server_name, domain_name): # real signature unknown; restored from __doc__
        """ S.netr_LogonGetTrustRid(server_name, domain_name) -> rid """
        pass

    def netr_LogonSamLogoff(self, server_name, computer_name, credential, return_authenticator, logon_level, logon): # real signature unknown; restored from __doc__
        """ S.netr_LogonSamLogoff(server_name, computer_name, credential, return_authenticator, logon_level, logon) -> return_authenticator """
        pass

    def netr_LogonSamLogon(self, server_name, computer_name, credential, return_authenticator, logon_level, logon, validation_level): # real signature unknown; restored from __doc__
        """ S.netr_LogonSamLogon(server_name, computer_name, credential, return_authenticator, logon_level, logon, validation_level) -> (return_authenticator, validation, authoritative) """
        pass

    def netr_LogonSamLogonEx(self, server_name, computer_name, logon_level, logon, validation_level, flags): # real signature unknown; restored from __doc__
        """ S.netr_LogonSamLogonEx(server_name, computer_name, logon_level, logon, validation_level, flags) -> (validation, authoritative, flags) """
        pass

    def netr_LogonSamLogonWithFlags(self, server_name, computer_name, credential, return_authenticator, logon_level, logon, validation_level, flags): # real signature unknown; restored from __doc__
        """ S.netr_LogonSamLogonWithFlags(server_name, computer_name, credential, return_authenticator, logon_level, logon, validation_level, flags) -> (return_authenticator, validation, authoritative, flags) """
        pass

    def netr_LogonUasLogoff(self, server_name, account_name, workstation): # real signature unknown; restored from __doc__
        """ S.netr_LogonUasLogoff(server_name, account_name, workstation) -> info """
        pass

    def netr_LogonUasLogon(self, server_name, account_name, workstation): # real signature unknown; restored from __doc__
        """ S.netr_LogonUasLogon(server_name, account_name, workstation) -> info """
        pass

    def netr_NetrEnumerateTrustedDomains(self, server_name): # real signature unknown; restored from __doc__
        """ S.netr_NetrEnumerateTrustedDomains(server_name) -> trusted_domains_blob """
        pass

    def netr_NetrEnumerateTrustedDomainsEx(self, server_name): # real signature unknown; restored from __doc__
        """ S.netr_NetrEnumerateTrustedDomainsEx(server_name) -> dom_trust_list """
        pass

    def netr_ServerAuthenticate(self, server_name, account_name, secure_channel_type, computer_name, credentials): # real signature unknown; restored from __doc__
        """ S.netr_ServerAuthenticate(server_name, account_name, secure_channel_type, computer_name, credentials) -> return_credentials """
        pass

    def netr_ServerAuthenticate2(self, server_name, account_name, secure_channel_type, computer_name, credentials, negotiate_flags): # real signature unknown; restored from __doc__
        """ S.netr_ServerAuthenticate2(server_name, account_name, secure_channel_type, computer_name, credentials, negotiate_flags) -> (return_credentials, negotiate_flags) """
        pass

    def netr_ServerAuthenticate3(self, server_name, account_name, secure_channel_type, computer_name, credentials, negotiate_flags): # real signature unknown; restored from __doc__
        """ S.netr_ServerAuthenticate3(server_name, account_name, secure_channel_type, computer_name, credentials, negotiate_flags) -> (return_credentials, negotiate_flags, rid) """
        pass

    def netr_ServerGetTrustInfo(self, server_name, account_name, secure_channel_type, computer_name, credential): # real signature unknown; restored from __doc__
        """ S.netr_ServerGetTrustInfo(server_name, account_name, secure_channel_type, computer_name, credential) -> (return_authenticator, new_owf_password, old_owf_password, trust_info) """
        pass

    def netr_ServerPasswordGet(self, server_name, account_name, secure_channel_type, computer_name, credential): # real signature unknown; restored from __doc__
        """ S.netr_ServerPasswordGet(server_name, account_name, secure_channel_type, computer_name, credential) -> (return_authenticator, password) """
        pass

    def netr_ServerPasswordSet(self, server_name, account_name, secure_channel_type, computer_name, credential, new_password): # real signature unknown; restored from __doc__
        """ S.netr_ServerPasswordSet(server_name, account_name, secure_channel_type, computer_name, credential, new_password) -> return_authenticator """
        pass

    def netr_ServerPasswordSet2(self, server_name, account_name, secure_channel_type, computer_name, credential, new_password): # real signature unknown; restored from __doc__
        """ S.netr_ServerPasswordSet2(server_name, account_name, secure_channel_type, computer_name, credential, new_password) -> return_authenticator """
        pass

    def netr_ServerReqChallenge(self, server_name, computer_name, credentials): # real signature unknown; restored from __doc__
        """ S.netr_ServerReqChallenge(server_name, computer_name, credentials) -> return_credentials """
        pass

    def netr_ServerTrustPasswordsGet(self, server_name, account_name, secure_channel_type, computer_name, credential): # real signature unknown; restored from __doc__
        """ S.netr_ServerTrustPasswordsGet(server_name, account_name, secure_channel_type, computer_name, credential) -> (return_authenticator, new_owf_password, old_owf_password) """
        pass

    def netr_Unused47(self): # real signature unknown; restored from __doc__
        """ S.netr_Unused47() -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


