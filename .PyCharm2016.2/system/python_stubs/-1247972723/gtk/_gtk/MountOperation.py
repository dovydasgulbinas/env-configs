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


class MountOperation(__gio.MountOperation):
    """
    Object GtkMountOperation
    
    Properties from GtkMountOperation:
      parent -> GtkWindow: Parent
        The parent window
      is-showing -> gboolean: Is Showing
        Are we showing a dialog
      screen -> GdkScreen: Screen
        The screen where this window will be displayed.
    
    Signals from GMountOperation:
      ask-password (gchararray, gchararray, gchararray, GAskPasswordFlags)
      ask-question (gchararray, GStrv)
      reply (GMountOperationResult)
      aborted ()
      show-processes (gchararray, GArray, GStrv)
      show-unmount-progress (gchararray, gint64, gint64)
    
    Properties from GMountOperation:
      username -> gchararray: Username
        The user name
      password -> gchararray: Password
        The password
      anonymous -> gboolean: Anonymous
        Whether to use an anonymous user
      domain -> gchararray: Domain
        The domain of the mount operation
      password-save -> GPasswordSave: Password save
        How passwords should be saved
      choice -> gint: Choice
        The users choice
    
    Signals from GObject:
      notify (GParam)
    """
    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def is_showing(self, *args, **kwargs): # real signature unknown
        pass

    def set_parent(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


