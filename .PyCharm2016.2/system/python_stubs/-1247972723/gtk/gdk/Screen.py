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


class Screen(__gobject__gobject.GObject):
    """
    Object GdkScreen
    
    Signals from GdkScreen:
      size-changed ()
      composited-changed ()
      monitors-changed ()
    
    Properties from GdkScreen:
      font-options -> gpointer: Font options
        The default font options for the screen
      resolution -> gdouble: Font resolution
        The resolution for fonts on the screen
    
    Signals from GObject:
      notify (GParam)
    """
    def alternative_dialog_button_order(self, *args, **kwargs): # real signature unknown
        pass

    def broadcast_client_message(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_composited_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_size_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_active_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def get_display(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_height_mm(self, *args, **kwargs): # real signature unknown
        pass

    def get_monitor_at_point(self, *args, **kwargs): # real signature unknown
        pass

    def get_monitor_at_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_monitor_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def get_monitor_height_mm(self, *args, **kwargs): # real signature unknown
        pass

    def get_monitor_plug_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_monitor_width_mm(self, *args, **kwargs): # real signature unknown
        pass

    def get_number(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_monitors(self, *args, **kwargs): # real signature unknown
        pass

    def get_primary_monitor(self, *args, **kwargs): # real signature unknown
        pass

    def get_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def get_rgba_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def get_rgba_visual(self, *args, **kwargs): # real signature unknown
        pass

    def get_rgb_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def get_rgb_visual(self, *args, **kwargs): # real signature unknown
        pass

    def get_root_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen_number(self, *args, **kwargs): # real signature unknown
        pass

    def get_setting(self, *args, **kwargs): # real signature unknown
        pass

    def get_system_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def get_system_visual(self, *args, **kwargs): # real signature unknown
        pass

    def get_toplevel_windows(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_width_mm(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_manager_name(self, *args, **kwargs): # real signature unknown
        pass

    def is_composited(self, *args, **kwargs): # real signature unknown
        pass

    def list_visuals(self, *args, **kwargs): # real signature unknown
        pass

    def make_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def supports_net_wm_hint(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


