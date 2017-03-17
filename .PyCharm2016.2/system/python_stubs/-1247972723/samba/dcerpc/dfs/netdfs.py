# encoding: utf-8
# module samba.dcerpc.dfs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dfs.so
# by generator 1.143
""" dfs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netdfs(__dcerpc.ClientConnection):
    """
    netdfs(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Settings for Microsoft Distributed File System
    """
    def Add(self, path, server, share, comment, flags): # real signature unknown; restored from __doc__
        """ S.Add(path, server, share, comment, flags) -> None """
        pass

    def AddFtRoot(self, servername, dns_servername, dfsname, rootshare, comment, dfs_config_dn, unknown1, flags, unknown2): # real signature unknown; restored from __doc__
        """ S.AddFtRoot(servername, dns_servername, dfsname, rootshare, comment, dfs_config_dn, unknown1, flags, unknown2) -> unknown2 """
        pass

    def AddStdRoot(self, servername, rootshare, comment, flags): # real signature unknown; restored from __doc__
        """ S.AddStdRoot(servername, rootshare, comment, flags) -> None """
        pass

    def AddStdRootForced(self, servername, rootshare, comment, store): # real signature unknown; restored from __doc__
        """ S.AddStdRootForced(servername, rootshare, comment, store) -> None """
        pass

    def Enum(self, level, bufsize, info, total): # real signature unknown; restored from __doc__
        """ S.Enum(level, bufsize, info, total) -> (info, total) """
        pass

    def EnumEx(self, dfs_name, level, bufsize, info, total): # real signature unknown; restored from __doc__
        """ S.EnumEx(dfs_name, level, bufsize, info, total) -> (info, total) """
        pass

    def FlushFtTable(self, servername, rootshare): # real signature unknown; restored from __doc__
        """ S.FlushFtTable(servername, rootshare) -> None """
        pass

    def GetDcAddress(self, servername, server_fullname, is_root, ttl): # real signature unknown; restored from __doc__
        """ S.GetDcAddress(servername, server_fullname, is_root, ttl) -> (server_fullname, is_root, ttl) """
        pass

    def GetInfo(self, dfs_entry_path, servername, sharename, level): # real signature unknown; restored from __doc__
        """ S.GetInfo(dfs_entry_path, servername, sharename, level) -> info """
        pass

    def GetManagerVersion(self): # real signature unknown; restored from __doc__
        """ S.GetManagerVersion() -> version """
        pass

    def ManagerInitialize(self, servername, flags): # real signature unknown; restored from __doc__
        """ S.ManagerInitialize(servername, flags) -> None """
        pass

    def Remove(self, dfs_entry_path, servername, sharename): # real signature unknown; restored from __doc__
        """ S.Remove(dfs_entry_path, servername, sharename) -> None """
        pass

    def RemoveFtRoot(self, servername, dns_servername, dfsname, rootshare, flags, unknown): # real signature unknown; restored from __doc__
        """ S.RemoveFtRoot(servername, dns_servername, dfsname, rootshare, flags, unknown) -> unknown """
        pass

    def RemoveStdRoot(self, servername, rootshare, flags): # real signature unknown; restored from __doc__
        """ S.RemoveStdRoot(servername, rootshare, flags) -> None """
        pass

    def SetDcAddress(self, servername, server_fullname, flags, ttl): # real signature unknown; restored from __doc__
        """ S.SetDcAddress(servername, server_fullname, flags, ttl) -> None """
        pass

    def SetInfo(self, dfs_entry_path, servername, sharename, level, info): # real signature unknown; restored from __doc__
        """ S.SetInfo(dfs_entry_path, servername, sharename, level, info) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


