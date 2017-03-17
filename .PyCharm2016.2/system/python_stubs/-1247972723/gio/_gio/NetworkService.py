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


class NetworkService(__gobject__gobject.GObject, __gio.SocketConnectable):
    """
    Object GNetworkService
    
    Properties from GNetworkService:
      service -> gchararray: Service
        Service name, eg "ldap"
      protocol -> gchararray: Protocol
        Network protocol, eg "tcp"
      domain -> gchararray: Domain
        Network domain, eg, "example.com"
      scheme -> gchararray: Scheme
        Network scheme (default is to use service)
    
    Signals from GObject:
      notify (GParam)
    """
    def get_domain(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def get_service(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


