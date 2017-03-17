# encoding: utf-8
# module samba.dcerpc.mgmt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/mgmt.so
# by generator 1.143
""" mgmt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

MGMT_STATS_ARRAY_MAX_SIZE = 4

MGMT_STATS_CALLS_IN = 0
MGMT_STATS_CALLS_OUT = 1

MGMT_STATS_PKTS_IN = 2
MGMT_STATS_PKTS_OUT = 3

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    DCE/RPC Remote Management
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class mgmt(__dcerpc.ClientConnection):
    """
    mgmt(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    DCE/RPC Remote Management
    """
    def inq_if_ids(self): # real signature unknown; restored from __doc__
        """ S.inq_if_ids() -> if_id_vector """
        pass

    def inq_princ_name(self, authn_proto, princ_name_size): # real signature unknown; restored from __doc__
        """ S.inq_princ_name(authn_proto, princ_name_size) -> princ_name """
        pass

    def inq_stats(self, max_count, unknown): # real signature unknown; restored from __doc__
        """ S.inq_stats(max_count, unknown) -> statistics """
        return statistics

    def is_server_listening(self): # real signature unknown; restored from __doc__
        """ S.is_server_listening() -> (status, result) """
        pass

    def stop_server_listening(self): # real signature unknown; restored from __doc__
        """ S.stop_server_listening() -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ndr_syntax_id_p(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class rpc_if_id_vector_t(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    if_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class statistics(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



