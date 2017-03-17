# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsserver.so
# by generator 1.143
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DNS_RPC_SERVER_INFO_W2K(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    aipForwarders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aipListenAddrs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aipServerAddrs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cAddressAnswerLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwDebugLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwDefaultNoRefreshInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwDefaultRefreshInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwDsPollingInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwForwardTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwLogLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwMaxCacheTtl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwNameCheckFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwRecursionRetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwRecursionTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserveArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwRpcProtocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwScavengingInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAdminConfigured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAllowUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAutoCacheUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAutoReverseZones = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fBindSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fBootMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fDefaultAgingState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fDsAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fForwardDelegations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fLocalNetPriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fLooseWildcarding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fNoRecursion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fRecurseAfterForwarding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fReserveArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fRoundRobin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fSecureResponses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fStrictFileParsing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fWriteAuthorityNs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pExtension1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pExtension2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pExtension3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pExtension4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pExtension5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszDsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszServerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



