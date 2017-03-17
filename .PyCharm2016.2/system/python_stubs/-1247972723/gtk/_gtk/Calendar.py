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


from Widget import Widget

class Calendar(Widget):
    """
    Object GtkCalendar
    
    Signals from GtkCalendar:
      month-changed ()
      day-selected ()
      day-selected-double-click ()
      prev-month ()
      next-month ()
      prev-year ()
      next-year ()
    
    Properties from GtkCalendar:
      year -> gint: Year
        The selected year
      month -> gint: Month
        The selected month (as a number between 0 and 11)
      day -> gint: Day
        The selected day (as a number between 1 and 31, or 0 to unselect the currently selected day)
      show-heading -> gboolean: Show Heading
        If TRUE, a heading is displayed
      show-day-names -> gboolean: Show Day Names
        If TRUE, day names are displayed
      no-month-change -> gboolean: No Month Change
        If TRUE, the selected month cannot be changed
      show-week-numbers -> gboolean: Show Week Numbers
        If TRUE, week numbers are displayed
      show-details -> gboolean: Show Details
        If TRUE, details are shown
      detail-width-chars -> gint: Details Width
        Details width in characters
      detail-height-rows -> gint: Details Height
        Details height in rows
    
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
    def clear_marks(self, *args, **kwargs): # real signature unknown
        pass

    def display_options(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_day_selected(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_day_selected_double_click(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_month_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_next_month(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_next_year(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_prev_month(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_prev_year(cls, *args, **kwargs): # real signature unknown
        pass

    def freeze(self, *args, **kwargs): # real signature unknown
        pass

    def get_date(self, *args, **kwargs): # real signature unknown
        pass

    def get_detail_height_rows(self, *args, **kwargs): # real signature unknown
        pass

    def get_detail_width_chars(self, *args, **kwargs): # real signature unknown
        pass

    def get_display_options(self, *args, **kwargs): # real signature unknown
        pass

    def mark_day(self, *args, **kwargs): # real signature unknown
        pass

    def select_day(self, *args, **kwargs): # real signature unknown
        pass

    def select_month(self, *args, **kwargs): # real signature unknown
        pass

    def set_detail_height_rows(self, *args, **kwargs): # real signature unknown
        pass

    def set_detail_width_chars(self, *args, **kwargs): # real signature unknown
        pass

    def set_display_options(self, *args, **kwargs): # real signature unknown
        pass

    def thaw(self, *args, **kwargs): # real signature unknown
        pass

    def unmark_day(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


