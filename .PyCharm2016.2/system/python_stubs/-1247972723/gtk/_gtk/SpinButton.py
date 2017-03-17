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


from Entry import Entry

from Editable import Editable

from CellEditable import CellEditable

class SpinButton(Entry, Editable, CellEditable):
    """
    Object GtkSpinButton
    
    Signals from GtkSpinButton:
      value-changed ()
      change-value (GtkScrollType)
      input (gpointer) -> gint
      output () -> gboolean
      wrapped ()
    
    Properties from GtkSpinButton:
      adjustment -> GtkAdjustment: Adjustment
        The adjustment that holds the value of the spinbutton
      climb-rate -> gdouble: Climb Rate
        The acceleration rate when you hold down a button
      digits -> guint: Digits
        The number of decimal places to display
      snap-to-ticks -> gboolean: Snap to Ticks
        Whether erroneous values are automatically changed to a spin button's nearest step increment
      numeric -> gboolean: Numeric
        Whether non-numeric characters should be ignored
      wrap -> gboolean: Wrap
        Whether a spin button should wrap upon reaching its limits
      update-policy -> GtkSpinButtonUpdatePolicy: Update Policy
        Whether the spin button should update always, or only when the value is legal
      value -> gdouble: Value
        Reads the current value, or sets a new value
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkEntry:
      move-cursor (GtkMovementStep, gint, gboolean)
      copy-clipboard ()
      populate-popup (GtkMenu)
      activate ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      icon-press (GtkEntryIconPosition, GdkEvent)
      icon-release (GtkEntryIconPosition, GdkEvent)
      preedit-changed (gchararray)
    
    Properties from GtkEntry:
      buffer -> GtkEntryBuffer: Text Buffer
        Text buffer object which actually stores entry text
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      editable -> gboolean: Editable
        Whether the entry contents can be edited
      max-length -> gint: Maximum length
        Maximum number of characters for this entry. Zero if no maximum
      visibility -> gboolean: Visibility
        FALSE displays the "invisible char" instead of the actual text (password mode)
      has-frame -> gboolean: Has Frame
        FALSE removes outside bevel from entry
      inner-border -> GtkBorder: Inner Border
        Border between text and frame. Overrides the inner-border style property
      invisible-char -> guint: Invisible character
        The character to use when masking entry contents (in "password mode")
      activates-default -> gboolean: Activates default
        Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed
      width-chars -> gint: Width in chars
        Number of characters to leave space for in the entry
      scroll-offset -> gint: Scroll offset
        Number of pixels of the entry scrolled off the screen to the left
      text -> gchararray: Text
        The contents of the entry
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      truncate-multiline -> gboolean: Truncate multiline
        Whether to truncate multiline pastes to one line.
      shadow-type -> GtkShadowType: Shadow type
        Which kind of shadow to draw around the entry when has-frame is set
      overwrite-mode -> gboolean: Overwrite mode
        Whether new text overwrites existing text
      text-length -> guint: Text length
        Length of the text currently in the entry
      invisible-char-set -> gboolean: Invisible char set
        Whether the invisible char has been set
      caps-lock-warning -> gboolean: Caps Lock warning
        Whether password entries will show a warning when Caps Lock is on
      progress-fraction -> gdouble: Progress Fraction
        The current fraction of the task that's been completed
      progress-pulse-step -> gdouble: Progress Pulse Step
        The fraction of total entry width to move the progress bouncing block for each call to gtk_entry_progress_pulse()
      primary-icon-pixbuf -> GdkPixbuf: Primary pixbuf
        Primary pixbuf for the entry
      secondary-icon-pixbuf -> GdkPixbuf: Secondary pixbuf
        Secondary pixbuf for the entry
      primary-icon-stock -> gchararray: Primary stock ID
        Stock ID for primary icon
      secondary-icon-stock -> gchararray: Secondary stock ID
        Stock ID for secondary icon
      primary-icon-name -> gchararray: Primary icon name
        Icon name for primary icon
      secondary-icon-name -> gchararray: Secondary icon name
        Icon name for secondary icon
      primary-icon-gicon -> GIcon: Primary GIcon
        GIcon for primary icon
      secondary-icon-gicon -> GIcon: Secondary GIcon
        GIcon for secondary icon
      primary-icon-storage-type -> GtkImageType: Primary storage type
        The representation being used for primary icon
      secondary-icon-storage-type -> GtkImageType: Secondary storage type
        The representation being used for secondary icon
      primary-icon-activatable -> gboolean: Primary icon activatable
        Whether the primary icon is activatable
      secondary-icon-activatable -> gboolean: Secondary icon activatable
        Whether the secondary icon is activatable
      primary-icon-sensitive -> gboolean: Primary icon sensitive
        Whether the primary icon is sensitive
      secondary-icon-sensitive -> gboolean: Secondary icon sensitive
        Whether the secondary icon is sensitive
      primary-icon-tooltip-text -> gchararray: Primary icon tooltip text
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-text -> gchararray: Secondary icon tooltip text
        The contents of the tooltip on the secondary icon
      primary-icon-tooltip-markup -> gchararray: Primary icon tooltip markup
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-markup -> gchararray: Secondary icon tooltip markup
        The contents of the tooltip on the secondary icon
      im-module -> gchararray: IM module
        Which IM module should be used
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
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
    def configure(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_change_value(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_output(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_value_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_wrapped(cls, *args, **kwargs): # real signature unknown
        pass

    def get_adjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_digits(self, *args, **kwargs): # real signature unknown
        pass

    def get_increments(self, *args, **kwargs): # real signature unknown
        pass

    def get_numeric(self, *args, **kwargs): # real signature unknown
        pass

    def get_range(self, *args, **kwargs): # real signature unknown
        pass

    def get_snap_to_ticks(self, *args, **kwargs): # real signature unknown
        pass

    def get_update_policy(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def get_value_as_int(self, *args, **kwargs): # real signature unknown
        pass

    def get_wrap(self, *args, **kwargs): # real signature unknown
        pass

    def set_adjustment(self, *args, **kwargs): # real signature unknown
        pass

    def set_digits(self, *args, **kwargs): # real signature unknown
        pass

    def set_increments(self, *args, **kwargs): # real signature unknown
        pass

    def set_numeric(self, *args, **kwargs): # real signature unknown
        pass

    def set_range(self, *args, **kwargs): # real signature unknown
        pass

    def set_snap_to_ticks(self, *args, **kwargs): # real signature unknown
        pass

    def set_update_policy(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def set_wrap(self, *args, **kwargs): # real signature unknown
        pass

    def spin(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


