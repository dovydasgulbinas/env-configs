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


class SocketService(__gio.SocketListener):
    """
    Object GSocketService
    
    Signals from GSocketService:
      incoming (GSocketConnection, GObject) -> gboolean
    
    Properties from GSocketService:
      active -> gboolean: Active
        Whether the service is currently accepting connections
    
    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)
    
    Properties from GSocketListener:
      listen-backlog -> gint: Listen backlog
        outstanding connections in the listen queue
    
    Signals from GObject:
      notify (GParam)
    """
    def is_active(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


