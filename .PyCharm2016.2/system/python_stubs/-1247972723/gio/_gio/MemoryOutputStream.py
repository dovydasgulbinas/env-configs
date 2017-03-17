# encoding: utf-8
# module gio._gio
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gio/_gio.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
import gio as __gio
import glib as __glib
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class MemoryOutputStream(__gio.OutputStream, __gio.Seekable, __gio.__main__.GPollableOutputStream):
    """
    Object GMemoryOutputStream
    
    Properties from GMemoryOutputStream:
      data -> gpointer: Data Buffer
        Pointer to buffer where data will be written.
      size -> gulong: Data Buffer Size
        Current size of the data buffer.
      data-size -> gulong: Data Size
        Size of data written to the buffer.
      realloc-function -> gpointer: Memory Reallocation Function
        Function with realloc semantics called to enlarge the buffer.
      destroy-function -> gpointer: Destroy Notification Function
        Function called with the buffer as argument when the stream is destroyed.
    
    Signals from GObject:
      notify (GParam)
    """
    def get_contents(self, *args, **kwargs): # real signature unknown
        pass

    def get_data_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


