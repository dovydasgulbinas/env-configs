# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.143
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class drsuapi(__dcerpc.ClientConnection):
    """
    drsuapi(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Active Directory Replication
    """
    def DsAddEntry(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsAddEntry(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def DsBind(self, bind_guid, bind_info): # real signature unknown; restored from __doc__
        """ S.DsBind(bind_guid, bind_info) -> (bind_info, bind_handle) """
        pass

    def DsCrackNames(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsCrackNames(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def DsExecuteKCC(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsExecuteKCC(bind_handle, level, req) -> None """
        pass

    def DsGetDomainControllerInfo(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsGetDomainControllerInfo(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def DsGetMemberships(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsGetMemberships(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def DsGetMemberships2(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsGetMemberships2(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def DsGetNCChanges(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsGetNCChanges(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def DsGetNT4ChangeLog(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsGetNT4ChangeLog(bind_handle, level, req) -> (level_out, info) """
        pass

    def DsRemoveDSServer(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsRemoveDSServer(bind_handle, level, req) -> (level_out, res) """
        pass

    def DsReplicaAdd(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsReplicaAdd(bind_handle, level, req) -> None """
        pass

    def DsReplicaDel(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsReplicaDel(bind_handle, level, req) -> None """
        pass

    def DsReplicaGetInfo(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsReplicaGetInfo(bind_handle, level, req) -> (info_type, info) """
        pass

    def DsReplicaMod(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsReplicaMod(bind_handle, level, req) -> None """
        pass

    def DsReplicaSync(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsReplicaSync(bind_handle, level, req) -> None """
        pass

    def DsReplicaUpdateRefs(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsReplicaUpdateRefs(bind_handle, level, req) -> None """
        pass

    def DsUnbind(self, bind_handle): # real signature unknown; restored from __doc__
        """ S.DsUnbind(bind_handle) -> bind_handle """
        pass

    def DsWriteAccountSpn(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.DsWriteAccountSpn(bind_handle, level, req) -> (level_out, res) """
        pass

    def QuerySitesByCost(self, bind_handle, level, req): # real signature unknown; restored from __doc__
        """ S.QuerySitesByCost(bind_handle, level, req) -> (level_out, ctr) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


