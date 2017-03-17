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


class Display(__gobject__gobject.GObject):
    """
    Object GdkDisplay
    
    Signals from GdkDisplay:
      closed (gboolean)
    
    Signals from GObject:
      notify (GParam)
    """
    def beep(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_closed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_default_screen(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_display_name(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_n_screens(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_screen(cls, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def get_core_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_cursor_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_event(self, *args, **kwargs): # real signature unknown
        pass

    def get_maximal_cursor_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_screens(self, *args, **kwargs): # real signature unknown
        pass

    def get_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_user_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_at_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def grab(self, *args, **kwargs): # real signature unknown
        pass

    def is_closed(self, *args, **kwargs): # real signature unknown
        pass

    def keyboard_ungrab(self, *args, **kwargs): # real signature unknown
        pass

    def list_devices(self, *args, **kwargs): # real signature unknown
        pass

    def peek_event(self, *args, **kwargs): # real signature unknown
        pass

    def pointer_is_grabbed(self, *args, **kwargs): # real signature unknown
        pass

    def pointer_ungrab(self, *args, **kwargs): # real signature unknown
        pass

    def put_event(self, *args, **kwargs): # real signature unknown
        pass

    def request_selection_notification(self, *args, **kwargs): # real signature unknown
        pass

    def set_double_click_distance(self, *args, **kwargs): # real signature unknown
        pass

    def set_double_click_time(self, *args, **kwargs): # real signature unknown
        pass

    def store_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def supports_clipboard_persistence(self, *args, **kwargs): # real signature unknown
        pass

    def supports_composite(self, *args, **kwargs): # real signature unknown
        pass

    def supports_cursor_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def supports_cursor_color(self, *args, **kwargs): # real signature unknown
        pass

    def supports_input_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def supports_selection_notification(self, *args, **kwargs): # real signature unknown
        pass

    def supports_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def sync(self, *args, **kwargs): # real signature unknown
        pass

    def ungrab(self, *args, **kwargs): # real signature unknown
        pass

    def warp_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


