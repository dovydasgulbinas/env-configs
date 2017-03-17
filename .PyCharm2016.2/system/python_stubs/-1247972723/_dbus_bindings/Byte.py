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


from _IntBase import _IntBase

class Byte(_IntBase):
    """
    An unsigned byte: a subtype of int, with range restricted to [0, 255].
    
    A Byte b may be converted to a str of length 1 via str(b) == chr(b).
    
    Most of the time you don't want to use this class - it mainly exists
    for symmetry with the other D-Bus types. See `dbus.ByteArray` for a
    better way to handle arrays of Byte.
    
    Constructor::
    
       dbus.Byte(integer or str of length 1[, variant_level])
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a byte, this is represented in Python by a
        Byte with variant_level==2.
    """
    def __init__(self, integer_or_str_of_length, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


