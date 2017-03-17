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


from Container import Container

class Notebook(Container):
    """
    Object GtkNotebook
    
    Signals from GtkNotebook:
      switch-page (gpointer, guint)
      focus-tab (GtkNotebookTab) -> gboolean
      select-page (gboolean) -> gboolean
      change-current-page (gint) -> gboolean
      move-focus-out (GtkDirectionType)
      reorder-tab (GtkDirectionType, gboolean) -> gboolean
      page-reordered (GtkWidget, guint)
      page-removed (GtkWidget, guint)
      page-added (GtkWidget, guint)
      create-window (GtkWidget, gint, gint) -> GtkNotebook
    
    Properties from GtkNotebook:
      tab-pos -> GtkPositionType: Tab Position
        Which side of the notebook holds the tabs
      show-tabs -> gboolean: Show Tabs
        Whether tabs should be shown or not
      show-border -> gboolean: Show Border
        Whether the border should be shown or not
      scrollable -> gboolean: Scrollable
        If TRUE, scroll arrows are added if there are too many tabs to fit
      tab-border -> guint: Tab Border
        Width of the border around the tab labels
      tab-hborder -> guint: Horizontal Tab Border
        Width of the horizontal border of tab labels
      tab-vborder -> guint: Vertical Tab Border
        Width of the vertical border of tab labels
      page -> gint: Page
        The index of the current page
      enable-popup -> gboolean: Enable Popup
        If TRUE, pressing the right mouse button on the notebook pops up a menu that you can use to go to a page
      group-id -> gint: Group ID
        Group ID for tabs drag and drop
      group -> gpointer: Group
        Group for tabs drag and drop
      group-name -> gchararray: Group Name
        Group name for tabs drag and drop
      homogeneous -> gboolean: Homogeneous
        Whether tabs should have homogeneous sizes
    
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
    def append_page(self, *args, **kwargs): # real signature unknown
        pass

    def append_page_menu(self, *args, **kwargs): # real signature unknown
        pass

    def current_page(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_change_current_page(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus_tab(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_page(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_reorder_tab(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_page(cls, *args, **kwargs): # real signature unknown
        pass

    def get_action_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_page(self, *args, **kwargs): # real signature unknown
        pass

    def get_group_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_group_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_menu_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_menu_label_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_nth_page(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_pages(self, *args, **kwargs): # real signature unknown
        pass

    def get_scrollable(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_border(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_detachable(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_hborder(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_label_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_pos(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_vborder(self, *args, **kwargs): # real signature unknown
        pass

    def insert_page(self, *args, **kwargs): # real signature unknown
        pass

    def insert_page_menu(self, *args, **kwargs): # real signature unknown
        pass

    def next_page(self, *args, **kwargs): # real signature unknown
        pass

    def page_num(self, *args, **kwargs): # real signature unknown
        pass

    def popup_disable(self, *args, **kwargs): # real signature unknown
        pass

    def popup_enable(self, *args, **kwargs): # real signature unknown
        pass

    def prepend_page(self, *args, **kwargs): # real signature unknown
        pass

    def prepend_page_menu(self, *args, **kwargs): # real signature unknown
        pass

    def prev_page(self, *args, **kwargs): # real signature unknown
        pass

    def query_tab_label_packing(self, *args, **kwargs): # real signature unknown
        pass

    def remove_page(self, *args, **kwargs): # real signature unknown
        pass

    def reorder_child(self, *args, **kwargs): # real signature unknown
        pass

    def set_action_widget(self, *args, **kwargs): # real signature unknown
        pass

    def set_current_page(self, *args, **kwargs): # real signature unknown
        pass

    def set_group_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_group_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_homogeneous_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def set_menu_label(self, *args, **kwargs): # real signature unknown
        pass

    def set_menu_label_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_page(self, *args, **kwargs): # real signature unknown
        pass

    def set_scrollable(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_border(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_border(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_detachable(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_hborder(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_label(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_label_packing(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_label_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_pos(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_vborder(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    tab_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


