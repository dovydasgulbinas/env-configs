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

class IMContext(Object):
    """
    Object GtkIMContext
    
    Signals from GtkIMContext:
      preedit-changed ()
      preedit-start ()
      preedit-end ()
      commit (gchararray)
      retrieve-surrounding () -> gboolean
      delete-surrounding (gint, gint) -> gboolean
    
    Signals from GObject:
      notify (GParam)
    """
    def delete_surrounding(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_commit(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delete_surrounding(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_filter_keypress(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus_in(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus_out(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_preedit_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_preedit_end(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_preedit_start(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_reset(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_retrieve_surrounding(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_client_window(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_cursor_location(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_surrounding(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_use_preedit(cls, *args, **kwargs): # real signature unknown
        pass

    def filter_keypress(self, *args, **kwargs): # real signature unknown
        pass

    def focus_in(self, *args, **kwargs): # real signature unknown
        pass

    def focus_out(self, *args, **kwargs): # real signature unknown
        pass

    def get_preedit_string(self, *args, **kwargs): # real signature unknown
        pass

    def get_surrounding(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def set_client_window(self, *args, **kwargs): # real signature unknown
        pass

    def set_cursor_location(self, *args, **kwargs): # real signature unknown
        pass

    def set_surrounding(self, *args, **kwargs): # real signature unknown
        pass

    def set_use_preedit(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


