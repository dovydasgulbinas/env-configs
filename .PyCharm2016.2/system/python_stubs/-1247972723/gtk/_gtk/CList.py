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

class CList(Container):
    """
    Object GtkCList
    
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
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def columns_autosize(self, *args, **kwargs): # real signature unknown
        pass

    def column_titles_active(self, *args, **kwargs): # real signature unknown
        pass

    def column_titles_hide(self, *args, **kwargs): # real signature unknown
        pass

    def column_titles_passive(self, *args, **kwargs): # real signature unknown
        pass

    def column_titles_show(self, *args, **kwargs): # real signature unknown
        pass

    def column_title_active(self, *args, **kwargs): # real signature unknown
        pass

    def column_title_passive(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_abort_column_resize(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_clear(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_click_column(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_end_selection(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_extend_selection(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_fake_unselect_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_refresh(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_remove_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_resize_column(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_resync_selection(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_row_move(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_scroll_horizontal(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_scroll_vertical(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_select_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_scroll_adjustments(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_sort_list(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_start_selection(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_toggle_add_mode(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_toggle_focus_row(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_undo_selection(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unselect_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unselect_row(cls, *args, **kwargs): # real signature unknown
        pass

    def find_row_from_data(self, *args, **kwargs): # real signature unknown
        pass

    def freeze(self, *args, **kwargs): # real signature unknown
        pass

    def get_cell_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_cell_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_column_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_column_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixtext(self, *args, **kwargs): # real signature unknown
        pass

    def get_row_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_row_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_selectable(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_info(self, *args, **kwargs): # real signature unknown
        pass

    def get_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def moveto(self, *args, **kwargs): # real signature unknown
        pass

    def optimal_column_width(self, *args, **kwargs): # real signature unknown
        pass

    def prepend(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def row_is_visible(self, *args, **kwargs): # real signature unknown
        pass

    def row_move(self, *args, **kwargs): # real signature unknown
        pass

    def select_all(self, *args, **kwargs): # real signature unknown
        pass

    def select_row(self, *args, **kwargs): # real signature unknown
        pass

    def set_auto_sort(self, *args, **kwargs): # real signature unknown
        pass

    def set_background(self, *args, **kwargs): # real signature unknown
        pass

    def set_button_actions(self, *args, **kwargs): # real signature unknown
        pass

    def set_cell_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_auto_resize(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_justification(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_max_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_min_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_resizeable(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_title(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_visibility(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_widget(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_foreground(self, *args, **kwargs): # real signature unknown
        pass

    def set_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixtext(self, *args, **kwargs): # real signature unknown
        pass

    def set_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_data(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_height(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_selectable(self, *args, **kwargs): # real signature unknown
        pass

    def set_selection_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_shadow_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_shift(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_use_drag_icons(self, *args, **kwargs): # real signature unknown
        pass

    def set_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        pass

    def swap_rows(self, *args, **kwargs): # real signature unknown
        pass

    def thaw(self, *args, **kwargs): # real signature unknown
        pass

    def undo_selection(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_all(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_row(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


