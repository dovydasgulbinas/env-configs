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


from int import int

class _IntBase(int):
    """
    Base class for int subclasses with a ``variant_level`` attribute.
    Do not rely on the existence of this class outside dbus-python.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



