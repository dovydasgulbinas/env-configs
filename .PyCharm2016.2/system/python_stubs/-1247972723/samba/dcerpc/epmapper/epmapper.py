# encoding: utf-8
# module samba.dcerpc.epmapper
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/epmapper.so
# by generator 1.143
""" epmapper DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class epmapper(__dcerpc.ClientConnection):
    """
    epmapper(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    EndPoint Mapper
    """
    def epm_Delete(self, entries): # real signature unknown; restored from __doc__
        """ S.epm_Delete(entries) -> result """
        pass

    def epm_InqObject(self, epm_object): # real signature unknown; restored from __doc__
        """ S.epm_InqObject(epm_object) -> result """
        pass

    def epm_Insert(self, entries, replace): # real signature unknown; restored from __doc__
        """ S.epm_Insert(entries, replace) -> result """
        pass

    def epm_Lookup(self, inquiry_type, p_object, interface_id, vers_option, entry_handle, max_ents): # real signature unknown; restored from __doc__
        """ S.epm_Lookup(inquiry_type, object, interface_id, vers_option, entry_handle, max_ents) -> (entry_handle, entries, result) """
        pass

    def epm_LookupHandleFree(self, entry_handle): # real signature unknown; restored from __doc__
        """ S.epm_LookupHandleFree(entry_handle) -> (entry_handle, result) """
        pass

    def epm_Map(self, p_object, map_tower, entry_handle, max_towers): # real signature unknown; restored from __doc__
        """ S.epm_Map(object, map_tower, entry_handle, max_towers) -> (entry_handle, towers, result) """
        pass

    def epm_MgmtDelete(self, object_speced, p_object, tower): # real signature unknown; restored from __doc__
        """ S.epm_MgmtDelete(object_speced, object, tower) -> result """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


