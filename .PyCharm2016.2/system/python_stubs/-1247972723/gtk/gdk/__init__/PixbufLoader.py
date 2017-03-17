# encoding: utf-8
# module gtk.gdk
# from /usr/lib/python2.7/dist-packages/webkit/webkit.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
from exceptions import Warning

import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import pango as __pango
import pangocairo as __pangocairo


class PixbufLoader(__gobject__gobject.GObject):
    """
    Object GdkPixbufLoader
    
    Signals from GdkPixbufLoader:
      closed ()
      size-prepared (gint, gint)
      area-prepared ()
      area-updated (gint, gint, gint, gint)
    
    Signals from GObject:
      notify (GParam)
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_area_prepared(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_area_updated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_closed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_size_prepared(cls, *args, **kwargs): # real signature unknown
        pass

    def get_animation(self, *args, **kwargs): # real signature unknown
        pass

    def get_format(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


