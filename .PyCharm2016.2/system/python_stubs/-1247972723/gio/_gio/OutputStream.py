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


class OutputStream(__gobject__gobject.GObject):
    """
    Object GOutputStream
    
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

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def flush_async(self, *args, **kwargs): # real signature unknown
        pass

    def flush_finish(self, *args, **kwargs): # real signature unknown
        pass

    def has_pending(self, *args, **kwargs): # real signature unknown
        pass

    def is_closed(self, *args, **kwargs): # real signature unknown
        pass

    def set_pending(self, *args, **kwargs): # real signature unknown
        pass

    def splice(self, *args, **kwargs): # real signature unknown
        pass

    def splice_async(self, *args, **kwargs): # real signature unknown
        pass

    def splice_finish(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def write_async(self, buffer, callback, io_priority=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        S.write_async(buffer, callback [,io_priority] [,cancellable] [,user_data])
        
        Request an asynchronous write of count bytes from buffer into the stream.
        When the operation is finished callback will be called. You can then call
        gio.OutputStream.write_finish() to get the result of the operation.
        On success, the number of bytes written will be passed to the callback.
        It is not an error if this is not the same as the requested size, as it can
        happen e.g. on a partial I/O error, but generally tries to write as many 
        bytes as requested.
        For the synchronous, blocking version of this function, see
        gio.OutputStream.write().
        """
        pass

    def write_finish(self, *args, **kwargs): # real signature unknown
        pass

    def write_part(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """
        STREAM.write_part(buffer, [cancellable]) -> int
        
        Write the bytes in 'buffer' to the stream. Return the number of bytes
        successfully written. This method is allowed to stop at any time after
        writing at least 1 byte. Therefore, to reliably write the whole buffer,
        you need to use a loop. See also gio.OutputStream.write for easier to
        use (though less efficient) method.
        
        Note: this method roughly corresponds to C GIO g_output_stream_write.
        """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


