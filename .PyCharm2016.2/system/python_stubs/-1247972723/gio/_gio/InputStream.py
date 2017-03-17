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


class InputStream(__gobject__gobject.GObject):
    """
    Object GInputStream
    
    Signals from GObject:
      notify (GParam)
    """
    def clear_pending(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def close_async(self, *args, **kwargs): # real signature unknown
        pass

    def close_finish(self, *args, **kwargs): # real signature unknown
        pass

    def has_pending(self, *args, **kwargs): # real signature unknown
        pass

    def is_closed(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, count=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        STREAM.read([count, [cancellable]]) -> string
        
        Read 'count' bytes from the stream. If 'count' is not specified or is
        omitted, read until the end of the stream. This method will stop only
        after reading requested number of bytes, reaching end of stream or
        triggering an I/O error. See also gio.InputStream.read_part for more
        efficient, but more cumbersome to use method.
        
        Note: this method roughly corresponds to C GIO g_input_stream_read_all.
        It was renamed for consistency with Python standard file.read.
        """
        return ""

    def read_async(self, *args, **kwargs): # real signature unknown
        pass

    def read_finish(self, *args, **kwargs): # real signature unknown
        pass

    def read_part(self, count=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        STREAM.read_part([count, [cancellable]]) -> string
        
        Read 'count' bytes from the stream. If 'count' is not specified or is
        omitted, read until the end of the stream. This method is allowed to
        stop at any time after reading at least 1 byte from the stream. E.g.
        when reading over a (relatively slow) HTTP connection, it will often
        stop after receiving one packet. Therefore, to reliably read requested
        number of bytes, you need to use a loop. See also gio.InputStream.read
        for easier to use (though less efficient) method.
        
        Note: this method roughly corresponds to C GIO g_input_stream_read.
        """
        return ""

    def set_pending(self, *args, **kwargs): # real signature unknown
        pass

    def skip(self, *args, **kwargs): # real signature unknown
        pass

    def skip_async(self, *args, **kwargs): # real signature unknown
        pass

    def skip_finish(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


