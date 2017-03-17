# encoding: utf-8
# module _dbus_bindings
# from /usr/lib/python2.7/dist-packages/_dbus_bindings.x86_64-linux-gnu.so
# by generator 1.143
"""
Low-level Python bindings for libdbus. Don't use this module directly -
the public API is provided by the `dbus`, `dbus.service`, `dbus.mainloop`
and `dbus.mainloop.glib` modules, with a lower-level API provided by the
`dbus.lowlevel` module.
"""

# imports
import dbus.lowlevel as __dbus_lowlevel


from tuple import tuple

class Struct(tuple):
    """
    An structure containing items of possibly distinct types.
    
    Constructor::
    
        dbus.Struct(iterable, signature=None, variant_level=0) -> Struct
    
    D-Bus structs may not be empty, so the iterable argument is required and
    may not be an empty iterable.
    
    ``signature`` is either None, or a string representing the contents of the
    struct as one or more complete type signatures. The overall signature of
    the struct will be the given signature enclosed in parentheses, ``()``.
    
    If the signature is None (default) it will be guessed
    from the types of the items during construction.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a struct, this is represented in Python by a
        Struct with variant_level==2.
    """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, iterable, signature=None, variant_level=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


