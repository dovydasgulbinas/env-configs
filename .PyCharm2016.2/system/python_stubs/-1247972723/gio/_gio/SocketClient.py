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


class SocketClient(__gobject__gobject.GObject):
    """
    Object GSocketClient
    
    Signals from GSocketClient:
      event (GSocketClientEvent, GSocketConnectable, GIOStream)
    
    Properties from GSocketClient:
      family -> GSocketFamily: Socket family
        The sockets address family to use for socket construction
      type -> GSocketType: Socket type
        The sockets type to use for socket construction
      protocol -> GSocketProtocol: Socket protocol
        The protocol to use for socket construction, or 0 for default
      local-address -> GSocketAddress: Local address
        The local address constructed sockets will be bound to
      timeout -> guint: Socket timeout
        The I/O timeout for sockets, or 0 for none
      enable-proxy -> gboolean: Enable proxy
        Enable proxy support
      tls -> gboolean: TLS
        Whether to create TLS connections
      tls-validation-flags -> GTlsCertificateFlags: TLS validation flags
        TLS validation flags to use
      proxy-resolver -> GProxyResolver: Proxy resolver
        The proxy resolver to use
    
    Signals from GObject:
      notify (GParam)
    """
    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_async(self, *args, **kwargs): # real signature unknown
        pass

    def connect_finish(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_host(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_host_async(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_host_finish(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_service(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_service_async(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_service_finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_family(self, *args, **kwargs): # real signature unknown
        pass

    def get_local_address(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def get_socket_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_family(self, *args, **kwargs): # real signature unknown
        pass

    def set_local_address(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def set_socket_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


