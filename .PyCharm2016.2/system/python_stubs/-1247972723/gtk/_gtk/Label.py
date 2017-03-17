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


from Misc import Misc

class Label(Misc):
    """
    Object GtkLabel
    
    Signals from GtkLabel:
      activate-link (gchararray) -> gboolean
      move-cursor (GtkMovementStep, gint, gboolean)
      copy-clipboard ()
      populate-popup (GtkMenu)
      activate-current-link ()
    
    Properties from GtkLabel:
      label -> gchararray: Label
        The text of the label
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the label
      use-markup -> gboolean: Use markup
        The text of the label includes XML markup. See pango_parse_markup()
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      justify -> GtkJustification: Justification
        The alignment of the lines in the text of the label relative to each other. This does NOT affect the alignment of the label within its allocation. See GtkMisc::xalign for that
      pattern -> gchararray: Pattern
        A string with _ characters in positions correspond to characters in the text to underline
      wrap -> gboolean: Line wrap
        If set, wrap lines if the text becomes too wide
      wrap-mode -> PangoWrapMode: Line wrap mode
        If wrap is set, controls how linewrapping is done
      selectable -> gboolean: Selectable
        Whether the label text can be selected with the mouse
      mnemonic-keyval -> guint: Mnemonic key
        The mnemonic accelerator key for this label
      mnemonic-widget -> GtkWidget: Mnemonic widget
        The widget to be activated when the label's mnemonic key is pressed
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      ellipsize -> PangoEllipsizeMode: Ellipsize
        The preferred place to ellipsize the string, if the label does not have enough room to display the entire string
      width-chars -> gint: Width In Characters
        The desired width of the label, in characters
      single-line-mode -> gboolean: Single Line Mode
        Whether the label is in single line mode
      angle -> gdouble: Angle
        Angle at which the label is rotated
      max-width-chars -> gint: Maximum Width In Characters
        The desired maximum width of the label, in characters
      track-visited-links -> gboolean: Track visited links
        Whether visited links should be tracked
    
    Properties from GtkMisc:
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      yalign -> gfloat: Y align
        The vertical alignment, from 0 (top) to 1 (bottom)
      xpad -> gint: X pad
        The amount of space to add on the left and right of the widget, in pixels
      ypad -> gint: Y pad
        The amount of space to add on the top and bottom of the widget, in pixels
    
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
    def do_copy_clipboard(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_move_cursor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_populate_popup(cls, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def get_angle(self, *args, **kwargs): # real signature unknown
        pass

    def get_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_ellipsize(self, *args, **kwargs): # real signature unknown
        pass

    def get_justify(self, *args, **kwargs): # real signature unknown
        pass

    def get_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_layout(self, *args, **kwargs): # real signature unknown
        pass

    def get_layout_offsets(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_wrap(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_max_width_chars(self, *args, **kwargs): # real signature unknown
        pass

    def get_mnemonic_keyval(self, *args, **kwargs): # real signature unknown
        pass

    def get_mnemonic_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_selectable(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_bounds(self, *args, **kwargs): # real signature unknown
        pass

    def get_single_line_mode(self, *args, **kwargs): # real signature unknown
        pass

    def get_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_track_visited_links(self, *args, **kwargs): # real signature unknown
        pass

    def get_use_markup(self, *args, **kwargs): # real signature unknown
        pass

    def get_use_underline(self, *args, **kwargs): # real signature unknown
        pass

    def get_width_chars(self, *args, **kwargs): # real signature unknown
        pass

    def parse_uline(self, *args, **kwargs): # real signature unknown
        pass

    def select_region(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def set_angle(self, *args, **kwargs): # real signature unknown
        pass

    def set_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def set_ellipsize(self, *args, **kwargs): # real signature unknown
        pass

    def set_justify(self, *args, **kwargs): # real signature unknown
        pass

    def set_label(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_wrap(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_markup(self, *args, **kwargs): # real signature unknown
        pass

    def set_markup_with_mnemonic(self, *args, **kwargs): # real signature unknown
        pass

    def set_max_width_chars(self, *args, **kwargs): # real signature unknown
        pass

    def set_mnemonic_widget(self, *args, **kwargs): # real signature unknown
        pass

    def set_pattern(self, *args, **kwargs): # real signature unknown
        pass

    def set_selectable(self, *args, **kwargs): # real signature unknown
        pass

    def set_single_line_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_text_with_mnemonic(self, *args, **kwargs): # real signature unknown
        pass

    def set_track_visited_links(self, *args, **kwargs): # real signature unknown
        pass

    def set_use_markup(self, *args, **kwargs): # real signature unknown
        pass

    def set_use_underline(self, *args, **kwargs): # real signature unknown
        pass

    def set_width_chars(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


