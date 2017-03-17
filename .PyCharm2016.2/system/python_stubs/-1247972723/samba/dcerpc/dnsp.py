# encoding: utf-8
# module samba.dcerpc.dnsp
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsp.so
# by generator 1.143
""" dnsp DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

DCPROMO_CONVERT_DOMAIN = 1
DCPROMO_CONVERT_FOREST = 2
DCPROMO_CONVERT_NONE = 0

DNS_RANK_CACHE_A_ADDITIONAL = 81
DNS_RANK_CACHE_A_ANSWER = 193
DNS_RANK_CACHE_A_AUTHORITY = 113

DNS_RANK_CACHE_BIT = 1

DNS_RANK_CACHE_NA_ADDITIONAL = 49
DNS_RANK_CACHE_NA_ANSWER = 97
DNS_RANK_CACHE_NA_AUTHORITY = 65

DNS_RANK_GLUE = 128
DNS_RANK_NONE = 0

DNS_RANK_NS_GLUE = 130

DNS_RANK_OUTSIDE_GLUE = 32

DNS_RANK_ROOT_HINT = 8

DNS_RANK_ZONE = 240

DNS_RPC_FLAG_AGING_ON = 131072

DNS_RPC_FLAG_AUTH_ZONE_ROOT = 536870912

DNS_RPC_FLAG_CACHE_DATA = 2147483648

DNS_RPC_FLAG_NODE_COMPLETE = 8388608
DNS_RPC_FLAG_NODE_STICKY = 16777216

DNS_RPC_FLAG_OPEN_ACL = 262144

DNS_RPC_FLAG_RECORD_CREATE_PTR = 33554432

DNS_RPC_FLAG_RECORD_DEFAULT_TTL = 134217728

DNS_RPC_FLAG_RECORD_TTL_CHANGE = 67108864

DNS_RPC_FLAG_SUPPRESS_NOTIFY = 65536

DNS_RPC_FLAG_ZONE_DELEGATION = 268435456
DNS_RPC_FLAG_ZONE_ROOT = 1073741824

DNS_TYPE_A = 1
DNS_TYPE_AAAA = 28
DNS_TYPE_AFSDB = 18
DNS_TYPE_ALL = 255
DNS_TYPE_ATMA = 34
DNS_TYPE_CNAME = 5
DNS_TYPE_DHCID = 49
DNS_TYPE_DNAME = 39
DNS_TYPE_DNSKEY = 48
DNS_TYPE_DS = 43
DNS_TYPE_HINFO = 13
DNS_TYPE_ISDN = 20
DNS_TYPE_KEY = 25
DNS_TYPE_LOC = 29
DNS_TYPE_MB = 7
DNS_TYPE_MD = 3
DNS_TYPE_MF = 4
DNS_TYPE_MG = 8
DNS_TYPE_MINFO = 14
DNS_TYPE_MR = 9
DNS_TYPE_MX = 15
DNS_TYPE_NAPTR = 35
DNS_TYPE_NS = 2
DNS_TYPE_NSEC = 47
DNS_TYPE_NULL = 10
DNS_TYPE_NXT = 30
DNS_TYPE_PTR = 12
DNS_TYPE_RP = 17
DNS_TYPE_RRSIG = 46
DNS_TYPE_RT = 21
DNS_TYPE_SIG = 24
DNS_TYPE_SOA = 6
DNS_TYPE_SRV = 33
DNS_TYPE_TOMBSTONE = 0
DNS_TYPE_TXT = 16
DNS_TYPE_WINS = 65281
DNS_TYPE_WINSR = 65282
DNS_TYPE_WKS = 11
DNS_TYPE_X25 = 19

DNS_ZONE_TYPE_CACHE = 0
DNS_ZONE_TYPE_FORWARDER = 4
DNS_ZONE_TYPE_PRIMARY = 1
DNS_ZONE_TYPE_SECONDARY = 2

DNS_ZONE_TYPE_SECONDARY_CACHE = 5

DNS_ZONE_TYPE_STUB = 3

DNS_ZONE_UPDATE_OFF = 0
DNS_ZONE_UPDATE_SECURE = 2
DNS_ZONE_UPDATE_UNSECURE = 1

DSPROPERTY_ZONE_AGING_ENABLED_TIME = 18

DSPROPERTY_ZONE_AGING_STATE = 64

DSPROPERTY_ZONE_ALLOW_UPDATE = 2

DSPROPERTY_ZONE_AUTO_NS_SERVERS = 130

DSPROPERTY_ZONE_DCPROMO_CONVERT = 131

DSPROPERTY_ZONE_DELETED_FROM_HOSTNAME = 128

DSPROPERTY_ZONE_EMPTY = 0

DSPROPERTY_ZONE_MASTER_SERVERS = 129

DSPROPERTY_ZONE_MASTER_SERVERS_DA = 145

DSPROPERTY_ZONE_NODE_DBFLAGS = 256

DSPROPERTY_ZONE_NOREFRESH_INTERVAL = 16

DSPROPERTY_ZONE_NS_SERVERS_DA = 146

DSPROPERTY_ZONE_REFRESH_INTERVAL = 32

DSPROPERTY_ZONE_SCAVENGING_SERVERS = 17

DSPROPERTY_ZONE_SCAVENGING_SERVERS_DA = 144

DSPROPERTY_ZONE_SECURE_TIME = 8

DSPROPERTY_ZONE_TYPE = 1

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    DNSP interfaces
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class dnsp(__dcerpc.ClientConnection):
    """
    dnsp(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    DNSP interfaces
    """
    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class DnsProperty(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    namelength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wDataLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DnssrvRpcRecord(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwSerial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwTtlSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wDataLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class dns_addr(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ipv4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ipv6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class dns_addr_array(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AddrArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AddrCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MatchFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MaxCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class hinfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    cpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    os = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ip4_array(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    addrCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class mx(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    nameTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wPriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class soa(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    expire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class srv(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    nameTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wPort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wPriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class string_list(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



