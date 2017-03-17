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

class Adjustment(Object):
    """
    Object GtkAdjustment
    
    Signals from GtkAdjustment:
      changed ()
      value-changed ()
    
    Properties from GtkAdjustment:
      value -> gdouble: Value
        The value of the adjustment
      lower -> gdouble: Minimum Value
        The minimum value of the adjustment
      upper -> gdouble: Maximum Value
        The maximum value of the adjustment
      step-increment -> gdouble: Step Increment
        The step increment of the adjustment
      page-increment -> gdouble: Page Increment
        The page increment of the adjustment
      page-size -> gdouble: Page Size
        The page size of the adjustment
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def clamp_page(self, *args, **kwargs): # real signature unknown
        pass

    def configure(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_value_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_lower(self, *args, **kwargs): # real signature unknown
        pass

    def get_page_increment(self, *args, **kwargs): # real signature unknown
        pass

    def get_page_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_step_increment(self, *args, **kwargs): # real signature unknown
        pass

    def get_upper(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def set_all(self, *args, **kwargs): # real signature unknown
        pass

    def set_lower(self, *args, **kwargs): # real signature unknown
        pass

    def set_page_increment(self, *args, **kwargs): # real signature unknown
        pass

    def set_page_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_step_increment(self, *args, **kwargs): # real signature unknown
        pass

    def set_upper(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def value_changed(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    lower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    step_increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


