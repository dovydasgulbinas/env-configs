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


class NetworkAddress(__gobject__gobject.GObject, __gio.SocketConnectable):
    """
    Object GNetworkAddress
    
    Properties from GNetworkAddress:
      hostname -> gchararray: Hostname
        Hostname to resolve
      port -> guint: Port
        Network port
      scheme -> gchararray: Scheme
        URI Scheme
    
    Signals from GObject:
      notify (GParam)
    """
    def get_hostname(self, *args, **kwargs): # real signature unknown
        pass

    def get_port(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


