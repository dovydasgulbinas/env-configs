# encoding: utf-8
# module sexy
# from /usr/lib/python2.7/dist-packages/gtk-2.0/sexy.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gtk as __gtk


# Variables with simple values

ICON_ENTRY_PRIMARY = 0
ICON_ENTRY_SECONDARY = 1

SPELL_ERROR_BACKEND = 0

# functions

def sexy_icon_entry_get_type(*args, **kwargs): # real signature unknown
    pass

def sexy_spell_entry_get_type(*args, **kwargs): # real signature unknown
    pass

def sexy_tooltip_get_type(*args, **kwargs): # real signature unknown
    pass

def sexy_tooltip_new_with_label(*args, **kwargs): # real signature unknown
    pass

def sexy_tree_view_get_type(*args, **kwargs): # real signature unknown
    pass

def sexy_url_label_get_type(*args, **kwargs): # real signature unknown
    pass

# classes

class IconEntry(__gtk.Entry):
    """
    Object SexyIconEntry
    
    Signals from SexyIconEntry:
      icon-pressed (gint, gint)
      icon-released (gint, gint)
    
    Signals from GtkEditable:
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
      changed ()
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkEntry:
      populate-popup (GtkMenu)
      activate ()
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
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
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
      changed ()
    
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
    def add_clear_button(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_highlight(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_highlight(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class IconEntryPosition(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
    }
    __gtype__ = None # (!) real value is ''


class SpellEntry(__gtk.Entry):
    """
    Object SexySpellEntry
    
    Signals from SexySpellEntry:
      word-check (gchararray) -> gboolean
    
    Signals from GtkEditable:
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
      changed ()
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkEntry:
      populate-popup (GtkMenu)
      activate ()
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
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
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
      changed ()
    
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
    def activate_default_languages(self, *args, **kwargs): # real signature unknown
        pass

    def activate_language(self, *args, **kwargs): # real signature unknown
        pass

    def deactivate_language(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_languages(self, *args, **kwargs): # real signature unknown
        pass

    def get_languages(self, *args, **kwargs): # real signature unknown
        pass

    def get_language_name(self, *args, **kwargs): # real signature unknown
        pass

    def is_checked(self, *args, **kwargs): # real signature unknown
        pass

    def language_is_active(self, *args, **kwargs): # real signature unknown
        pass

    def set_active_languages(self, *args, **kwargs): # real signature unknown
        pass

    def set_checked(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class SpellError(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
    }
    __gtype__ = None # (!) real value is ''


class Tooltip(__gtk.Window):
    """
    Object SexyTooltip
    
    Signals from GtkWindow:
      set-focus (GtkWidget)
      frame-event (GdkEvent) -> gboolean
      activate-focus ()
      activate-default ()
      keys-changed ()
    
    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      allow-shrink -> gboolean: Allow Shrink
        If TRUE, the window has no mimimum size. Setting this to TRUE is 99% of the time a bad idea
      allow-grow -> gboolean: Allow Grow
        If TRUE, users can expand the window beyond its minimum size
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      opacity -> gdouble: Opacity for Window
        The opacity of the window, from 0 to 1
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
    
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
    def position_to_rect(self, *args, **kwargs): # real signature unknown
        pass

    def position_to_widget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class TreeView(__gtk.TreeView):
    """
    Object SexyTreeView
    
    Signals from SexyTreeView:
      get-tooltip (GtkTreePath, GtkTreeViewColumn) -> GtkWidget
    
    Signals from GtkTreeView:
      move-cursor (GtkMovementStep, gint) -> gboolean
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      row-activated (GtkTreePath, GtkTreeViewColumn)
      test-expand-row (GtkTreeIter, GtkTreePath) -> gboolean
      test-collapse-row (GtkTreeIter, GtkTreePath) -> gboolean
      row-expanded (GtkTreeIter, GtkTreePath)
      row-collapsed (GtkTreeIter, GtkTreePath)
      columns-changed ()
      cursor-changed ()
      select-all () -> gboolean
      unselect-all () -> gboolean
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
    def set_tooltip_label_column(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class UrlLabel(__gtk.Label):
    """
    Object SexyUrlLabel
    
    Signals from SexyUrlLabel:
      url-activated (gchararray)
    
    Signals from GtkLabel:
      populate-popup (GtkMenu)
      move-cursor (GtkMovementStep, gint, gboolean)
      copy-clipboard ()
      activate-current-link ()
      activate-link (gchararray) -> gboolean
    
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
    def set_markup(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


