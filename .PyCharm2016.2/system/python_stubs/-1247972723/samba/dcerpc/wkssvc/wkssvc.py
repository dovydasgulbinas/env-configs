# encoding: utf-8
# module samba.dcerpc.wkssvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/wkssvc.so
# by generator 1.143
""" wkssvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class wkssvc(__dcerpc.ClientConnection):
    """
    wkssvc(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Workstation Service
    """
    def NetrAddAlternateComputerName(self, server_name, NewAlternateMachineName, Account, EncryptedPassword, Reserved): # real signature unknown; restored from __doc__
        """ S.NetrAddAlternateComputerName(server_name, NewAlternateMachineName, Account, EncryptedPassword, Reserved) -> None """
        pass

    def NetrEnumerateComputerNames(self, server_name, name_type, Reserved): # real signature unknown; restored from __doc__
        """ S.NetrEnumerateComputerNames(server_name, name_type, Reserved) -> ctr """
        pass

    def NetrGetJoinableOus(self, server_name, domain_name, Account, unknown, num_ous): # real signature unknown; restored from __doc__
        """ S.NetrGetJoinableOus(server_name, domain_name, Account, unknown, num_ous) -> (num_ous, ous) """
        pass

    def NetrGetJoinableOus2(self, server_name, domain_name, Account, EncryptedPassword, num_ous): # real signature unknown; restored from __doc__
        """ S.NetrGetJoinableOus2(server_name, domain_name, Account, EncryptedPassword, num_ous) -> (num_ous, ous) """
        pass

    def NetrGetJoinInformation(self, server_name, name_buffer): # real signature unknown; restored from __doc__
        """ S.NetrGetJoinInformation(server_name, name_buffer) -> (name_buffer, name_type) """
        pass

    def NetrJoinDomain(self, server_name, domain_name, account_ou, Account, password, join_flags): # real signature unknown; restored from __doc__
        """ S.NetrJoinDomain(server_name, domain_name, account_ou, Account, password, join_flags) -> None """
        pass

    def NetrJoinDomain2(self, server_name, domain_name, account_ou, admin_account, encrypted_password, join_flags): # real signature unknown; restored from __doc__
        """ S.NetrJoinDomain2(server_name, domain_name, account_ou, admin_account, encrypted_password, join_flags) -> None """
        pass

    def NetrLogonDomainNameAdd(self, domain_name): # real signature unknown; restored from __doc__
        """ S.NetrLogonDomainNameAdd(domain_name) -> None """
        pass

    def NetrLogonDomainNameDel(self, domain_name): # real signature unknown; restored from __doc__
        """ S.NetrLogonDomainNameDel(domain_name) -> None """
        pass

    def NetrMessageBufferSend(self, server_name, message_name, message_sender_name, message_buffer): # real signature unknown; restored from __doc__
        """ S.NetrMessageBufferSend(server_name, message_name, message_sender_name, message_buffer) -> None """
        pass

    def NetrRemoveAlternateComputerName(self, server_name, AlternateMachineNameToRemove, Account, EncryptedPassword, Reserved): # real signature unknown; restored from __doc__
        """ S.NetrRemoveAlternateComputerName(server_name, AlternateMachineNameToRemove, Account, EncryptedPassword, Reserved) -> None """
        pass

    def NetrRenameMachineInDomain(self, server_name, NewMachineName, Account, password, RenameOptions): # real signature unknown; restored from __doc__
        """ S.NetrRenameMachineInDomain(server_name, NewMachineName, Account, password, RenameOptions) -> None """
        pass

    def NetrRenameMachineInDomain2(self, server_name, NewMachineName, Account, EncryptedPassword, RenameOptions): # real signature unknown; restored from __doc__
        """ S.NetrRenameMachineInDomain2(server_name, NewMachineName, Account, EncryptedPassword, RenameOptions) -> None """
        pass

    def NetrSetPrimaryComputername(self, server_name, primary_name, Account, EncryptedPassword, Reserved): # real signature unknown; restored from __doc__
        """ S.NetrSetPrimaryComputername(server_name, primary_name, Account, EncryptedPassword, Reserved) -> None """
        pass

    def NetrUnjoinDomain(self, server_name, Account, password, unjoin_flags): # real signature unknown; restored from __doc__
        """ S.NetrUnjoinDomain(server_name, Account, password, unjoin_flags) -> None """
        pass

    def NetrUnjoinDomain2(self, server_name, account, encrypted_password, unjoin_flags): # real signature unknown; restored from __doc__
        """ S.NetrUnjoinDomain2(server_name, account, encrypted_password, unjoin_flags) -> None """
        pass

    def NetrUseAdd(self, server_name, level, ctr, parm_err): # real signature unknown; restored from __doc__
        """ S.NetrUseAdd(server_name, level, ctr, parm_err) -> parm_err """
        pass

    def NetrUseDel(self, server_name, use_name, force_cond): # real signature unknown; restored from __doc__
        """ S.NetrUseDel(server_name, use_name, force_cond) -> None """
        pass

    def NetrUseEnum(self, server_name, info, prefmaxlen, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetrUseEnum(server_name, info, prefmaxlen, resume_handle) -> (info, entries_read, resume_handle) """
        pass

    def NetrUseGetInfo(self, server_name, use_name, level): # real signature unknown; restored from __doc__
        """ S.NetrUseGetInfo(server_name, use_name, level) -> ctr """
        pass

    def NetrValidateName(self, server_name, name, Account, Password, name_type): # real signature unknown; restored from __doc__
        """ S.NetrValidateName(server_name, name, Account, Password, name_type) -> None """
        pass

    def NetrValidateName2(self, server_name, name, Account, EncryptedPassword, name_type): # real signature unknown; restored from __doc__
        """ S.NetrValidateName2(server_name, name, Account, EncryptedPassword, name_type) -> None """
        pass

    def NetrWkstaTransportAdd(self, server_name, level, info0, parm_err): # real signature unknown; restored from __doc__
        """ S.NetrWkstaTransportAdd(server_name, level, info0, parm_err) -> parm_err """
        pass

    def NetrWkstaTransportDel(self, server_name, transport_name, unknown3): # real signature unknown; restored from __doc__
        """ S.NetrWkstaTransportDel(server_name, transport_name, unknown3) -> None """
        pass

    def NetrWkstaUserGetInfo(self, unknown, level): # real signature unknown; restored from __doc__
        """ S.NetrWkstaUserGetInfo(unknown, level) -> info """
        pass

    def NetrWkstaUserSetInfo(self, unknown, level, info, parm_err): # real signature unknown; restored from __doc__
        """ S.NetrWkstaUserSetInfo(unknown, level, info, parm_err) -> parm_err """
        pass

    def NetrWorkstationStatisticsGet(self, server_name, unknown2, unknown3, unknown4): # real signature unknown; restored from __doc__
        """ S.NetrWorkstationStatisticsGet(server_name, unknown2, unknown3, unknown4) -> info """
        pass

    def NetWkstaEnumUsers(self, server_name, info, prefmaxlen, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetWkstaEnumUsers(server_name, info, prefmaxlen, resume_handle) -> (info, entries_read, resume_handle) """
        pass

    def NetWkstaGetInfo(self, server_name, level): # real signature unknown; restored from __doc__
        """ S.NetWkstaGetInfo(server_name, level) -> info """
        pass

    def NetWkstaSetInfo(self, server_name, level, info, parm_error): # real signature unknown; restored from __doc__
        """ S.NetWkstaSetInfo(server_name, level, info, parm_error) -> parm_error """
        pass

    def NetWkstaTransportEnum(self, server_name, info, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetWkstaTransportEnum(server_name, info, max_buffer, resume_handle) -> (info, total_entries, resume_handle) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


