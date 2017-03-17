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

class TreeView(Container):
    """
    Object GtkTreeView
    
    Signals from GtkTreeView:
      move-cursor (GtkMovementStep, gint) -> gboolean
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      select-all () -> gboolean
      unselect-all () -> gboolean
      row-activated (GtkTreePath, GtkTreeViewColumn)
      test-expand-row (GtkTreeIter, GtkTreePath) -> gboolean
      test-collapse-row (GtkTreeIter, GtkTreePath) -> gboolean
      row-expanded (GtkTreeIter, GtkTreePath)
      row-collapsed (GtkTreeIter, GtkTreePath)
      columns-changed ()
      cursor-changed ()
      select-cursor-row (gboolean) -> gboolean
      toggle-cursor-row () -> gboolean
      expand-collapse-cursor-row (gboolean, gboolean, gboolean) -> gboolean
      select-cursor-parent () -> gboolean
      start-interactive-search () -> gboolean
    
    Properties from GtkTreeView:
      model -> GtkTreeModel: TreeView Model
        The model for the tree view
      hadjustment -> GtkAdjustment: Horizontal Adjustment
        Horizontal Adjustment for the widget
      vadjustment -> GtkAdjustment: Vertical Adjustment
        Vertical Adjustment for the widget
      headers-visible -> gboolean: Headers Visible
        Show the column header buttons
      headers-clickable -> gboolean: Headers Clickable
        Column headers respond to click events
      expander-column -> GtkTreeViewColumn: Expander Column
        Set the column for the expander column
      reorderable -> gboolean: Reorderable
        View is reorderable
      rules-hint -> gboolean: Rules Hint
        Set a hint to the theme engine to draw rows in alternating colors
      enable-search -> gboolean: Enable Search
        View allows user to search through columns interactively
      search-column -> gint: Search Column
        Model column to search through during interactive search
      fixed-height-mode -> gboolean: Fixed Height Mode
        Speeds up GtkTreeView by assuming that all rows have the same height
      ubuntu-almost-fixed-height-mode -> gboolean: Private Ubuntu extension
        Private Ubuntu extension
      hover-selection -> gboolean: Hover Selection
        Whether the selection should follow the pointer
      hover-expand -> gboolean: Hover Expand
        Whether rows should be expanded/collapsed when the pointer moves over them
      show-expanders -> gboolean: Show Expanders
        View has expanders
      level-indentation -> gint: Level Indentation
        Extra indentation for each level
      rubber-banding -> gboolean: Rubber Banding
        Whether to enable selection of multiple items by dragging the mouse pointer
      enable-grid-lines -> GtkTreeViewGridLines: Enable Grid Lines
        Whether grid lines should be drawn in the tree view
      enable-tree-lines -> gboolean: Enable Tree Lines
        Whether tree lines should be drawn in the tree view
      tooltip-column -> gint: Tooltip Column
        The column in the model containing the tooltip texts for the rows
    
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
    def append_column(self, *args, **kwargs): # real signature unknown
        pass

    def collapse_all(self, *args, **kwargs): # real signature unknown
        pass

    def collapse_row(self, *args, **kwargs): # real signature unknown
        pass

    def columns_autosize(self, *args, **kwargs): # real signature unknown
        pass

    def convert_bin_window_to_tree_coords(self, *args, **kwargs): # real signature unknown
        pass

    def convert_bin_window_to_widget_coords(self, *args, **kwargs): # real signature unknown
        pass

    def convert_tree_to_bin_window_coords(self, *args, **kwargs): # real signature unknown
        pass

    def convert_tree_to_widget_coords(self, *args, **kwargs): # real signature unknown
        pass

    def convert_widget_to_bin_window_coords(self, *args, **kwargs): # real signature unknown
        pass

    def convert_widget_to_tree_coords(self, *args, **kwargs): # real signature unknown
        pass

    def create_row_drag_icon(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_columns_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_cursor_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_expand_collapse_cursor_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_move_cursor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_row_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_row_collapsed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_row_expanded(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_cursor_parent(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_cursor_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_scroll_adjustments(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_start_interactive_search(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_test_collapse_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_test_expand_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_toggle_cursor_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unselect_all(cls, *args, **kwargs): # real signature unknown
        pass

    def enable_model_drag_dest(self, *args, **kwargs): # real signature unknown
        pass

    def enable_model_drag_source(self, *args, **kwargs): # real signature unknown
        pass

    def expand_all(self, *args, **kwargs): # real signature unknown
        pass

    def expand_row(self, *args, **kwargs): # real signature unknown
        pass

    def expand_to_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_background_area(self, *args, **kwargs): # real signature unknown
        pass

    def get_bin_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_cell_area(self, *args, **kwargs): # real signature unknown
        pass

    def get_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_columns(self, *args, **kwargs): # real signature unknown
        pass

    def get_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def get_dest_row_at_pos(self, *args, **kwargs): # real signature unknown
        pass

    def get_drag_dest_row(self, *args, **kwargs): # real signature unknown
        pass

    def get_enable_search(self, *args, **kwargs): # real signature unknown
        pass

    def get_enable_tree_lines(self, *args, **kwargs): # real signature unknown
        pass

    def get_expander_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_fixed_height_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_grid_lines(self, *args, **kwargs): # real signature unknown
        pass

    def get_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_headers_clickable(self, *args, **kwargs): # real signature unknown
        pass

    def get_headers_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_hover_expand(self, *args, **kwargs): # real signature unknown
        pass

    def get_hover_selection(self, *args, **kwargs): # real signature unknown
        pass

    def get_level_indentation(self, *args, **kwargs): # real signature unknown
        pass

    def get_model(self, *args, **kwargs): # real signature unknown
        pass

    def get_path_at_pos(self, *args, **kwargs): # real signature unknown
        pass

    def get_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def get_rubber_banding(self, *args, **kwargs): # real signature unknown
        pass

    def get_rules_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_search_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_search_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_expanders(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_range(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_rect(self, *args, **kwargs): # real signature unknown
        pass

    def insert_column(self, *args, **kwargs): # real signature unknown
        pass

    def insert_column_with_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def insert_column_with_data_func(self, *args, **kwargs): # real signature unknown
        pass

    def is_rubber_banding_active(self, *args, **kwargs): # real signature unknown
        pass

    def map_expanded_rows(self, *args, **kwargs): # real signature unknown
        pass

    def move_column_after(self, *args, **kwargs): # real signature unknown
        pass

    def remove_column(self, *args, **kwargs): # real signature unknown
        pass

    def row_activated(self, *args, **kwargs): # real signature unknown
        pass

    def row_expanded(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_to_cell(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_to_point(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_drag_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def set_cursor_on_cell(self, *args, **kwargs): # real signature unknown
        pass

    def set_drag_dest_row(self, *args, **kwargs): # real signature unknown
        pass

    def set_enable_search(self, *args, **kwargs): # real signature unknown
        pass

    def set_enable_tree_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_expander_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_fixed_height_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_grid_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def set_headers_clickable(self, *args, **kwargs): # real signature unknown
        pass

    def set_headers_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_hover_expand(self, *args, **kwargs): # real signature unknown
        pass

    def set_hover_selection(self, *args, **kwargs): # real signature unknown
        pass

    def set_level_indentation(self, *args, **kwargs): # real signature unknown
        pass

    def set_model(self, *args, **kwargs): # real signature unknown
        pass

    def set_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_separator_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_rubber_banding(self, *args, **kwargs): # real signature unknown
        pass

    def set_rules_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_entry(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_equal_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_position_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_expanders(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_cell(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_row(self, *args, **kwargs): # real signature unknown
        pass

    def set_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def tree_to_widget_coords(self, *args, **kwargs): # real signature unknown
        pass

    def unset_rows_drag_dest(self, *args, **kwargs): # real signature unknown
        pass

    def unset_rows_drag_source(self, *args, **kwargs): # real signature unknown
        pass

    def widget_to_tree_coords(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


