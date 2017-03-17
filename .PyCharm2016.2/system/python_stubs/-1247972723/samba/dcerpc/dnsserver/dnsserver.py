# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsserver.so
# by generator 1.143
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class dnsserver(__dcerpc.ClientConnection):
    """
    dnsserver(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    DNS Management Server
    """
    def DnssrvComplexOperation(self, pwszServerName, pszZone, pszOperation, dwTypeIn, pDataIn): # real signature unknown; restored from __doc__
        """ S.DnssrvComplexOperation(pwszServerName, pszZone, pszOperation, dwTypeIn, pDataIn) -> (pdwTypeOut, ppDataOut) """
        pass

    def DnssrvComplexOperation2(self, dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszOperation, dwTypeIn, pDataIn): # real signature unknown; restored from __doc__
        """ S.DnssrvComplexOperation2(dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszOperation, dwTypeIn, pDataIn) -> (pdwTypeOut, ppDataOut) """
        pass

    def DnssrvEnumRecords(self, pwszServerName, pszZone, pszNodeName, pszStartChild, wRecordType, fSelectFlag, pszFilterStart, pszFilterStop): # real signature unknown; restored from __doc__
        """ S.DnssrvEnumRecords(pwszServerName, pszZone, pszNodeName, pszStartChild, wRecordType, fSelectFlag, pszFilterStart, pszFilterStop) -> (pdwBufferLength, pBuffer) """
        pass

    def DnssrvEnumRecords2(self, dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszNodeName, pszStartChild, wRecordType, fSelectFlag, pszFilterStart, pszFilterStop): # real signature unknown; restored from __doc__
        """ S.DnssrvEnumRecords2(dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszNodeName, pszStartChild, wRecordType, fSelectFlag, pszFilterStart, pszFilterStop) -> (pdwBufferLength, pBuffer) """
        pass

    def DnssrvOperation(self, pwszServerName, pszZone, dwContext, pszOperation, dwTypeId, pData): # real signature unknown; restored from __doc__
        """ S.DnssrvOperation(pwszServerName, pszZone, dwContext, pszOperation, dwTypeId, pData) -> None """
        pass

    def DnssrvOperation2(self, dwClientVersion, dwSettingFlags, pwszServerName, pszZone, dwContext, pszOperation, dwTypeId, pData): # real signature unknown; restored from __doc__
        """ S.DnssrvOperation2(dwClientVersion, dwSettingFlags, pwszServerName, pszZone, dwContext, pszOperation, dwTypeId, pData) -> None """
        pass

    def DnssrvQuery(self, pwszServerName, pszZone, pszOperation): # real signature unknown; restored from __doc__
        """ S.DnssrvQuery(pwszServerName, pszZone, pszOperation) -> (pdwTypeId, ppData) """
        pass

    def DnssrvQuery2(self, dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszOperation): # real signature unknown; restored from __doc__
        """ S.DnssrvQuery2(dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszOperation) -> (pdwTypeId, ppData) """
        pass

    def DnssrvUpdateRecord(self, pwszServerName, pszZone, pszNodeName, pAddRecord, pDeleteRecord): # real signature unknown; restored from __doc__
        """ S.DnssrvUpdateRecord(pwszServerName, pszZone, pszNodeName, pAddRecord, pDeleteRecord) -> None """
        pass

    def DnssrvUpdateRecord2(self, dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszNodeName, pAddRecord, pDeleteRecord): # real signature unknown; restored from __doc__
        """ S.DnssrvUpdateRecord2(dwClientVersion, dwSettingFlags, pwszServerName, pszZone, pszNodeName, pAddRecord, pDeleteRecord) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


