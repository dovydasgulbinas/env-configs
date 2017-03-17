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


from _StrBase import _StrBase

class Signature(_StrBase):
    """
    A string subclass whose values are restricted to valid D-Bus
    signatures. When iterated over, instead of individual characters it
    produces Signature instances representing single complete types.
    
    Constructor::
    
        ``Signature(value: str or unicode[, variant_level: int]) -> Signature``
    
    ``value`` must be a valid D-Bus signature (zero or more single complete
    types).
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a signature, this is represented in Python by a
        Signature with variant_level==2.
    """
    def __init__(self, value_or_unicode, variant_level=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


