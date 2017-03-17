# encoding: utf-8
# module samba.dcerpc.unixinfo
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/unixinfo.so
# by generator 1.143
""" unixinfo DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    Unixinfo specific stuff
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class GetPWUidInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    homedir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class unixinfo(__dcerpc.ClientConnection):
    """
    unixinfo(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Unixinfo specific stuff
    """
    def GetPWUid(self, uids): # real signature unknown; restored from __doc__
        """ S.GetPWUid(uids) -> infos """
        pass

    def GidToSid(self, gid): # real signature unknown; restored from __doc__
        """ S.GidToSid(gid) -> sid """
        pass

    def SidToGid(self, sid): # real signature unknown; restored from __doc__
        """ S.SidToGid(sid) -> gid """
        pass

    def SidToUid(self, sid): # real signature unknown; restored from __doc__
        """ S.SidToUid(sid) -> uid """
        pass

    def UidToSid(self, uid): # real signature unknown; restored from __doc__
        """ S.UidToSid(uid) -> sid """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


