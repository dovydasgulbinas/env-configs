# encoding: utf-8
# module samba.dcerpc.dns
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dns.so
# by generator 1.143
""" dns DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

DNS_FLAG_AUTHORITATIVE = 1024
DNS_FLAG_BROADCAST = 16

DNS_FLAG_RECURSION_AVAIL = 128
DNS_FLAG_RECURSION_DESIRED = 256

DNS_FLAG_REPLY = 32768
DNS_FLAG_TRUNCATION = 512

DNS_OPCODE = 30720

DNS_OPCODE_IQUERY = 2048

DNS_OPCODE_MULTI_HOME_REG = 30720

DNS_OPCODE_QUERY = 0
DNS_OPCODE_REFRESH = 16384
DNS_OPCODE_REFRESH2 = 18432
DNS_OPCODE_RELEASE = 12288
DNS_OPCODE_STATUS = 4096
DNS_OPCODE_UPDATE = 10240
DNS_OPCODE_WACK = 14336

DNS_QCLASS_ANY = 255
DNS_QCLASS_IN = 1
DNS_QCLASS_NONE = 254

DNS_QTYPE_A = 1
DNS_QTYPE_AAAA = 28
DNS_QTYPE_AFSDB = 18
DNS_QTYPE_ALL = 255
DNS_QTYPE_ATMA = 34
DNS_QTYPE_AXFR = 252
DNS_QTYPE_CNAME = 5
DNS_QTYPE_DHCID = 49
DNS_QTYPE_DNAME = 39
DNS_QTYPE_DNSKEY = 48
DNS_QTYPE_DS = 43
DNS_QTYPE_HINFO = 13
DNS_QTYPE_ISDN = 20
DNS_QTYPE_KEY = 25
DNS_QTYPE_LOC = 29
DNS_QTYPE_MAILA = 254
DNS_QTYPE_MAILB = 253
DNS_QTYPE_MB = 7
DNS_QTYPE_MD = 3
DNS_QTYPE_MF = 4
DNS_QTYPE_MG = 8
DNS_QTYPE_MINFO = 14
DNS_QTYPE_MR = 9
DNS_QTYPE_MX = 15
DNS_QTYPE_NAPTR = 35
DNS_QTYPE_NETBIOS = 32
DNS_QTYPE_NS = 2
DNS_QTYPE_NSEC = 47
DNS_QTYPE_NULL = 10
DNS_QTYPE_NXT = 30
DNS_QTYPE_OPT = 41
DNS_QTYPE_PTR = 12
DNS_QTYPE_RP = 17
DNS_QTYPE_RRSIG = 46
DNS_QTYPE_RT = 21
DNS_QTYPE_SIG = 24
DNS_QTYPE_SOA = 6
DNS_QTYPE_SRV = 33
DNS_QTYPE_TKEY = 249
DNS_QTYPE_TSIG = 250
DNS_QTYPE_TXT = 16
DNS_QTYPE_WKS = 11
DNS_QTYPE_X25 = 19
DNS_QTYPE_ZERO = 0

DNS_RCODE = 15

DNS_RCODE_BADALG = 21
DNS_RCODE_BADKEY = 17
DNS_RCODE_BADMODE = 19
DNS_RCODE_BADNAME = 20
DNS_RCODE_BADSIG = 16
DNS_RCODE_BADTIME = 18
DNS_RCODE_FORMERR = 1
DNS_RCODE_NOTAUTH = 9
DNS_RCODE_NOTIMP = 4
DNS_RCODE_NOTZONE = 10
DNS_RCODE_NXDOMAIN = 3
DNS_RCODE_NXRRSET = 8
DNS_RCODE_OK = 0
DNS_RCODE_REFUSED = 5
DNS_RCODE_SERVFAIL = 2
DNS_RCODE_YXDOMAIN = 6
DNS_RCODE_YXRRSET = 7

DNS_SERVICE_PORT = 53

DNS_TKEY_MODE_CLIENT = 4
DNS_TKEY_MODE_DELETE = 5
DNS_TKEY_MODE_DH = 2
DNS_TKEY_MODE_GSSAPI = 3
DNS_TKEY_MODE_LAST = 65535
DNS_TKEY_MODE_NULL = 0
DNS_TKEY_MODE_SERVER = 1

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    DNS records
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class dns(__dcerpc.ClientConnection):
    """
    dns(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    DNS records
    """
    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class fake_tsig_rec(__talloc.Object):
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

    algorithm_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fudge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    original_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rr_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ttl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class mx_record(__talloc.Object):
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

    exchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class name_packet(__talloc.Object):
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

    additional = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ancount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    answers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    arcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nscount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nsrecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    questions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class name_question(__talloc.Object):
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    question_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    question_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class opt_record(__talloc.Object):
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

    option_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    option_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    option_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class rdata_data(__talloc.Object):
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

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class res_rec(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rr_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rr_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ttl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unexpected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class rp_record(__talloc.Object):
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

    mbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    txt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class soa_record(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
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



class srv_record(__talloc.Object):
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

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class tkey_record(__talloc.Object):
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

    algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expiration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class tsig_record(__talloc.Object):
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

    algorithm_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fudge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mac_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    original_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class txt_record(__talloc.Object):
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

    txt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



