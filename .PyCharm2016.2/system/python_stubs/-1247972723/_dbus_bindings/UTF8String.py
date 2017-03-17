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

class UTF8String(_StrBase):
    """
    A string represented using UTF-8 - a subtype of `str`.
    
    All strings on D-Bus are required to be valid Unicode; in the "wire
    protocol" they're transported as UTF-8.
    
    By default, when byte arrays are converted from D-Bus to Python, they
    come out as a `dbus.String`, which is a subtype of `unicode`.
    If you prefer to get UTF-8 strings (as instances of this class) or you
    want to avoid the conversion overhead of going from UTF-8 to Python's
    internal Unicode representation, you can pass the ``utf8_strings=True``
    keyword argument to any of these methods:
    
    * any D-Bus method proxy, or ``connect_to_signal``, on the objects returned
      by `Bus.get_object`
    * any D-Bus method on a `dbus.Interface`
    * `dbus.Interface.connect_to_signal`
    * `Bus.add_signal_receiver`
    
    
    Constructor::
    
        dbus.UTF8String(value: str or unicode[, variant_level: int]) -> UTF8String
    
    If value is a str object it must be valid UTF-8.
    
    variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a string, this is represented in Python by a
        String or UTF8String with variant_level==2.
    :Since: 0.80 (in older versions, use dbus.String)
    """
    def __init__(self, value_or_unicode, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


