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


from Buildable import Buildable

class ActionGroup(__gobject__gobject.GObject, Buildable):
    """
    Object GtkActionGroup
    
    Signals from GtkActionGroup:
      connect-proxy (GtkAction, GtkWidget)
      disconnect-proxy (GtkAction, GtkWidget)
      pre-activate (GtkAction)
      post-activate (GtkAction)
    
    Properties from GtkActionGroup:
      name -> gchararray: Name
        A name for the action group.
      sensitive -> gboolean: Sensitive
        Whether the action group is enabled.
      visible -> gboolean: Visible
        Whether the action group is visible.
    
    Signals from GObject:
      notify (GParam)
    """
    def add_action(self, *args, **kwargs): # real signature unknown
        pass

    def add_actions(self, *args, **kwargs): # real signature unknown
        pass

    def add_action_with_accel(self, *args, **kwargs): # real signature unknown
        pass

    def add_radio_actions(self, *args, **kwargs): # real signature unknown
        pass

    def add_toggle_actions(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_action(cls, *args, **kwargs): # real signature unknown
        pass

    def get_action(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible(self, *args, **kwargs): # real signature unknown
        pass

    def list_actions(self, *args, **kwargs): # real signature unknown
        pass

    def remove_action(self, *args, **kwargs): # real signature unknown
        pass

    def set_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def set_translation_domain(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible(self, *args, **kwargs): # real signature unknown
        pass

    def translate_string(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


