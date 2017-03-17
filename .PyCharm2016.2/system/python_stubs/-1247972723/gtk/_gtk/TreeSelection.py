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


class TreeSelection(__gobject__gobject.GObject):
    """
    Object GtkTreeSelection
    
    Signals from GtkTreeSelection:
      changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def count_selected_rows(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_selected(self, *args, **kwargs): # real signature unknown
        pass

    def get_selected_rows(self, *args, **kwargs): # real signature unknown
        pass

    def get_tree_view(self, *args, **kwargs): # real signature unknown
        pass

    def iter_is_selected(self, *args, **kwargs): # real signature unknown
        pass

    def path_is_selected(self, *args, **kwargs): # real signature unknown
        pass

    def selected_foreach(self, *args, **kwargs): # real signature unknown
        pass

    def select_all(self, *args, **kwargs): # real signature unknown
        pass

    def select_iter(self, *args, **kwargs): # real signature unknown
        pass

    def select_path(self, *args, **kwargs): # real signature unknown
        pass

    def select_range(self, *args, **kwargs): # real signature unknown
        pass

    def set_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_select_function(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_all(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_iter(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_path(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_range(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


