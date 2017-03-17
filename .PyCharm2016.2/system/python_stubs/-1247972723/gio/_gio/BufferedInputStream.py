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


class BufferedInputStream(__gio.FilterInputStream, __gio.Seekable):
    """
    Object GBufferedInputStream
    
    Properties from GBufferedInputStream:
      buffer-size -> guint: Buffer Size
        The size of the backend buffer
    
    Properties from GFilterInputStream:
      base-stream -> GInputStream: The Filter Base Stream
        The underlying base stream on which the io ops will be done.
      close-base-stream -> gboolean: Close Base Stream
        If the base stream should be closed when the filter stream is closed.
    
    Signals from GObject:
      notify (GParam)
    """
    def fill(self, *args, **kwargs): # real signature unknown
        pass

    def fill_async(self, *args, **kwargs): # real signature unknown
        pass

    def fill_finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_available(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def read_byte(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


