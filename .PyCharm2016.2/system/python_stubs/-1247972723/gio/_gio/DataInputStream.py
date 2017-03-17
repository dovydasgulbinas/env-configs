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


class DataInputStream(__gio.FilterInputStream, __gio.Seekable):
    """
    Object GDataInputStream
    
    Properties from GDataInputStream:
      byte-order -> GDataStreamByteOrder: Byte order
        The byte order
      newline-type -> GDataStreamNewlineType: Newline type
        The accepted types of line ending
    
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
    def get_byte_order(self, *args, **kwargs): # real signature unknown
        pass

    def get_newline_type(self, *args, **kwargs): # real signature unknown
        pass

    def read_byte(self, *args, **kwargs): # real signature unknown
        pass

    def read_int16(self, *args, **kwargs): # real signature unknown
        pass

    def read_int32(self, *args, **kwargs): # real signature unknown
        pass

    def read_int64(self, *args, **kwargs): # real signature unknown
        pass

    def read_line(self, cancellable=None): # real signature unknown; restored from __doc__
        """
        S.read_line([cancellable]) -> str
        Read a line from the stream. Return value includes ending newline
        character.
        """
        return ""

    def read_line_async(self, *args, **kwargs): # real signature unknown
        pass

    def read_line_finish(self, *args, **kwargs): # real signature unknown
        pass

    def read_uint16(self, *args, **kwargs): # real signature unknown
        pass

    def read_uint32(self, *args, **kwargs): # real signature unknown
        pass

    def read_uint64(self, *args, **kwargs): # real signature unknown
        pass

    def read_until(self, stop_chars, cancellable=None): # real signature unknown; restored from __doc__
        """
        S.read_until(stop_chars, [cancellable]) -> str
        Read characters from the string, stopping at the end or upon reading
        any character in stop_chars. Return value does not include the stopping
        character.
        """
        return ""

    def read_until_async(self, *args, **kwargs): # real signature unknown
        pass

    def read_until_finish(self, *args, **kwargs): # real signature unknown
        pass

    def set_byte_order(self, *args, **kwargs): # real signature unknown
        pass

    def set_newline_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


