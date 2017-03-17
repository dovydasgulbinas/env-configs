# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsserver.so
# by generator 1.143
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DNS_RPC_ZONE_INFO_DOTNET(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    aipLocalMasters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aipMasters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aipNotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aipScavengeServers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aipSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwAvailForScavengeTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwDpFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwForwarderTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwLastSuccessfulSoaCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwLastSuccessfulXfr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwNoRefreshInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwRefreshInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwRpcStructureVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwZoneType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAllowUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fAutoCreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fForwarderSlave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fNotifyLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fPaused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fReverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fSecureSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fShutdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fUseDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fUseNbstat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fUseWins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pReserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pReserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pReserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pReserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszDataFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszDpFqdn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszZoneName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwszZoneDn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



