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


class TcpConnection(__gio.SocketConnection):
    """
    Object GTcpConnection
    
    Properties from GTcpConnection:
      graceful-disconnect -> gboolean: Graceful Disconnect
        Whether or not close does a graceful disconnect
    
    Properties from GSocketConnection:
      socket -> GSocket: Socket
        The underlying GSocket
    
    Properties from GIOStream:
      input-stream -> GInputStream: Input stream
        The GInputStream to read from
      output-stream -> GOutputStream: Output stream
        The GOutputStream to write to
      closed -> gboolean: Closed
        Is the stream closed
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


