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


class MountOperation(__gobject__gobject.GObject):
    """
    Object GMountOperation
    
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
    def get_anonymous(self, *args, **kwargs): # real signature unknown
        pass

    def get_choice(self, *args, **kwargs): # real signature unknown
        pass

    def get_domain(self, *args, **kwargs): # real signature unknown
        pass

    def get_password(self, *args, **kwargs): # real signature unknown
        pass

    def get_password_save(self, *args, **kwargs): # real signature unknown
        pass

    def get_username(self, *args, **kwargs): # real signature unknown
        pass

    def reply(self, *args, **kwargs): # real signature unknown
        pass

    def set_anonymous(self, *args, **kwargs): # real signature unknown
        pass

    def set_choice(self, *args, **kwargs): # real signature unknown
        pass

    def set_domain(self, *args, **kwargs): # real signature unknown
        pass

    def set_password(self, *args, **kwargs): # real signature unknown
        pass

    def set_password_save(self, *args, **kwargs): # real signature unknown
        pass

    def set_username(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


