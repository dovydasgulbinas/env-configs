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

from CellEditable import CellEditable

from CellLayout import CellLayout

class ComboBox(Bin, CellEditable, CellLayout):
    """
    Object GtkComboBox
    
    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
    
    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      focus-on-click -> gboolean: Focus on click
        Whether the combo box grabs focus when it is clicked with the mouse
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
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
    def append_text(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_active_text(cls, *args, **kwargs): # real signature unknown
        pass

    def get_active(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_add_tearoffs(self, *args, **kwargs): # real signature unknown
        pass

    def get_button_sensitivity(self, *args, **kwargs): # real signature unknown
        pass

    def get_column_span_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_entry_text_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_on_click(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_model(self, *args, **kwargs): # real signature unknown
        pass

    def get_popup_accessible(self, *args, **kwargs): # real signature unknown
        pass

    def get_row_span_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_wrap_width(self, *args, **kwargs): # real signature unknown
        pass

    def insert_text(self, *args, **kwargs): # real signature unknown
        pass

    def popdown(self, *args, **kwargs): # real signature unknown
        pass

    def popup(self, *args, **kwargs): # real signature unknown
        pass

    def prepend_text(self, *args, **kwargs): # real signature unknown
        pass

    def remove_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_active(self, *args, **kwargs): # real signature unknown
        pass

    def set_active_iter(self, *args, **kwargs): # real signature unknown
        pass

    def set_add_tearoffs(self, *args, **kwargs): # real signature unknown
        pass

    def set_button_sensitivity(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_span_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_entry_text_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_on_click(self, *args, **kwargs): # real signature unknown
        pass

    def set_model(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_separator_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_span_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, *args, **kwargs): # real signature unknown
        pass

    def set_wrap_width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


