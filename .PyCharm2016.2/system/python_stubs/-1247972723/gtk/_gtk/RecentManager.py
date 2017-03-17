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


class RecentManager(__gobject__gobject.GObject):
    """
    Object GtkRecentManager
    
    Signals from GtkRecentManager:
      changed ()
    
    Properties from GtkRecentManager:
      filename -> gchararray: Filename
        The full path to the file to be used to store and read the list
      limit -> gint: Limit
        The maximum number of items to be returned by gtk_recent_manager_get_items()
      size -> gint: Size
        The size of the recently used resources list
    
    Signals from GObject:
      notify (GParam)
    """
    def add_full(self, *args, **kwargs): # real signature unknown
        pass

    def add_item(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_items(self, *args, **kwargs): # real signature unknown
        pass

    def get_limit(self, *args, **kwargs): # real signature unknown
        pass

    def has_item(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_item(self, *args, **kwargs): # real signature unknown
        pass

    def move_item(self, *args, **kwargs): # real signature unknown
        pass

    def purge_items(self, *args, **kwargs): # real signature unknown
        pass

    def remove_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_limit(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


