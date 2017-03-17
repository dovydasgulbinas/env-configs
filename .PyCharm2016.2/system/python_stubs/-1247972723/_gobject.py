# encoding: utf-8
# module _gobject
# from /usr/lib/python2.7/dist-packages/gi/_gi_cairo.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
from gobject import (GBoxed, GEnum, GFlags, GInterface, GParamSpec, GPointer, 
    GType, Warning)


# Variables with simple values

G_MAXDOUBLE = 1.7976931348623157e+308
G_MAXFLOAT = 3.4028234663852886e+38
G_MAXINT = 2147483647
G_MAXLONG = 9223372036854775807L
G_MAXOFFSET = 9223372036854775807L
G_MAXSHORT = 32767
G_MAXSIZE = 18446744073709551615L
G_MAXSSIZE = 9223372036854775807L
G_MAXUINT = 4294967295L
G_MAXULONG = 18446744073709551615L
G_MAXUSHORT = 65535
G_MINDOUBLE = 2.2250738585072014e-308
G_MINFLOAT = 1.1754943508222875e-38
G_MININT = -2147483648
G_MINLONG = -9223372036854775808L
G_MINOFFSET = -9223372036854775808L
G_MINSHORT = -32768
G_MINSSIZE = -9223372036854775808L

PARAM_READWRITE = 3

SIGNAL_RUN_FIRST = 1

# functions

def add_emission_hook(*args, **kwargs): # real signature unknown
    pass

def list_properties(*args, **kwargs): # real signature unknown
    pass

def new(*args, **kwargs): # real signature unknown
    pass

def signal_accumulator_true_handled(*args, **kwargs): # real signature unknown
    pass

def signal_new(*args, **kwargs): # real signature unknown
    pass

def type_from_name(*args, **kwargs): # real signature unknown
    pass

def type_is_a(*args, **kwargs): # real signature unknown
    pass

def type_name(*args, **kwargs): # real signature unknown
    pass

def type_register(*args, **kwargs): # real signature unknown
    pass

def _gvalue_get(*args, **kwargs): # real signature unknown
    pass

def _gvalue_set(*args, **kwargs): # real signature unknown
    pass

def _install_metaclass(*args, **kwargs): # real signature unknown
    pass

# classes

class GObject(object):
    """
    Object GObject
    
    Signals from GObject:
      notify (GParam)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

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

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


# variables with complex values

features = {
    'generic-c-marshaller': True,
}

pygobject_version = (
    3,
    20,
    0,
)

TYPE_GSTRING = None # (!) real value is ''

TYPE_INVALID = None # (!) real value is ''

_PyGObject_API = None # (!) real value is ''

