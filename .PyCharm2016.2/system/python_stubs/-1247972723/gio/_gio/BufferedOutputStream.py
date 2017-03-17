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


class BufferedOutputStream(__gio.FilterOutputStream, __gio.Seekable):
    """
    Object GBufferedOutputStream
    
    Properties from GBufferedOutputStream:
      buffer-size -> guint: Buffer Size
        The size of the backend buffer
      auto-grow -> gboolean: Auto-grow
        Whether the buffer should automatically grow
    
    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: The Filter Base Stream
        The underlying base stream on which the io ops will be done.
      close-base-stream -> gboolean: Close Base Stream
        If the base stream should be closed when the filter stream is closed.
    
    Signals from GObject:
      notify (GParam)
    """
    def get_auto_grow(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_auto_grow(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


