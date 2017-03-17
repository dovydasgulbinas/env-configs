# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/samr.so
# by generator 1.143
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class samr(__dcerpc.ClientConnection):
    """
    samr(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    """
    def AddAliasMember(self, alias_handle, sid): # real signature unknown; restored from __doc__
        """ S.AddAliasMember(alias_handle, sid) -> None """
        pass

    def AddGroupMember(self, group_handle, rid, flags): # real signature unknown; restored from __doc__
        """ S.AddGroupMember(group_handle, rid, flags) -> None """
        pass

    def AddMultipleMembersToAlias(self, alias_handle, sids): # real signature unknown; restored from __doc__
        """ S.AddMultipleMembersToAlias(alias_handle, sids) -> None """
        pass

    def ChangePasswordUser(self, user_handle, lm_present, old_lm_crypted, new_lm_crypted, nt_present, old_nt_crypted, new_nt_crypted, cross1_present, nt_cross, cross2_present, lm_cross): # real signature unknown; restored from __doc__
        """ S.ChangePasswordUser(user_handle, lm_present, old_lm_crypted, new_lm_crypted, nt_present, old_nt_crypted, new_nt_crypted, cross1_present, nt_cross, cross2_present, lm_cross) -> None """
        pass

    def ChangePasswordUser2(self, server, account, nt_password, nt_verifier, lm_change, lm_password, lm_verifier): # real signature unknown; restored from __doc__
        """ S.ChangePasswordUser2(server, account, nt_password, nt_verifier, lm_change, lm_password, lm_verifier) -> None """
        pass

    def ChangePasswordUser3(self, server, account, nt_password, nt_verifier, lm_change, lm_password, lm_verifier, password3): # real signature unknown; restored from __doc__
        """ S.ChangePasswordUser3(server, account, nt_password, nt_verifier, lm_change, lm_password, lm_verifier, password3) -> (dominfo, reject) """
        pass

    def Close(self, handle): # real signature unknown; restored from __doc__
        """ S.Close(handle) -> handle """
        pass

    def Connect(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.Connect(system_name, access_mask) -> connect_handle """
        pass

    def Connect2(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.Connect2(system_name, access_mask) -> connect_handle """
        pass

    def Connect3(self, system_name, unknown, access_mask): # real signature unknown; restored from __doc__
        """ S.Connect3(system_name, unknown, access_mask) -> connect_handle """
        pass

    def Connect4(self, system_name, client_version, access_mask): # real signature unknown; restored from __doc__
        """ S.Connect4(system_name, client_version, access_mask) -> connect_handle """
        pass

    def Connect5(self, system_name, access_mask, level_in, info_in): # real signature unknown; restored from __doc__
        """ S.Connect5(system_name, access_mask, level_in, info_in) -> (level_out, info_out, connect_handle) """
        pass

    def CreateDomainGroup(self, domain_handle, name, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateDomainGroup(domain_handle, name, access_mask) -> (group_handle, rid) """
        pass

    def CreateDomAlias(self, domain_handle, alias_name, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateDomAlias(domain_handle, alias_name, access_mask) -> (alias_handle, rid) """
        pass

    def CreateUser(self, domain_handle, account_name, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateUser(domain_handle, account_name, access_mask) -> (user_handle, rid) """
        pass

    def CreateUser2(self, domain_handle, account_name, acct_flags, access_mask): # real signature unknown; restored from __doc__
        """ S.CreateUser2(domain_handle, account_name, acct_flags, access_mask) -> (user_handle, access_granted, rid) """
        pass

    def DeleteAliasMember(self, alias_handle, sid): # real signature unknown; restored from __doc__
        """ S.DeleteAliasMember(alias_handle, sid) -> None """
        pass

    def DeleteDomainGroup(self, group_handle): # real signature unknown; restored from __doc__
        """ S.DeleteDomainGroup(group_handle) -> group_handle """
        pass

    def DeleteDomAlias(self, alias_handle): # real signature unknown; restored from __doc__
        """ S.DeleteDomAlias(alias_handle) -> alias_handle """
        pass

    def DeleteGroupMember(self, group_handle, rid): # real signature unknown; restored from __doc__
        """ S.DeleteGroupMember(group_handle, rid) -> None """
        pass

    def DeleteUser(self, user_handle): # real signature unknown; restored from __doc__
        """ S.DeleteUser(user_handle) -> user_handle """
        pass

    def EnumDomainAliases(self, domain_handle, resume_handle, max_size): # real signature unknown; restored from __doc__
        """ S.EnumDomainAliases(domain_handle, resume_handle, max_size) -> (resume_handle, sam, num_entries) """
        pass

    def EnumDomainGroups(self, domain_handle, resume_handle, max_size): # real signature unknown; restored from __doc__
        """ S.EnumDomainGroups(domain_handle, resume_handle, max_size) -> (resume_handle, sam, num_entries) """
        pass

    def EnumDomains(self, connect_handle, resume_handle, buf_size): # real signature unknown; restored from __doc__
        """ S.EnumDomains(connect_handle, resume_handle, buf_size) -> (resume_handle, sam, num_entries) """
        pass

    def EnumDomainUsers(self, domain_handle, resume_handle, acct_flags, max_size): # real signature unknown; restored from __doc__
        """ S.EnumDomainUsers(domain_handle, resume_handle, acct_flags, max_size) -> (resume_handle, sam, num_entries) """
        pass

    def GetAliasMembership(self, domain_handle, sids): # real signature unknown; restored from __doc__
        """ S.GetAliasMembership(domain_handle, sids) -> rids """
        pass

    def GetBootKeyInformation(self, domain_handle): # real signature unknown; restored from __doc__
        """ S.GetBootKeyInformation(domain_handle) -> unknown """
        pass

    def GetDisplayEnumerationIndex(self, domain_handle, level, name): # real signature unknown; restored from __doc__
        """ S.GetDisplayEnumerationIndex(domain_handle, level, name) -> idx """
        pass

    def GetDisplayEnumerationIndex2(self, domain_handle, level, name): # real signature unknown; restored from __doc__
        """ S.GetDisplayEnumerationIndex2(domain_handle, level, name) -> idx """
        pass

    def GetDomPwInfo(self, domain_name): # real signature unknown; restored from __doc__
        """ S.GetDomPwInfo(domain_name) -> info """
        pass

    def GetGroupsForUser(self, user_handle): # real signature unknown; restored from __doc__
        """ S.GetGroupsForUser(user_handle) -> rids """
        pass

    def GetMembersInAlias(self, alias_handle): # real signature unknown; restored from __doc__
        """ S.GetMembersInAlias(alias_handle) -> sids """
        pass

    def GetUserPwInfo(self, user_handle): # real signature unknown; restored from __doc__
        """ S.GetUserPwInfo(user_handle) -> info """
        pass

    def LookupDomain(self, connect_handle, domain_name): # real signature unknown; restored from __doc__
        """ S.LookupDomain(connect_handle, domain_name) -> sid """
        pass

    def LookupNames(self, domain_handle, names): # real signature unknown; restored from __doc__
        """ S.LookupNames(domain_handle, names) -> (rids, types) """
        pass

    def LookupRids(self, domain_handle, rids): # real signature unknown; restored from __doc__
        """ S.LookupRids(domain_handle, rids) -> (names, types) """
        pass

    def OemChangePasswordUser2(self, server, account, password, hash): # real signature unknown; restored from __doc__
        """ S.OemChangePasswordUser2(server, account, password, hash) -> None """
        pass

    def OpenAlias(self, domain_handle, access_mask, rid): # real signature unknown; restored from __doc__
        """ S.OpenAlias(domain_handle, access_mask, rid) -> alias_handle """
        pass

    def OpenDomain(self, connect_handle, access_mask, sid): # real signature unknown; restored from __doc__
        """ S.OpenDomain(connect_handle, access_mask, sid) -> domain_handle """
        pass

    def OpenGroup(self, domain_handle, access_mask, rid): # real signature unknown; restored from __doc__
        """ S.OpenGroup(domain_handle, access_mask, rid) -> group_handle """
        pass

    def OpenUser(self, domain_handle, access_mask, rid): # real signature unknown; restored from __doc__
        """ S.OpenUser(domain_handle, access_mask, rid) -> user_handle """
        pass

    def QueryAliasInfo(self, alias_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryAliasInfo(alias_handle, level) -> info """
        pass

    def QueryDisplayInfo(self, domain_handle, level, start_idx, max_entries, buf_size): # real signature unknown; restored from __doc__
        """ S.QueryDisplayInfo(domain_handle, level, start_idx, max_entries, buf_size) -> (total_size, returned_size, info) """
        pass

    def QueryDisplayInfo2(self, domain_handle, level, start_idx, max_entries, buf_size): # real signature unknown; restored from __doc__
        """ S.QueryDisplayInfo2(domain_handle, level, start_idx, max_entries, buf_size) -> (total_size, returned_size, info) """
        pass

    def QueryDisplayInfo3(self, domain_handle, level, start_idx, max_entries, buf_size): # real signature unknown; restored from __doc__
        """ S.QueryDisplayInfo3(domain_handle, level, start_idx, max_entries, buf_size) -> (total_size, returned_size, info) """
        pass

    def QueryDomainInfo(self, domain_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryDomainInfo(domain_handle, level) -> info """
        pass

    def QueryDomainInfo2(self, domain_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryDomainInfo2(domain_handle, level) -> info """
        pass

    def QueryGroupInfo(self, group_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryGroupInfo(group_handle, level) -> info """
        pass

    def QueryGroupMember(self, group_handle): # real signature unknown; restored from __doc__
        """ S.QueryGroupMember(group_handle) -> rids """
        pass

    def QuerySecurity(self, handle, sec_info): # real signature unknown; restored from __doc__
        """ S.QuerySecurity(handle, sec_info) -> sdbuf """
        pass

    def QueryUserInfo(self, user_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryUserInfo(user_handle, level) -> info """
        pass

    def QueryUserInfo2(self, user_handle, level): # real signature unknown; restored from __doc__
        """ S.QueryUserInfo2(user_handle, level) -> info """
        pass

    def RemoveMemberFromForeignDomain(self, domain_handle, sid): # real signature unknown; restored from __doc__
        """ S.RemoveMemberFromForeignDomain(domain_handle, sid) -> None """
        pass

    def RemoveMultipleMembersFromAlias(self, alias_handle, sids): # real signature unknown; restored from __doc__
        """ S.RemoveMultipleMembersFromAlias(alias_handle, sids) -> None """
        pass

    def RidToSid(self, domain_handle, rid): # real signature unknown; restored from __doc__
        """ S.RidToSid(domain_handle, rid) -> sid """
        pass

    def SetAliasInfo(self, alias_handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetAliasInfo(alias_handle, level, info) -> None """
        pass

    def SetBootKeyInformation(self, connect_handle, unknown1, unknown2, unknown3): # real signature unknown; restored from __doc__
        """ S.SetBootKeyInformation(connect_handle, unknown1, unknown2, unknown3) -> None """
        pass

    def SetDomainInfo(self, domain_handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetDomainInfo(domain_handle, level, info) -> None """
        pass

    def SetDsrmPassword(self, name, unknown, hash): # real signature unknown; restored from __doc__
        """ S.SetDsrmPassword(name, unknown, hash) -> None """
        pass

    def SetGroupInfo(self, group_handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetGroupInfo(group_handle, level, info) -> None """
        pass

    def SetMemberAttributesOfGroup(self, group_handle, unknown1, unknown2): # real signature unknown; restored from __doc__
        """ S.SetMemberAttributesOfGroup(group_handle, unknown1, unknown2) -> None """
        pass

    def SetSecurity(self, handle, sec_info, sdbuf): # real signature unknown; restored from __doc__
        """ S.SetSecurity(handle, sec_info, sdbuf) -> None """
        pass

    def SetUserInfo(self, user_handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetUserInfo(user_handle, level, info) -> None """
        pass

    def SetUserInfo2(self, user_handle, level, info): # real signature unknown; restored from __doc__
        """ S.SetUserInfo2(user_handle, level, info) -> None """
        pass

    def Shutdown(self, connect_handle): # real signature unknown; restored from __doc__
        """ S.Shutdown(connect_handle) -> None """
        pass

    def TestPrivateFunctionsDomain(self, domain_handle): # real signature unknown; restored from __doc__
        """ S.TestPrivateFunctionsDomain(domain_handle) -> None """
        pass

    def TestPrivateFunctionsUser(self, user_handle): # real signature unknown; restored from __doc__
        """ S.TestPrivateFunctionsUser(user_handle) -> None """
        pass

    def ValidatePassword(self, level, req): # real signature unknown; restored from __doc__
        """ S.ValidatePassword(level, req) -> rep """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


