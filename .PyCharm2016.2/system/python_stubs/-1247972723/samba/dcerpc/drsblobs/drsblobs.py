# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsblobs.so
# by generator 1.143
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class drsblobs(__dcerpc.ClientConnection):
    """
    drsblobs(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Active Directory Replication LDAP Blobs
    """
    def decode_ldapControlDirSync(self, cookie): # real signature unknown; restored from __doc__
        """ S.decode_ldapControlDirSync(cookie) -> None """
        pass

    def decode_Packages(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_Packages(blob) -> None """
        pass

    def decode_partialAttributeSet(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_partialAttributeSet(blob) -> None """
        pass

    def decode_prefixMap(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_prefixMap(blob) -> None """
        pass

    def decode_PrimaryCLEARTEXT(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_PrimaryCLEARTEXT(blob) -> None """
        pass

    def decode_PrimaryKerberos(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_PrimaryKerberos(blob) -> None """
        pass

    def decode_PrimaryWDigest(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_PrimaryWDigest(blob) -> None """
        pass

    def decode_replPropertyMetaData(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_replPropertyMetaData(blob) -> None """
        pass

    def decode_replUpToDateVector(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_replUpToDateVector(blob) -> None """
        pass

    def decode_repsFromTo(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_repsFromTo(blob) -> None """
        pass

    def decode_supplementalCredentials(self, blob): # real signature unknown; restored from __doc__
        """ S.decode_supplementalCredentials(blob) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


