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


class Mount(__gobject.GInterface):
    # no doc
    def can_eject(self, *args, **kwargs): # real signature unknown
        pass

    def can_unmount(self, *args, **kwargs): # real signature unknown
        pass

    def eject(self, callback, flags=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        F.eject(callback, [flags, cancellable, user_data])
        Ejects a volume.
        
        If cancellable is not None, then the operation can be cancelled by
        triggering the cancellable object from another thread. If the
        operation was cancelled, the error gio.ERROR_CANCELLED will be returned.
        
        When the operation is finished, callback will be called. You can
        then call gio.Volume.eject_finish() to get the result of the operation.
        """
        pass

    def eject_finish(self, *args, **kwargs): # real signature unknown
        pass

    def eject_with_operation(self, *args, **kwargs): # real signature unknown
        pass

    def eject_with_operation_finish(self, *args, **kwargs): # real signature unknown
        pass

    def get_drive(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_root(self, *args, **kwargs): # real signature unknown
        pass

    def get_uuid(self, *args, **kwargs): # real signature unknown
        pass

    def get_volume(self, *args, **kwargs): # real signature unknown
        pass

    def guess_content_type(self, *args, **kwargs): # real signature unknown
        pass

    def guess_content_type_finish(self, *args, **kwargs): # real signature unknown
        pass

    def guess_content_type_sync(self, *args, **kwargs): # real signature unknown
        pass

    def is_shadowed(self, *args, **kwargs): # real signature unknown
        pass

    def remount(self, callback, flags=None, mount_operation=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        M.remount(callback, [flags, [mount_operation, [cancellable, [user_data]]]])
        Remounts a mount. This is an asynchronous operation, and is finished by
        calling gio.Mount.remount_finish with the mount and gio.AsyncResults data
        returned in the callback.
        """
        pass

    def remount_finish(self, *args, **kwargs): # real signature unknown
        pass

    def shadow(self, *args, **kwargs): # real signature unknown
        pass

    def unmount(self, callback, flags=None, cancellable=None, user_data=None): # real signature unknown; restored from __doc__
        """
        M.unmount(callback, [flags, cancellable, user_data])
        Unmounts a mount. This is an asynchronous operation, and is finished
        by calling gio.Mount.unmount_finish() with the mount and gio.AsyncResults
        data returned in the callback.
        """
        pass

    def unmount_finish(self, *args, **kwargs): # real signature unknown
        pass

    def unmount_with_operation(self, *args, **kwargs): # real signature unknown
        pass

    def unmount_with_operation_finish(self, *args, **kwargs): # real signature unknown
        pass

    def unshadow(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __gtype__ = None # (!) real value is ''


