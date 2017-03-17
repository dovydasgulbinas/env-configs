# encoding: utf-8
# module gio._gio
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gio/_gio.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gio as __gio
import glib as __glib
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class InetSocketAddress(__gio.SocketAddress):
    """
    Object GInetSocketAddress
    
    Properties from GInetSocketAddress:
      address -> GInetAddress: Address
        The address
      port -> guint: Port
        The port
      flowinfo -> guint: Flow info
        IPv6 flow info
      scope-id -> guint: Scope ID
        IPv6 scope ID
    
    Properties from GSocketAddress:
      family -> GSocketFamily: Address family
        The family of the socket address
    
    Signals from GObject:
      notify (GParam)
    """
    def get_address(self, *args, **kwargs): # real signature unknown
        pass

    def get_port(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


