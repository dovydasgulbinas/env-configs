# encoding: utf-8
# module gtk.gdk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.143
# no doc

# imports
from exceptions import Warning

import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import pango as __pango
import pangocairo as __pangocairo


class Device(__gobject__gobject.GObject):
    """
    Object GdkDevice
    
    Signals from GObject:
      notify (GParam)
    """
    def get_axis(self, *args, **kwargs): # real signature unknown
        pass

    def get_axis_use(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def get_history(self, *args, **kwargs): # real signature unknown
        pass

    def get_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_axes(self, *args, **kwargs): # real signature unknown
        pass

    def get_source(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_axis_use(self, *args, **kwargs): # real signature unknown
        pass

    def set_key(self, *args, **kwargs): # real signature unknown
        pass

    def set_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_source(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


