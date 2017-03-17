# encoding: utf-8
# module gobject._gobject
# from /usr/lib/python2.7/dist-packages/gobject/_gobject.x86_64-linux-gnu.so
# by generator 1.143
# no doc
# no imports

# Variables with simple values

G_MAXDOUBLE = 1.7976931348623157e+308
G_MAXFLOAT = 3.4028234663852886e+38
G_MAXINT = 2147483647
G_MAXINT16 = 32767
G_MAXINT32 = 2147483647
G_MAXINT64 = 9223372036854775807L
G_MAXINT8 = 127
G_MAXLONG = 9223372036854775807L
G_MAXOFFSET = 9223372036854775807L
G_MAXSHORT = 32767
G_MAXSIZE = 18446744073709551615L
G_MAXSSIZE = 9223372036854775807L
G_MAXUINT = 4294967295L
G_MAXUINT16 = 65535
G_MAXUINT32 = 4294967295L
G_MAXUINT64 = 18446744073709551615L
G_MAXUINT8 = 255
G_MAXULONG = 18446744073709551615L
G_MAXUSHORT = 65535
G_MINDOUBLE = 2.2250738585072014e-308
G_MINFLOAT = 1.1754943508222875e-38
G_MININT = -2147483648
G_MININT16 = -32768
G_MININT32 = -2147483648
G_MININT64 = -9223372036854775808L
G_MININT8 = -128
G_MINLONG = -9223372036854775808L
G_MINOFFSET = -9223372036854775808L
G_MINSHORT = -32768

PARAM_CONSTRUCT = 4

PARAM_CONSTRUCT_ONLY = 8

PARAM_LAX_VALIDATION = 16

PARAM_READABLE = 1
PARAM_READWRITE = 3
PARAM_WRITABLE = 2

SIGNAL_ACTION = 32
SIGNAL_DETAILED = 16

SIGNAL_NO_HOOKS = 64
SIGNAL_NO_RECURSE = 8

SIGNAL_RUN_CLEANUP = 4
SIGNAL_RUN_FIRST = 1
SIGNAL_RUN_LAST = 2

# functions

def add_emission_hook(*args, **kwargs): # real signature unknown
    pass

def list_properties(*args, **kwargs): # real signature unknown
    pass

def new(*args, **kwargs): # real signature unknown
    pass

def remove_emission_hook(*args, **kwargs): # real signature unknown
    pass

def signal_accumulator_true_handled(*args, **kwargs): # real signature unknown
    pass

def signal_list_ids(*args, **kwargs): # real signature unknown
    pass

def signal_list_names(*args, **kwargs): # real signature unknown
    pass

def signal_lookup(*args, **kwargs): # real signature unknown
    pass

def signal_name(*args, **kwargs): # real signature unknown
    pass

def signal_new(*args, **kwargs): # real signature unknown
    pass

def signal_query(*args, **kwargs): # real signature unknown
    pass

def threads_init(*args, **kwargs): # real signature unknown
    pass

def type_children(*args, **kwargs): # real signature unknown
    pass

def type_from_name(*args, **kwargs): # real signature unknown
    pass

def type_interfaces(*args, **kwargs): # real signature unknown
    pass

def type_is_a(*args, **kwargs): # real signature unknown
    pass

def type_name(*args, **kwargs): # real signature unknown
    pass

def type_parent(*args, **kwargs): # real signature unknown
    pass

def type_register(*args, **kwargs): # real signature unknown
    pass

def _install_metaclass(*args, **kwargs): # real signature unknown
    pass

# classes

class GBoxed(object):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __gtype__ = None # (!) real value is ''


class GEnum(int):
    # no doc
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class GFlags(int):
    # no doc
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class GInterface(object):
    """ Interface GInterface """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gdoc__ = 'Interface GInterface\n\n'
    __gtype__ = None # (!) real value is ''


class GObject(object):
    """
    Object GObject
    
    Signals from GObject:
      notify (GParam)
    """
    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def freeze_notify(self, *args, **kwargs): # real signature unknown
        pass

    def get_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def handler_block(self, *args, **kwargs): # real signature unknown
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(self, *args, **kwargs): # real signature unknown
        pass

    def handler_is_connected(self, *args, **kwargs): # real signature unknown
        pass

    def handler_unblock(self, *args, **kwargs): # real signature unknown
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        pass

    def set_data(self, *args, **kwargs): # real signature unknown
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def stop_emission(self, *args, **kwargs): # real signature unknown
        pass

    def thaw_notify(self, *args, **kwargs): # real signature unknown
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gobject_init__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is ''
    __dict__ = None # (!) real value is ''
    __gdoc__ = 'Object GObject\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gtype__ = None # (!) real value is ''


class GObjectWeakRef(object):
    """ A GObject weak reference """
    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class GParamSpec(object):
    # no doc
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class GPointer(object):
    # no doc
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __gtype__ = None # (!) real value is ''


class GType(object):
    # no doc
    def from_name(self, *args, **kwargs): # real signature unknown
        pass

    def has_value_table(self, *args, **kwargs): # real signature unknown
        pass

    def is_a(self, *args, **kwargs): # real signature unknown
        pass

    def is_abstract(self, *args, **kwargs): # real signature unknown
        pass

    def is_classed(self, *args, **kwargs): # real signature unknown
        pass

    def is_deep_derivable(self, *args, **kwargs): # real signature unknown
        pass

    def is_derivable(self, *args, **kwargs): # real signature unknown
        pass

    def is_instantiatable(self, *args, **kwargs): # real signature unknown
        pass

    def is_interface(self, *args, **kwargs): # real signature unknown
        pass

    def is_value_abstract(self, *args, **kwargs): # real signature unknown
        pass

    def is_value_type(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fundamental = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pytype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Warning(Warning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

features = {
    'generic-c-marshaller': True,
}

pygobject_version = (
    2,
    28,
    6,
)

pygtk_version = (
    2,
    28,
    6,
)

TYPE_GSTRING = None # (!) real value is ''

TYPE_INVALID = None # (!) real value is ''

_PyGObject_API = None # (!) real value is ''

