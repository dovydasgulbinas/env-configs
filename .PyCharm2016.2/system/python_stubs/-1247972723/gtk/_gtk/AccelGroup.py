# encoding: utf-8
# module gtk._gtk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.143
# no doc

# imports
import atk as __atk
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class AccelGroup(__gobject__gobject.GObject):
    """
    Object GtkAccelGroup
    
    Signals from GtkAccelGroup:
      accel-activate (GObject, guint, GdkModifierType) -> gboolean
      accel-changed (guint, GdkModifierType, GClosure)
    
    Properties from GtkAccelGroup:
      is-locked -> gboolean: Is locked
        Is the accel group locked
      modifier-mask -> GdkModifierType: Modifier Mask
        Modifier Mask
    
    Signals from GObject:
      notify (GParam)
    """
    def connect_by_path(self, *args, **kwargs): # real signature unknown
        pass

    def connect_group(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_key(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_accel_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_is_locked(self, *args, **kwargs): # real signature unknown
        pass

    def get_modifier_mask(self, *args, **kwargs): # real signature unknown
        pass

    def lock(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


