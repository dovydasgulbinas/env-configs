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

class Action(__gobject__gobject.GObject, Buildable):
    """
    Object GtkAction
    
    Signals from GtkAction:
      activate ()
    
    Properties from GtkAction:
      name -> gchararray: Name
        A unique name for the action.
      label -> gchararray: Label
        The label used for menu items and buttons that activate this action.
      short-label -> gchararray: Short label
        A shorter label that may be used on toolbar buttons.
      tooltip -> gchararray: Tooltip
        A tooltip for this action.
      stock-id -> gchararray: Stock Icon
        The stock icon displayed in widgets representing this action.
      icon-name -> gchararray: Icon Name
        The name of the icon from the icon theme
      gicon -> GIcon: GIcon
        The GIcon being displayed
      visible-horizontal -> gboolean: Visible when horizontal
        Whether the toolbar item is visible when the toolbar is in a horizontal orientation.
      visible-vertical -> gboolean: Visible when vertical
        Whether the toolbar item is visible when the toolbar is in a vertical orientation.
      visible-overflown -> gboolean: Visible when overflown
        When TRUE, toolitem proxies for this action are represented in the toolbar overflow menu.
      is-important -> gboolean: Is important
        Whether the action is considered important. When TRUE, toolitem proxies for this action show text in GTK_TOOLBAR_BOTH_HORIZ mode.
      hide-if-empty -> gboolean: Hide if empty
        When TRUE, empty menu proxies for this action are hidden.
      sensitive -> gboolean: Sensitive
        Whether the action is enabled.
      visible -> gboolean: Visible
        Whether the action is visible.
      action-group -> GtkActionGroup: Action Group
        The GtkActionGroup this GtkAction is associated with, or NULL (for internal use).
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown
    
    Signals from GObject:
      notify (GParam)
    """
    def activate(self, *args, **kwargs): # real signature unknown
        pass

    def block_activate(self, *args, **kwargs): # real signature unknown
        pass

    def block_activate_from(self, *args, **kwargs): # real signature unknown
        pass

    def connect_accelerator(self, *args, **kwargs): # real signature unknown
        pass

    def connect_proxy(self, *args, **kwargs): # real signature unknown
        pass

    def create_icon(self, *args, **kwargs): # real signature unknown
        pass

    def create_menu(self, *args, **kwargs): # real signature unknown
        pass

    def create_menu_item(self, *args, **kwargs): # real signature unknown
        pass

    def create_tool_item(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_accelerator(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_proxy(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_activate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_connect_proxy(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_create_menu_item(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_create_tool_item(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_disconnect_proxy(cls, *args, **kwargs): # real signature unknown
        pass

    def get_accel_closure(self, *args, **kwargs): # real signature unknown
        pass

    def get_accel_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_always_show_image(self, *args, **kwargs): # real signature unknown
        pass

    def get_gicon(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_important(self, *args, **kwargs): # real signature unknown
        pass

    def get_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxies(self, *args, **kwargs): # real signature unknown
        pass

    def get_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def get_short_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_stock_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_horizontal(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_vertical(self, *args, **kwargs): # real signature unknown
        pass

    def is_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def is_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_accel_group(self, *args, **kwargs): # real signature unknown
        pass

    def set_accel_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_always_show_image(self, *args, **kwargs): # real signature unknown
        pass

    def set_gicon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_is_important(self, *args, **kwargs): # real signature unknown
        pass

    def set_label(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def set_menu_item_type(cls, *args, **kwargs): # real signature unknown
        pass

    def set_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def set_short_label(self, *args, **kwargs): # real signature unknown
        pass

    def set_stock_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def set_tool_item_type(cls, *args, **kwargs): # real signature unknown
        pass

    def set_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible_horizontal(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible_vertical(self, *args, **kwargs): # real signature unknown
        pass

    def unblock_activate(self, *args, **kwargs): # real signature unknown
        pass

    def unblock_activate_from(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


