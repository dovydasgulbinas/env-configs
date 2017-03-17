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


class FileMonitor(__gobject__gobject.GObject):
    """
    Object GFileMonitor
    
    Signals from GFileMonitor:
      changed (GFile, GFile, GFileMonitorEvent)
    
    Properties from GFileMonitor:
      rate-limit -> gint: Rate limit
        The limit of the monitor to watch for changes, in milliseconds
      cancelled -> gboolean: Cancelled
        Whether the monitor has been cancelled
    
    Signals from GObject:
      notify (GParam)
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def emit_event(self, *args, **kwargs): # real signature unknown
        pass

    def is_cancelled(self, *args, **kwargs): # real signature unknown
        pass

    def set_rate_limit(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


