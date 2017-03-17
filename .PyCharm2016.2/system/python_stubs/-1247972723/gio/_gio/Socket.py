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


class Socket(__gobject__gobject.GObject, __gio.Initable, __gio.__main__.GDatagramBased):
    """
    Object GSocket
    
    Properties from GSocket:
      family -> GSocketFamily: Socket family
        The sockets address family
      type -> GSocketType: Socket type
        The sockets type
      protocol -> GSocketProtocol: Socket protocol
        The id of the protocol to use, or -1 for unknown
      fd -> gint: File descriptor
        The sockets file descriptor
      blocking -> gboolean: blocking
        Whether or not I/O on this socket is blocking
      listen-backlog -> gint: Listen backlog
        Outstanding connections in the listen queue
      keepalive -> gboolean: Keep connection alive
        Keep connection alive by sending periodic pings
      local-address -> GSocketAddress: Local address
        The local address the socket is bound to
      remote-address -> GSocketAddress: Remote address
        The remote address the socket is connected to
      timeout -> guint: Timeout
        The timeout in seconds on socket I/O
      ttl -> guint: TTL
        Time-to-live of outgoing unicast packets
      broadcast -> gboolean: Broadcast
        Whether to allow sending to broadcast addresses
      multicast-loopback -> gboolean: Multicast loopback
        Whether outgoing multicast packets loop back to the local host
      multicast-ttl -> guint: Multicast TTL
        Time-to-live of outgoing multicast packets
    
    Signals from GObject:
      notify (GParam)
    """
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def check_connect_result(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def condition_check(self, *args, **kwargs): # real signature unknown
        pass

    def condition_wait(self, *args, **kwargs): # real signature unknown
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connection_factory_create_connection(self, *args, **kwargs): # real signature unknown
        pass

    def get_blocking(self, *args, **kwargs): # real signature unknown
        pass

    def get_family(self, *args, **kwargs): # real signature unknown
        pass

    def get_fd(self, *args, **kwargs): # real signature unknown
        pass

    def get_keepalive(self, *args, **kwargs): # real signature unknown
        pass

    def get_listen_backlog(self, *args, **kwargs): # real signature unknown
        pass

    def get_local_address(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def get_remote_address(self, *args, **kwargs): # real signature unknown
        pass

    def get_socket_type(self, *args, **kwargs): # real signature unknown
        pass

    def is_closed(self, *args, **kwargs): # real signature unknown
        pass

    def is_connected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, *args, **kwargs): # real signature unknown
        pass

    def receive(self, *args, **kwargs): # real signature unknown
        pass

    def send(self, *args, **kwargs): # real signature unknown
        pass

    def send_to(self, *args, **kwargs): # real signature unknown
        pass

    def set_blocking(self, *args, **kwargs): # real signature unknown
        pass

    def set_keepalive(self, *args, **kwargs): # real signature unknown
        pass

    def set_listen_backlog(self, *args, **kwargs): # real signature unknown
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        pass

    def speaks_ipv4(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


