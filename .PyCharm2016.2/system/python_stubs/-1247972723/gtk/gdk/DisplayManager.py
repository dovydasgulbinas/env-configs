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


class DisplayManager(__gobject__gobject.GObject):
    """
    Object GdkDisplayManager
    
    Signals from GdkDisplayManager:
      display-opened (GdkDisplay)
    
    Properties from GdkDisplayManager:
      default-display -> GdkDisplay: Default Display
        The default display for GDK
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_display_opened(cls, *args, **kwargs): # real signature unknown
        pass

    def get_default_display(self, *args, **kwargs): # real signature unknown
        pass

    def list_displays(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_display(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


