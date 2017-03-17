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

class TextView(Container):
    """
    Object GtkTextView
    
    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      copy-clipboard ()
      populate-popup (GtkMenu)
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      select-all (gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      preedit-changed (gchararray)
      page-horizontally (gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      toggle-cursor-visible ()
    
    Properties from GtkTextView:
      pixels-above-lines -> gint: Pixels Above Lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels Below Lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels Inside Wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      left-margin -> gint: Left Margin
        Width of the left margin in pixels
      right-margin -> gint: Right Margin
        Width of the right margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      cursor-visible -> gboolean: Cursor Visible
        If the insertion cursor is shown
      buffer -> GtkTextBuffer: Buffer
        The buffer which is displayed
      overwrite -> gboolean: Overwrite mode
        Whether entered text overwrites existing contents
      accepts-tab -> gboolean: Accepts tab
        Whether Tab will result in a tab character being entered
      im-module -> gchararray: IM module
        Which IM module should be used
    
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
    def add_child_at_anchor(self, *args, **kwargs): # real signature unknown
        pass

    def add_child_in_window(self, *args, **kwargs): # real signature unknown
        pass

    def backward_display_line(self, *args, **kwargs): # real signature unknown
        pass

    def backward_display_line_start(self, *args, **kwargs): # real signature unknown
        pass

    def buffer_to_window_coords(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_backspace(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_copy_clipboard(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_cut_clipboard(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delete_from_cursor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_insert_at_cursor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_move_cursor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_move_focus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_page_horizontally(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_paste_clipboard(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_populate_popup(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_anchor(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_scroll_adjustments(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_toggle_overwrite(cls, *args, **kwargs): # real signature unknown
        pass

    def forward_display_line(self, *args, **kwargs): # real signature unknown
        pass

    def forward_display_line_end(self, *args, **kwargs): # real signature unknown
        pass

    def get_accepts_tab(self, *args, **kwargs): # real signature unknown
        pass

    def get_border_window_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def get_cursor_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def get_editable(self, *args, **kwargs): # real signature unknown
        pass

    def get_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_indent(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_location(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_position(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_location(self, *args, **kwargs): # real signature unknown
        pass

    def get_justification(self, *args, **kwargs): # real signature unknown
        pass

    def get_left_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_at_y(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_yrange(self, *args, **kwargs): # real signature unknown
        pass

    def get_overwrite(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixels_above_lines(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixels_below_lines(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixels_inside_wrap(self, *args, **kwargs): # real signature unknown
        pass

    def get_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def get_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_rect(self, *args, **kwargs): # real signature unknown
        pass

    def get_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def im_context_filter_keypress(self, *args, **kwargs): # real signature unknown
        pass

    def move_child(self, *args, **kwargs): # real signature unknown
        pass

    def move_mark_onscreen(self, *args, **kwargs): # real signature unknown
        pass

    def move_visually(self, *args, **kwargs): # real signature unknown
        pass

    def place_cursor_onscreen(self, *args, **kwargs): # real signature unknown
        pass

    def reset_im_context(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_mark_onscreen(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_to_iter(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_to_mark(self, *args, **kwargs): # real signature unknown
        pass

    def set_accepts_tab(self, *args, **kwargs): # real signature unknown
        pass

    def set_border_window_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def set_cursor_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_editable(self, *args, **kwargs): # real signature unknown
        pass

    def set_indent(self, *args, **kwargs): # real signature unknown
        pass

    def set_justification(self, *args, **kwargs): # real signature unknown
        pass

    def set_left_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_overwrite(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixels_above_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixels_below_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixels_inside_wrap(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def set_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def starts_display_line(self, *args, **kwargs): # real signature unknown
        pass

    def window_to_buffer_coords(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


