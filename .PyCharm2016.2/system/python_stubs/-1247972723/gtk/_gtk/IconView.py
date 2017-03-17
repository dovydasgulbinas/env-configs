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

from CellLayout import CellLayout

class IconView(Container, CellLayout):
    """
    Object GtkIconView
    
    Signals from GtkIconView:
      move-cursor (GtkMovementStep, gint) -> gboolean
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      select-all ()
      unselect-all ()
      selection-changed ()
      item-activated (GtkTreePath)
      select-cursor-item ()
      toggle-cursor-item ()
      activate-cursor-item () -> gboolean
    
    Properties from GtkIconView:
      pixbuf-column -> gint: Pixbuf column
        Model column used to retrieve the icon pixbuf from
      text-column -> gint: Text column
        Model column used to retrieve the text from
      markup-column -> gint: Markup column
        Model column used to retrieve the text if using Pango markup
      selection-mode -> GtkSelectionMode: Selection mode
        The selection mode
      orientation -> GtkOrientation: Orientation
        How the text and icon of each item are positioned relative to each other
      item-orientation -> GtkOrientation: Item Orientation
        How the text and icon of each item are positioned relative to each other
      model -> GtkTreeModel: Icon View Model
        The model for the icon view
      columns -> gint: Number of columns
        Number of columns to display
      item-width -> gint: Width for each item
        The width used for each item
      spacing -> gint: Spacing
        Space which is inserted between cells of an item
      row-spacing -> gint: Row Spacing
        Space which is inserted between grid rows
      column-spacing -> gint: Column Spacing
        Space which is inserted between grid columns
      margin -> gint: Margin
        Space which is inserted at the edges of the icon view
      reorderable -> gboolean: Reorderable
        View is reorderable
      tooltip-column -> gint: Tooltip Column
        The column in the model containing the tooltip texts for the items
      item-padding -> gint: Item Padding
        Padding around icon view items
    
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
    def convert_widget_to_bin_window_coords(self, *args, **kwargs): # real signature unknown
        pass

    def create_drag_icon(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_activate_cursor_item(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_item_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_move_cursor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_selection_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_cursor_item(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_scroll_adjustments(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_toggle_cursor_item(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unselect_all(cls, *args, **kwargs): # real signature unknown
        pass

    def enable_model_drag_dest(self, *args, **kwargs): # real signature unknown
        pass

    def enable_model_drag_source(self, *args, **kwargs): # real signature unknown
        pass

    def get_columns(self, *args, **kwargs): # real signature unknown
        pass

    def get_column_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def get_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def get_dest_item_at_pos(self, *args, **kwargs): # real signature unknown
        pass

    def get_drag_dest_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_at_pos(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_padding(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_row(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_markup_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_model(self, *args, **kwargs): # real signature unknown
        pass

    def get_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def get_path_at_pos(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixbuf_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def get_row_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def get_selected_items(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def get_text_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_range(self, *args, **kwargs): # real signature unknown
        pass

    def item_activated(self, *args, **kwargs): # real signature unknown
        pass

    def path_is_selected(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_to_path(self, *args, **kwargs): # real signature unknown
        pass

    def selected_foreach(self, *args, **kwargs): # real signature unknown
        pass

    def select_all(self, *args, **kwargs): # real signature unknown
        pass

    def select_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_columns(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def set_drag_dest_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_item_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def set_item_padding(self, *args, **kwargs): # real signature unknown
        pass

    def set_item_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_markup_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_model(self, *args, **kwargs): # real signature unknown
        pass

    def set_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixbuf_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_selection_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_text_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_cell(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_item(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_all(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_path(self, *args, **kwargs): # real signature unknown
        pass

    def unset_model_drag_dest(self, *args, **kwargs): # real signature unknown
        pass

    def unset_model_drag_source(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


