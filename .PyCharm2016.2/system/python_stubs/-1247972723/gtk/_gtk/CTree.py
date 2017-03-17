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


from CList import CList

class CTree(CList):
    """
    Object GtkCTree
    
    Signals from GtkCTree:
      tree-select-row (GtkCTreeNode, gint)
      tree-unselect-row (GtkCTreeNode, gint)
      tree-expand (GtkCTreeNode)
      tree-collapse (GtkCTreeNode)
      tree-move (GtkCTreeNode, GtkCTreeNode, GtkCTreeNode)
      change-focus-row-expansion (GtkCTreeExpansionType)
    
    Properties from GtkCTree:
      n-columns -> guint: n-columns
      tree-column -> guint: tree-column
      indent -> guint: indent
      spacing -> guint: spacing
      show-stub -> gboolean: show-stub
      line-style -> GtkCTreeLineStyle: line-style
      expander-style -> GtkCTreeExpanderStyle: expander-style
    
    Signals from GtkCList:
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      select-row (gint, gint, GdkEvent)
      unselect-row (gint, gint, GdkEvent)
      row-move (gint, gint)
      click-column (gint)
      resize-column (gint, gint)
      toggle-focus-row ()
      select-all ()
      unselect-all ()
      undo-selection ()
      start-selection ()
      end-selection ()
      toggle-add-mode ()
      extend-selection (GtkScrollType, gfloat, gboolean)
      scroll-vertical (GtkScrollType, gfloat)
      scroll-horizontal (GtkScrollType, gfloat)
      abort-column-resize ()
    
    Properties from GtkCList:
      n-columns -> guint: n-columns
      shadow-type -> GtkShadowType: shadow-type
      selection-mode -> GtkSelectionMode: selection-mode
      row-height -> guint: row-height
      titles-active -> gboolean: titles-active
      reorderable -> gboolean: reorderable
      use-drag-icons -> gboolean: use-drag-icons
      sort-type -> GtkSortType: sort-type
    
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
    def base_nodes(self, *args, **kwargs): # real signature unknown
        pass

    def collapse(self, *args, **kwargs): # real signature unknown
        pass

    def collapse_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def collapse_to_depth(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_change_focus_row_expansion(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_tree_collapse(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_tree_expand(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_tree_move(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_tree_select_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_tree_unselect_row(cls, *args, **kwargs): # real signature unknown
        pass

    def expand(self, *args, **kwargs): # real signature unknown
        pass

    def expand_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def expand_to_depth(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def find_all_by_row_data(self, *args, **kwargs): # real signature unknown
        pass

    def find_by_row_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_node_info(self, *args, **kwargs): # real signature unknown
        pass

    def insert_node(self, *args, **kwargs): # real signature unknown
        pass

    def is_ancestor(self, *args, **kwargs): # real signature unknown
        pass

    def is_hot_spot(self, *args, **kwargs): # real signature unknown
        pass

    def is_viewable(self, *args, **kwargs): # real signature unknown
        pass

    def last(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_cell_style(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_cell_type(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_pixtext(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_row_data(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_row_style(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_selectable(self, *args, **kwargs): # real signature unknown
        pass

    def node_get_text(self, *args, **kwargs): # real signature unknown
        pass

    def node_is_visible(self, *args, **kwargs): # real signature unknown
        pass

    def node_moveto(self, *args, **kwargs): # real signature unknown
        pass

    def node_nth(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_background(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_cell_style(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_foreground(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_pixtext(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_row_data(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_row_style(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_selectable(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_shift(self, *args, **kwargs): # real signature unknown
        pass

    def node_set_text(self, *args, **kwargs): # real signature unknown
        pass

    def real_select_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def remove_node(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def select_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def set_expander_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_indent(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_node_info(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_stub(self, *args, **kwargs): # real signature unknown
        pass

    def set_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def sort_node(self, *args, **kwargs): # real signature unknown
        pass

    def sort_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def toggle_expansion(self, *args, **kwargs): # real signature unknown
        pass

    def toggle_expansion_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def unselect(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_recursive(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


