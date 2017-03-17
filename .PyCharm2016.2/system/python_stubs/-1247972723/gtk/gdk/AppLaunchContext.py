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


class AppLaunchContext(__gio.AppLaunchContext):
    """
    Object GdkAppLaunchContext
    
    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launched (GAppInfo, GVariant)
    
    Signals from GObject:
      notify (GParam)
    """
    def set_desktop(self, *args, **kwargs): # real signature unknown
        pass

    def set_display(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def set_timestamp(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


