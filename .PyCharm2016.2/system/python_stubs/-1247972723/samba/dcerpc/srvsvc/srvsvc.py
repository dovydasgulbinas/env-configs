# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/srvsvc.so
# by generator 1.143
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class srvsvc(__dcerpc.ClientConnection):
    """
    srvsvc(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Server Service
    """
    def NetCharDevControl(self, server_unc, device_name, opcode): # real signature unknown; restored from __doc__
        """ S.NetCharDevControl(server_unc, device_name, opcode) -> None """
        pass

    def NetCharDevEnum(self, server_unc, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetCharDevEnum(server_unc, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetCharDevGetInfo(self, server_unc, device_name, level): # real signature unknown; restored from __doc__
        """ S.NetCharDevGetInfo(server_unc, device_name, level) -> info """
        pass

    def NetCharDevQEnum(self, server_unc, user, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetCharDevQEnum(server_unc, user, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetCharDevQGetInfo(self, server_unc, queue_name, user, level): # real signature unknown; restored from __doc__
        """ S.NetCharDevQGetInfo(server_unc, queue_name, user, level) -> info """
        pass

    def NetCharDevQPurge(self, server_unc, queue_name): # real signature unknown; restored from __doc__
        """ S.NetCharDevQPurge(server_unc, queue_name) -> None """
        pass

    def NetCharDevQPurgeSelf(self, server_unc, queue_name, computer_name): # real signature unknown; restored from __doc__
        """ S.NetCharDevQPurgeSelf(server_unc, queue_name, computer_name) -> None """
        pass

    def NetCharDevQSetInfo(self, server_unc, queue_name, level, info, parm_error): # real signature unknown; restored from __doc__
        """ S.NetCharDevQSetInfo(server_unc, queue_name, level, info, parm_error) -> parm_error """
        pass

    def NetConnEnum(self, server_unc, path, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetConnEnum(server_unc, path, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetDiskEnum(self, server_unc, level, info, maxlen, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetDiskEnum(server_unc, level, info, maxlen, resume_handle) -> (info, totalentries, resume_handle) """
        pass

    def NetFileClose(self, server_unc, fid): # real signature unknown; restored from __doc__
        """ S.NetFileClose(server_unc, fid) -> None """
        pass

    def NetFileEnum(self, server_unc, path, user, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetFileEnum(server_unc, path, user, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetFileGetInfo(self, server_unc, fid, level): # real signature unknown; restored from __doc__
        """ S.NetFileGetInfo(server_unc, fid, level) -> info """
        pass

    def NetGetFileSecurity(self, server_unc, share, file, securityinformation): # real signature unknown; restored from __doc__
        """ S.NetGetFileSecurity(server_unc, share, file, securityinformation) -> sd_buf """
        pass

    def NetNameValidate(self, server_unc, name, name_type, flags): # real signature unknown; restored from __doc__
        """ S.NetNameValidate(server_unc, name, name_type, flags) -> None """
        pass

    def NetPathCanonicalize(self, server_unc, path, maxbuf, prefix, pathtype, pathflags): # real signature unknown; restored from __doc__
        """ S.NetPathCanonicalize(server_unc, path, maxbuf, prefix, pathtype, pathflags) -> (can_path, pathtype) """
        pass

    def NetPathCompare(self, server_unc, path1, path2, pathtype, pathflags): # real signature unknown; restored from __doc__
        """ S.NetPathCompare(server_unc, path1, path2, pathtype, pathflags) -> None """
        pass

    def NetPathType(self, server_unc, path, pathflags): # real signature unknown; restored from __doc__
        """ S.NetPathType(server_unc, path, pathflags) -> pathtype """
        pass

    def NetPRNameCompare(self, server_unc, name1, name2, name_type, flags): # real signature unknown; restored from __doc__
        """ S.NetPRNameCompare(server_unc, name1, name2, name_type, flags) -> None """
        pass

    def NetRemoteTOD(self, server_unc): # real signature unknown; restored from __doc__
        """ S.NetRemoteTOD(server_unc) -> info """
        pass

    def NetServerSetServiceBitsEx(self, server_unc, emulated_server_unc, transport, servicebitsofinterest, servicebits, updateimmediately): # real signature unknown; restored from __doc__
        """ S.NetServerSetServiceBitsEx(server_unc, emulated_server_unc, transport, servicebitsofinterest, servicebits, updateimmediately) -> None """
        pass

    def NetServerStatisticsGet(self, server_unc, service, level, options): # real signature unknown; restored from __doc__
        """ S.NetServerStatisticsGet(server_unc, service, level, options) -> stats """
        pass

    def NetServerTransportAddEx(self, server_unc, level, info): # real signature unknown; restored from __doc__
        """ S.NetServerTransportAddEx(server_unc, level, info) -> None """
        pass

    def NetSessDel(self, server_unc, client, user): # real signature unknown; restored from __doc__
        """ S.NetSessDel(server_unc, client, user) -> None """
        pass

    def NetSessEnum(self, server_unc, client, user, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetSessEnum(server_unc, client, user, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetSetFileSecurity(self, server_unc, share, file, securityinformation, sd_buf): # real signature unknown; restored from __doc__
        """ S.NetSetFileSecurity(server_unc, share, file, securityinformation, sd_buf) -> None """
        pass

    def NetSetServiceBits(self, server_unc, transport, servicebits, updateimmediately): # real signature unknown; restored from __doc__
        """ S.NetSetServiceBits(server_unc, transport, servicebits, updateimmediately) -> None """
        pass

    def NetShareAdd(self, server_unc, level, info, parm_error): # real signature unknown; restored from __doc__
        """ S.NetShareAdd(server_unc, level, info, parm_error) -> parm_error """
        pass

    def NetShareCheck(self, server_unc, device_name): # real signature unknown; restored from __doc__
        """ S.NetShareCheck(server_unc, device_name) -> type """
        return type(*(), **{})

    def NetShareDel(self, server_unc, share_name, reserved): # real signature unknown; restored from __doc__
        """ S.NetShareDel(server_unc, share_name, reserved) -> None """
        pass

    def NetShareDelCommit(self, hnd): # real signature unknown; restored from __doc__
        """ S.NetShareDelCommit(hnd) -> hnd """
        pass

    def NetShareDelStart(self, server_unc, share, reserved): # real signature unknown; restored from __doc__
        """ S.NetShareDelStart(server_unc, share, reserved) -> hnd """
        pass

    def NetShareDelSticky(self, server_unc, share_name, reserved): # real signature unknown; restored from __doc__
        """ S.NetShareDelSticky(server_unc, share_name, reserved) -> None """
        pass

    def NetShareEnum(self, server_unc, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetShareEnum(server_unc, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetShareEnumAll(self, server_unc, info_ctr, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetShareEnumAll(server_unc, info_ctr, max_buffer, resume_handle) -> (info_ctr, totalentries, resume_handle) """
        pass

    def NetShareGetInfo(self, server_unc, share_name, level): # real signature unknown; restored from __doc__
        """ S.NetShareGetInfo(server_unc, share_name, level) -> info """
        pass

    def NetShareSetInfo(self, server_unc, share_name, level, info, parm_error): # real signature unknown; restored from __doc__
        """ S.NetShareSetInfo(server_unc, share_name, level, info, parm_error) -> parm_error """
        pass

    def NetSrvGetInfo(self, server_unc, level): # real signature unknown; restored from __doc__
        """ S.NetSrvGetInfo(server_unc, level) -> info """
        pass

    def NetSrvSetInfo(self, server_unc, level, info, parm_error): # real signature unknown; restored from __doc__
        """ S.NetSrvSetInfo(server_unc, level, info, parm_error) -> parm_error """
        pass

    def NetTransportAdd(self, server_unc, level, info): # real signature unknown; restored from __doc__
        """ S.NetTransportAdd(server_unc, level, info) -> None """
        pass

    def NetTransportDel(self, server_unc, level, info0): # real signature unknown; restored from __doc__
        """ S.NetTransportDel(server_unc, level, info0) -> None """
        pass

    def NetTransportEnum(self, server_unc, transports, max_buffer, resume_handle): # real signature unknown; restored from __doc__
        """ S.NetTransportEnum(server_unc, transports, max_buffer, resume_handle) -> (transports, totalentries, resume_handle) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


