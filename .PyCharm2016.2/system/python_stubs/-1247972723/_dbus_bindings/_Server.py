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


from object import object

class _Server(object):
    """
    A D-Bus server.
    
    ::
    
       Server(address, connection_subtype, mainloop=None, auth_mechanisms=None)
         -> Server
    """
    def disconnect(self): # real signature unknown; restored from __doc__
        """
        disconnect()
        
        Releases the server's address and stops listening for new clients.
        
        If called more than once, only the first call has an effect.
        """
        pass

    def get_address(self): # real signature unknown; restored from __doc__
        """
        get_address() -> str
        
        Returns the address of the server.
        """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """
        get_id() -> str
        
        Returns the unique ID of the server.
        """
        return ""

    def get_is_connected(self): # real signature unknown; restored from __doc__
        """
        get_is_connected() -> bool
        
        Return true if this Server is still listening for new connections.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


