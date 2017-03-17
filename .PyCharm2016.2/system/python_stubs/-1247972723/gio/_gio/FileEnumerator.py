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


class FileEnumerator(__gobject__gobject.GObject):
    """
    Object GFileEnumerator
    
    Properties from GFileEnumerator:
      container -> GFile: Container
        The container that is being enumerated
    
    Signals from GObject:
      notify (GParam)
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def close_async(self, *args, **kwargs): # real signature unknown
        pass

    def close_finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_container(self, *args, **kwargs): # real signature unknown
        pass

    def has_pending(self, *args, **kwargs): # real signature unknown
        pass

    def is_closed(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def next_file(self, *args, **kwargs): # real signature unknown
        pass

    def next_files_async(self, num_files, callback, io_priority=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        FE.next_files_async(num_files, callback, [io_priority, cancellable,
                            user_data])
        Request information for a number of files from the enumerator
        asynchronously. When all i/o for the operation is finished the callback
        will be called with the requested information.
        
        The callback can be called with less than num_files files in case of error
        or at the end of the enumerator. In case of a partial error the callback
        will be called with any succeeding items and no error, and on the next
        request the error will be reported. If a request is cancelled the callback
        will be called with gio.ERROR_CANCELLED.
        
        During an async request no other sync and async calls are allowed, and will
        result in gio.ERROR_PENDING errors.
        
        Any outstanding i/o request with higher priority (lower numerical value)
        will be executed before an outstanding request with lower priority.
        Default priority is gobject.PRIORITY_DEFAULT.
        """
        pass

    def next_files_finish(self, result): # real signature unknown; restored from __doc__
        """
        FE.next_files_finish(result) -> a list of gio.FileInfos
        Finishes the asynchronous operation started with
        gio.FileEnumerator.next_files_async().
        """
        pass

    def set_pending(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


