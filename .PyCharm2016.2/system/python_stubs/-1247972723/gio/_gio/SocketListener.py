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


class SocketListener(__gobject__gobject.GObject):
    """
    Object GSocketListener
    
    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)
    
    Properties from GSocketListener:
      listen-backlog -> gint: Listen backlog
        outstanding connections in the listen queue
    
    Signals from GObject:
      notify (GParam)
    """
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def accept_async(self, *args, **kwargs): # real signature unknown
        pass

    def accept_finish(self, *args, **kwargs): # real signature unknown
        pass

    def accept_socket(self, *args, **kwargs): # real signature unknown
        pass

    def accept_socket_async(self, *args, **kwargs): # real signature unknown
        pass

    def accept_socket_finish(self, *args, **kwargs): # real signature unknown
        pass

    def add_address(self, *args, **kwargs): # real signature unknown
        pass

    def add_inet_port(self, *args, **kwargs): # real signature unknown
        pass

    def add_socket(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def set_backlog(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


