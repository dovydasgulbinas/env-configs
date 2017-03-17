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


class EntryBuffer(__gobject__gobject.GObject):
    """
    Object GtkEntryBuffer
    
    Signals from GtkEntryBuffer:
      inserted-text (guint, gchararray, guint)
      deleted-text (guint, guint)
    
    Properties from GtkEntryBuffer:
      text -> gchararray: Text
        The contents of the buffer
      length -> guint: Text length
        Length of the text currently in the buffer
      max-length -> gint: Maximum length
        Maximum number of characters for this entry. Zero if no maximum
    
    Signals from GObject:
      notify (GParam)
    """
    def delete_text(self, *args, **kwargs): # real signature unknown
        pass

    def emit_deleted_text(self, *args, **kwargs): # real signature unknown
        pass

    def emit_inserted_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_bytes(self, *args, **kwargs): # real signature unknown
        pass

    def get_length(self, *args, **kwargs): # real signature unknown
        pass

    def get_max_length(self, *args, **kwargs): # real signature unknown
        pass

    def get_text(self, *args, **kwargs): # real signature unknown
        pass

    def insert_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_max_length(self, *args, **kwargs): # real signature unknown
        pass

    def set_text(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


