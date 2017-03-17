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


class LoadableIcon(__gobject.GInterface):
    # no doc
    def load(self, size=None, cancellable=None): # real signature unknown; restored from __doc__
        """
        ICON.load([size, [cancellable]]) -> input stream, type
        
        Opens a stream of icon data for reading. The result is a tuple of
        gio.InputStream and type (either a string or None). The stream can
        be read to retrieve icon data.
        
        Optional size is a hint at desired icon size. Not all implementations
        support it and the hint will be just ignored in such cases.
        If cancellable is specified, then the operation can be cancelled
        by triggering the cancellable object from another thread. See
        gio.File.read for details.
        """
        pass

    def load_async(self, callback, size=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        ICON.load_async(callback, [size, [cancellable, [user_data]]])
        -> start loading
        
        For more information, see gio.LoadableIcon.load() which is the
        synchronous version of this call. Asynchronously opens icon data for
        reading. When the operation is finished, callback will be called.
        You can then call gio.LoadableIcon.load_finish() to get the result of
        the operation.
        """
        pass

    def load_finish(self, res): # real signature unknown; restored from __doc__
        """
        F.load_finish(res) -> start loading
        
        Finish asynchronous icon loading operation. Must be called from callback
        as specified to gio.LoadableIcon.load_async. Returns a tuple of
        gio.InputStream and type, just as gio.LoadableIcon.load.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


