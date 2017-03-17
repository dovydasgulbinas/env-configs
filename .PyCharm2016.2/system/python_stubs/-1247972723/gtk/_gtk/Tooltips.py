# encoding: utf-8
# module gtk._gtk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.143
# no doc

# imports
import atk as __atk
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


from Object import Object

class Tooltips(Object):
    """
    Object GtkTooltips
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def disable(self, *args, **kwargs): # real signature unknown
        pass

    def enable(self, *args, **kwargs): # real signature unknown
        pass

    def force_window(self, *args, **kwargs): # real signature unknown
        pass

    def set_delay(self, *args, **kwargs): # real signature unknown
        pass

    def set_tip(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    active_tips_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timer_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tips_data_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tip_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tip_window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_sticky_delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


