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


class Cancellable(__gobject__gobject.GObject):
    """
    Object GCancellable
    
    Signals from GCancellable:
      cancelled ()
    
    Signals from GObject:
      notify (GParam)
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self, *args, **kwargs): # real signature unknown
        pass

    def get_fd(self, *args, **kwargs): # real signature unknown
        pass

    def is_cancelled(self, *args, **kwargs): # real signature unknown
        pass

    def make_pollfd(self, *args, **kwargs): # real signature unknown
        pass

    def pop_current(self, *args, **kwargs): # real signature unknown
        pass

    def push_current(self, *args, **kwargs): # real signature unknown
        pass

    def release_fd(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_if_cancelled(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


