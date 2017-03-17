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


from Action import Action

from RecentChooser import RecentChooser

class RecentAction(Action, RecentChooser):
    """
    Object GtkRecentAction
    
    Properties from GtkRecentAction:
      show-numbers -> gboolean: Show Numbers
        Whether the items should be displayed with a number
    
    Signals from GtkRecentChooser:
      selection-changed ()
      item-activated ()
    
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
    def get_show_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


