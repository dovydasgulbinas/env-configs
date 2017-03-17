# encoding: utf-8
# module samba.dcerpc.echo
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/echo.so
# by generator 1.143
""" echo DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

ECHO_ENUM1 = 1

ECHO_ENUM1_32 = 1

ECHO_ENUM2 = 2

ECHO_ENUM2_32 = 2

# no functions
# classes

class abstract_syntax(__misc.ndr_syntax_id):
    """
    abstract_syntax()
    Simple echo pipe
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Enum2(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    e1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    e2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info1(__talloc.Object):
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

    v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info2(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info3(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info4(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info5(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    v1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info6(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    info1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class info7(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    info4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class rpcecho(__dcerpc.ClientConnection):
    """
    rpcecho(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Simple echo pipe
    """
    def AddOne(self, in_data): # real signature unknown; restored from __doc__
        """ S.AddOne(in_data) -> out_data """
        pass

    def EchoData(self, in_data): # real signature unknown; restored from __doc__
        """ S.EchoData(in_data) -> out_data """
        pass

    def SinkData(self, data): # real signature unknown; restored from __doc__
        """ S.SinkData(data) -> None """
        pass

    def SourceData(self, len): # real signature unknown; restored from __doc__
        """ S.SourceData(len) -> data """
        pass

    def TestCall(self, s1): # real signature unknown; restored from __doc__
        """ S.TestCall(s1) -> s2 """
        pass

    def TestCall2(self, level): # real signature unknown; restored from __doc__
        """ S.TestCall2(level) -> info """
        pass

    def TestDoublePointer(self, data): # real signature unknown; restored from __doc__
        """ S.TestDoublePointer(data) -> result """
        pass

    def TestEnum(self, foo1, foo2, foo3): # real signature unknown; restored from __doc__
        """ S.TestEnum(foo1, foo2, foo3) -> (foo1, foo2, foo3) """
        pass

    def TestSleep(self, seconds): # real signature unknown; restored from __doc__
        """ S.TestSleep(seconds) -> result """
        pass

    def TestSurrounding(self, data): # real signature unknown; restored from __doc__
        """ S.TestSurrounding(data) -> data """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Surrounding(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    surrounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



