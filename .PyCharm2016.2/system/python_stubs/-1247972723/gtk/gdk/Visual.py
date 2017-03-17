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


class Visual(__gobject__gobject.GObject):
    """
    Object GdkVisual
    
    Signals from GObject:
      notify (GParam)
    """
    def get_bits_per_rgb(self, *args, **kwargs): # real signature unknown
        pass

    def get_byte_order(self, *args, **kwargs): # real signature unknown
        pass

    def get_colormap_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_depth(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_visual_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    bits_per_rgb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue_prec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    byte_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    colormap_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green_prec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red_prec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


