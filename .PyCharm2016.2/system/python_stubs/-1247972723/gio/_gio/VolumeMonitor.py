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


class VolumeMonitor(__gobject__gobject.GObject):
    """
    Object GVolumeMonitor
    
    Signals from GVolumeMonitor:
      volume-added (GVolume)
      volume-removed (GVolume)
      volume-changed (GVolume)
      mount-added (GMount)
      mount-removed (GMount)
      mount-pre-unmount (GMount)
      mount-changed (GMount)
      drive-connected (GDrive)
      drive-disconnected (GDrive)
      drive-changed (GDrive)
      drive-eject-button (GDrive)
      drive-stop-button (GDrive)
    
    Signals from GObject:
      notify (GParam)
    """
    def get_connected_drives(self, *args, **kwargs): # real signature unknown
        pass

    def get_mounts(self, *args, **kwargs): # real signature unknown
        pass

    def get_mount_for_uuid(self, *args, **kwargs): # real signature unknown
        pass

    def get_volumes(self, *args, **kwargs): # real signature unknown
        pass

    def get_volume_for_uuid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gtype__ = None # (!) real value is ''


