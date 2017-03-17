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


class DragContext(__gobject__gobject.GObject):
    """
    Object GdkDragContext
    
    Signals from GObject:
      notify (GParam)
    """
    def drag_abort(self, *args, **kwargs): # real signature unknown
        pass

    def drag_drop(self, *args, **kwargs): # real signature unknown
        pass

    def drag_drop_succeeded(self, *args, **kwargs): # real signature unknown
        pass

    def drag_find_window(self, *args, **kwargs): # real signature unknown
        pass

    def drag_find_window_for_screen(self, *args, **kwargs): # real signature unknown
        pass

    def drag_get_selection(self, *args, **kwargs): # real signature unknown
        pass

    def drag_motion(self, *args, **kwargs): # real signature unknown
        pass

    def drag_status(self, *args, **kwargs): # real signature unknown
        pass

    def drop_finish(self, *args, **kwargs): # real signature unknown
        pass

    def drop_reply(self, *args, **kwargs): # real signature unknown
        pass

    def finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_actions(self, *args, **kwargs): # real signature unknown
        pass

    def get_selected_action(self, *args, **kwargs): # real signature unknown
        pass

    def get_source_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_source_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_suggested_action(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_default(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_stock(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_widget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dest_window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suggested_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    targets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


