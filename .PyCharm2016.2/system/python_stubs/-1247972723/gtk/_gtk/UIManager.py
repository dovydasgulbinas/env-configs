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

class UIManager(__gobject__gobject.GObject, Buildable):
    """
    Object GtkUIManager
    
    Signals from GtkUIManager:
      connect-proxy (GtkAction, GtkWidget)
      disconnect-proxy (GtkAction, GtkWidget)
      pre-activate (GtkAction)
      post-activate (GtkAction)
      add-widget (GtkWidget)
      actions-changed ()
    
    Properties from GtkUIManager:
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether tearoff menu items should be added to menus
      ui -> gchararray: Merged UI definition
        An XML string describing the merged UI
    
    Signals from GObject:
      notify (GParam)
    """
    def add_ui(self, *args, **kwargs): # real signature unknown
        pass

    def add_ui_from_file(self, *args, **kwargs): # real signature unknown
        pass

    def add_ui_from_string(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_actions_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_add_widget(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_connect_proxy(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_disconnect_proxy(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_action(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_widget(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_post_activate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_pre_activate(cls, *args, **kwargs): # real signature unknown
        pass

    def ensure_update(self, *args, **kwargs): # real signature unknown
        pass

    def get_accel_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_action(self, *args, **kwargs): # real signature unknown
        pass

    def get_action_groups(self, *args, **kwargs): # real signature unknown
        pass

    def get_add_tearoffs(self, *args, **kwargs): # real signature unknown
        pass

    def get_toplevels(self, *args, **kwargs): # real signature unknown
        pass

    def get_ui(self, *args, **kwargs): # real signature unknown
        pass

    def get_widget(self, *args, **kwargs): # real signature unknown
        pass

    def insert_action_group(self, *args, **kwargs): # real signature unknown
        pass

    def new_merge_id(self, *args, **kwargs): # real signature unknown
        pass

    def remove_action_group(self, *args, **kwargs): # real signature unknown
        pass

    def remove_ui(self, *args, **kwargs): # real signature unknown
        pass

    def set_add_tearoffs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


