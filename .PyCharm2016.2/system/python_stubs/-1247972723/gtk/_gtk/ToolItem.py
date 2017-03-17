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


from Bin import Bin

from Activatable import Activatable

class ToolItem(Bin, Activatable):
    """
    Object GtkToolItem
    
    Signals from GtkToolItem:
      create-menu-proxy () -> gboolean
      toolbar-reconfigured ()
      set-tooltip (GtkTooltips, gchararray, gchararray) -> gboolean
    
    Properties from GtkToolItem:
      visible-horizontal -> gboolean: Visible when horizontal
        Whether the toolbar item is visible when the toolbar is in a horizontal orientation.
      visible-vertical -> gboolean: Visible when vertical
        Whether the toolbar item is visible when the toolbar is in a vertical orientation.
      is-important -> gboolean: Is important
        Whether the toolbar item is considered important. When TRUE, toolbar buttons show text in GTK_TOOLBAR_BOTH_HORIZ mode
    
    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)
    
    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_create_menu_proxy(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_tooltip(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_toolbar_reconfigured(cls, *args, **kwargs): # real signature unknown
        pass

    def get_ellipsize_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_expand(self, *args, **kwargs): # real signature unknown
        pass

    def get_homogeneous(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_important(self, *args, **kwargs): # real signature unknown
        pass

    def get_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxy_menu_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_relief_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_text_alignment(self, *args, **kwargs): # real signature unknown
        pass

    def get_text_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def get_text_size_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_toolbar_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_use_drag_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_horizontal(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_vertical(self, *args, **kwargs): # real signature unknown
        pass

    def rebuild_menu(self, *args, **kwargs): # real signature unknown
        pass

    def retrieve_proxy_menu_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_expand(self, *args, **kwargs): # real signature unknown
        pass

    def set_homogeneous(self, *args, **kwargs): # real signature unknown
        pass

    def set_is_important(self, *args, **kwargs): # real signature unknown
        pass

    def set_proxy_menu_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_markup(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_use_drag_window(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible_horizontal(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible_vertical(self, *args, **kwargs): # real signature unknown
        pass

    def toolbar_reconfigured(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


