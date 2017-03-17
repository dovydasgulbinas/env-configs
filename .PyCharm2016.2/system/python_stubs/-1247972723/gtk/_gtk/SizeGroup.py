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


from Buildable import Buildable

class SizeGroup(__gobject__gobject.GObject, Buildable):
    """
    Object GtkSizeGroup
    
    Properties from GtkSizeGroup:
      mode -> GtkSizeGroupMode: Mode
        The directions in which the size group affects the requested sizes of its component widgets
      ignore-hidden -> gboolean: Ignore hidden
        If TRUE, unmapped widgets are ignored when determining the size of the group
    
    Signals from GObject:
      notify (GParam)
    """
    def add_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_ignore_hidden(self, *args, **kwargs): # real signature unknown
        pass

    def get_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_widgets(self, *args, **kwargs): # real signature unknown
        pass

    def remove_widget(self, *args, **kwargs): # real signature unknown
        pass

    def set_ignore_hidden(self, *args, **kwargs): # real signature unknown
        pass

    def set_mode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


