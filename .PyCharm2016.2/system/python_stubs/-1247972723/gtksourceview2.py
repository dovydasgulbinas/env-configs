# encoding: utf-8
# module gtksourceview2
# from /usr/lib/python2.7/dist-packages/gtksourceview2.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


# Variables with simple values

COMPLETION_ACTIVATION_INTERACTIVE = 1
COMPLETION_ACTIVATION_NONE = 0

COMPLETION_ACTIVATION_USER_REQUESTED = 2

COMPLETION_ERROR_ALREADY_BOUND = 0

COMPLETION_ERROR_NOT_BOUND = 1

DRAW_SPACES_ALL = 127
DRAW_SPACES_LEADING = 16
DRAW_SPACES_NBSP = 8
DRAW_SPACES_NEWLINE = 4
DRAW_SPACES_SPACE = 1
DRAW_SPACES_TAB = 2
DRAW_SPACES_TEXT = 32
DRAW_SPACES_TRAILING = 64

SEARCH_CASE_INSENSITIVE = 4

SEARCH_TEXT_ONLY = 2

SEARCH_VISIBLE_ONLY = 1

SMART_HOME_END_AFTER = 2
SMART_HOME_END_ALWAYS = 3
SMART_HOME_END_BEFORE = 1
SMART_HOME_END_DISABLED = 0

__version__ = '2.10.1'

# functions

def completion_item_new_from_stock(*args, **kwargs): # real signature unknown
    pass

def completion_item_new_with_markup(*args, **kwargs): # real signature unknown
    pass

def iter_backward_search(*args, **kwargs): # real signature unknown
    pass

def iter_forward_search(*args, **kwargs): # real signature unknown
    pass

def language_manager_get_default(*args, **kwargs): # real signature unknown
    pass

def print_compositor_new_from_view(*args, **kwargs): # real signature unknown
    pass

def style_scheme_manager_get_default(*args, **kwargs): # real signature unknown
    pass

# classes

class Buffer(__gtk.TextBuffer):
    """
    Object GtkSourceBuffer
    
    Signals from GtkSourceBuffer:
      highlight-updated (GtkTextIter, GtkTextIter)
      source-mark-updated (GtkTextMark)
      undo ()
      redo ()
    
    Properties from GtkSourceBuffer:
      can-undo -> gboolean: Can undo
        Whether Undo operation is possible
      can-redo -> gboolean: Can redo
        Whether Redo operation is possible
      highlight-syntax -> gboolean: Highlight Syntax
        Whether to highlight syntax in the buffer
      highlight-matching-brackets -> gboolean: Highlight Matching Brackets
        Whether to highlight matching brackets
      max-undo-levels -> gint: Maximum Undo Levels
        Number of undo levels for the buffer
      language -> GtkSourceLanguage: Language
        Language object to get highlighting patterns from
      style-scheme -> GtkSourceStyleScheme: Style scheme
        Style scheme
      undo-manager -> GtkSourceUndoManager: Undo manager
        The buffer undo manager
    
    Signals from GtkTextBuffer:
      insert-text (GtkTextIter, gchararray, gint)
      insert-pixbuf (GtkTextIter, GdkPixbuf)
      insert-child-anchor (GtkTextIter, GtkTextChildAnchor)
      delete-range (GtkTextIter, GtkTextIter)
      changed ()
      modified-changed ()
      mark-set (GtkTextIter, GtkTextMark)
      mark-deleted (GtkTextMark)
      apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      begin-user-action ()
      end-user-action ()
      paste-done (GtkClipboard)
    
    Properties from GtkTextBuffer:
      tag-table -> GtkTextTagTable: Tag Table
        Text Tag Table
      text -> gchararray: Text
        Current text of the buffer
      has-selection -> gboolean: Has selection
        Whether the buffer has some text currently selected
      cursor-position -> gint: Cursor position
        The position of the insert mark (as offset from the beginning of the buffer)
      copy-target-list -> GtkTargetList: Copy target list
        The list of targets this buffer supports for clipboard copying and DND source
      paste-target-list -> GtkTargetList: Paste target list
        The list of targets this buffer supports for clipboard pasting and DND destination
    
    Signals from GObject:
      notify (GParam)
    """
    def backward_iter_to_source_mark(self, *args, **kwargs): # real signature unknown
        pass

    def begin_not_undoable_action(self, *args, **kwargs): # real signature unknown
        pass

    def can_redo(self, *args, **kwargs): # real signature unknown
        pass

    def can_undo(self, *args, **kwargs): # real signature unknown
        pass

    def create_source_mark(self, *args, **kwargs): # real signature unknown
        pass

    def end_not_undoable_action(self, *args, **kwargs): # real signature unknown
        pass

    def ensure_highlight(self, *args, **kwargs): # real signature unknown
        pass

    def forward_iter_to_source_mark(self, *args, **kwargs): # real signature unknown
        pass

    def get_context_classes_at_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_matching_brackets(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def get_language(self, *args, **kwargs): # real signature unknown
        pass

    def get_max_undo_levels(self, *args, **kwargs): # real signature unknown
        pass

    def get_source_marks_at_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_source_marks_at_line(self, *args, **kwargs): # real signature unknown
        pass

    def get_style_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def get_undo_manager(self, *args, **kwargs): # real signature unknown
        pass

    def iter_backward_to_context_class_toggle(self, *args, **kwargs): # real signature unknown
        pass

    def iter_forward_to_context_class_toggle(self, *args, **kwargs): # real signature unknown
        pass

    def iter_has_context_class(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self, *args, **kwargs): # real signature unknown
        pass

    def remove_source_marks(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_matching_brackets(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def set_language(self, *args, **kwargs): # real signature unknown
        pass

    def set_max_undo_levels(self, *args, **kwargs): # real signature unknown
        pass

    def set_style_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def set_undo_manager(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Completion(__gobject__gobject.GObject):
    """
    Object GtkSourceCompletion
    
    Signals from GtkSourceCompletion:
      show ()
      hide ()
      populate-context (GtkSourceCompletionContext)
      move-cursor (GtkScrollStep, gint)
      move-page (GtkScrollStep, gint)
      activate-proposal ()
    
    Properties from GtkSourceCompletion:
      view -> GtkSourceView: View
        The GtkSourceView bound to the completion
      remember-info-visibility -> gboolean: Remember Info Visibility
        Remember the last info window visibility state
      select-on-show -> gboolean: Select on Show
        Select first proposal when completion is shown
      show-headers -> gboolean: Show Headers
        Show provider headers when proposals from multiple providers are available
      show-icons -> gboolean: Show Icons
        Show provider and proposal icons in the completion popup
      accelerators -> guint: Accelerators
        Number of proposal accelerators to show
      auto-complete-delay -> guint: Auto Complete Delay
        Completion popup delay for interactive completion
      provider-page-size -> guint: Provider Page Size
        Provider scrolling page size
      proposal-page-size -> guint: Proposal Page Size
        Proposal scrolling page size
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def add_provider(self, *args, **kwargs): # real signature unknown
        pass

    def create_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_info_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_providers(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def move_window(self, *args, **kwargs): # real signature unknown
        pass

    def remove_provider(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CompletionActivation(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is ''


class CompletionContext(__gobject__gobject.GObject):
    """
    Object GtkSourceCompletionContext
    
    Signals from GtkSourceCompletionContext:
      cancelled ()
    
    Properties from GtkSourceCompletionContext:
      completion -> GtkSourceCompletion: Completion
        The completion object to which the context belongs
      iter -> GtkTextIter: Iterator
        The GtkTextIter at which the completion was invoked
      activation -> GtkSourceCompletionActivation: Activation
        The type of activation
    
    Signals from GObject:
      notify (GParam)
    """
    def add_proposals(self, *args, **kwargs): # real signature unknown
        pass

    def get_activation(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CompletionError(__gobject.GEnum):
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


class CompletionInfo(__gtk.Window):
    """
    Object GtkSourceCompletionInfo
    
    Signals from GtkSourceCompletionInfo:
      before-show ()
    
    Properties from GtkSourceCompletionInfo:
      max-width -> gint: Maximum width
        The maximum allowed width
      max-height -> gint: Maximum height
        The maximum allowed height
      shrink-width -> gboolean: Shrink width
        Whether the window should shrink width to fit the contents
      shrink-height -> gboolean: Shrink height
        Whether the window should shrink height to fit the contents
    
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
    def get_widget(self, *args, **kwargs): # real signature unknown
        pass

    def move_to_iter(self, *args, **kwargs): # real signature unknown
        pass

    def process_resize(self, *args, **kwargs): # real signature unknown
        pass

    def set_sizing(self, *args, **kwargs): # real signature unknown
        pass

    def set_widget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class CompletionProposal(__gobject.GInterface):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_equal(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_icon(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_info(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_label(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_markup(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_hash(cls, *args, **kwargs): # real signature unknown
        pass

    def equal(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_info(self, *args, **kwargs): # real signature unknown
        pass

    def get_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_markup(self, *args, **kwargs): # real signature unknown
        pass

    def get_text(self, *args, **kwargs): # real signature unknown
        pass

    def hash(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CompletionItem(__gobject__gobject.GObject, CompletionProposal):
    """
    Object GtkSourceCompletionItem
    
    Properties from GtkSourceCompletionItem:
      label -> gchararray: Label
        Label to be shown for this item
      markup -> gchararray: Markup
        Markup to be shown for this item
      text -> gchararray: Text
        Item text
      icon -> GdkPixbuf: Icon
        Icon to be shown for this item
      info -> gchararray: Info
        Info to be shown for this item
    
    Signals from GtkSourceCompletionProposal:
      changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CompletionProvider(__gobject.GInterface):
    # no doc
    def activate_proposal(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_activate_proposal(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_activation(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_icon(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_info_widget(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_name(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_start_iter(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_match(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_populate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_update_info(cls, *args, **kwargs): # real signature unknown
        pass

    def get_activation(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_info_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_start_iter(self, *args, **kwargs): # real signature unknown
        pass

    def match(self, *args, **kwargs): # real signature unknown
        pass

    def populate(self, *args, **kwargs): # real signature unknown
        pass

    def update_info(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CompletionWords(__gobject__gobject.GObject, CompletionProvider):
    """
    Object GtkSourceCompletionWords
    
    Properties from GtkSourceCompletionWords:
      name -> gchararray: Name
        The provider name
      icon -> GdkPixbuf: Icon
        The provider icon
      proposals-batch-size -> guint: Proposals Batch Size
        Number of proposals added in one batch
      scan-batch-size -> guint: Scan Batch Size
        Number of lines scanned in one batch
      minimum-word-size -> guint: Minimum Word Size
        The minimum word size to complete
      interactive-delay -> gint: Interactive Delay
        The delay before initiating interactive completion
      priority -> gint: Priority
        Provider priority
    
    Signals from GObject:
      notify (GParam)
    """
    def register(self, *args, **kwargs): # real signature unknown
        pass

    def unregister(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class DrawSpacesFlags(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        127: 127,
    }
    __gtype__ = None # (!) real value is ''


class Gutter(__gobject__gobject.GObject):
    """
    Object GtkSourceGutter
    
    Signals from GtkSourceGutter:
      query-tooltip (GtkCellRenderer, GtkTextIter, GtkTooltip) -> gboolean
      cell-activated (GtkCellRenderer, GtkTextIter, GdkEvent)
    
    Properties from GtkSourceGutter:
      view -> GtkSourceView: View
        The gutters' GtkSourceView
      window-type -> GtkTextWindowType: Window Type
        The gutters text window type
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_cell_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_query_tooltip(cls, *args, **kwargs): # real signature unknown
        pass

    def get_window(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def queue_draw(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def reorder(self, *args, **kwargs): # real signature unknown
        pass

    def set_cell_data_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_cell_size_func(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Language(__gobject__gobject.GObject):
    """
    Object GtkSourceLanguage
    
    Properties from GtkSourceLanguage:
      id -> gchararray: Language id
        Language id
      name -> gchararray: Language name
        Language name
      section -> gchararray: Language section
        Language section
      hidden -> gboolean: Hidden
        Whether the language should be hidden from the user
    
    Signals from GObject:
      notify (GParam)
    """
    def get_globs(self, *args, **kwargs): # real signature unknown
        pass

    def get_hidden(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_metadata(self, *args, **kwargs): # real signature unknown
        pass

    def get_mime_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_section(self, *args, **kwargs): # real signature unknown
        pass

    def get_style_ids(self, *args, **kwargs): # real signature unknown
        pass

    def get_style_name(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gtype__ = None # (!) real value is ''


class LanguageManager(__gobject__gobject.GObject):
    """
    Object GtkSourceLanguageManager
    
    Properties from GtkSourceLanguageManager:
      search-path -> GStrv: Language specification directories
        List of directories where the language specification files (.lang) are located
      language-ids -> GStrv: Language ids
        List of the ids of the available languages
    
    Signals from GObject:
      notify (GParam)
    """
    def get_language(self, *args, **kwargs): # real signature unknown
        pass

    def get_language_ids(self, *args, **kwargs): # real signature unknown
        pass

    def get_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def guess_language(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Mark(__gtk.TextMark):
    """
    Object GtkSourceMark
    
    Properties from GtkSourceMark:
      category -> gchararray: category
        The mark category
    
    Properties from GtkTextMark:
      name -> gchararray: Name
        Mark name
      left-gravity -> gboolean: Left gravity
        Whether the mark has left gravity
    
    Signals from GObject:
      notify (GParam)
    """
    def get_category(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def prev(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PrintCompositor(__gobject__gobject.GObject):
    """
    Object GtkSourcePrintCompositor
    
    Properties from GtkSourcePrintCompositor:
      buffer -> GtkSourceBuffer: Source Buffer
        The GtkSourceBuffer object to print
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries.
      highlight-syntax -> gboolean: Highlight Syntax
        Whether to print the document with highlighted syntax
      print-line-numbers -> guint: Print Line Numbers
        Interval of printed line numbers (0 means no numbers)
      print-header -> gboolean: Print Header
        Whether to print a header in each page
      print-footer -> gboolean: Print Footer
        Whether to print a footer in each page
      body-font-name -> gchararray: Body Font Name
        Name of the font to use for the text body (e.g. "Monospace 10")
      line-numbers-font-name -> gchararray: Line Numbers Font Name
        Name of the font to use for the line numbers (e.g. "Monospace 10")
      header-font-name -> gchararray: Header Font Name
        Name of the font to use for the page header (e.g. "Monospace 10")
      footer-font-name -> gchararray: Footer Font Name
        Name of the font to use for the page footer (e.g. "Monospace 10")
      n-pages -> gint: Number of pages
        The number of pages in the document (-1 means the document has not been completely paginated).
    
    Signals from GObject:
      notify (GParam)
    """
    def draw_page(self, *args, **kwargs): # real signature unknown
        pass

    def get_body_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_bottom_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def get_footer_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_header_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def get_left_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_numbers_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_pages(self, *args, **kwargs): # real signature unknown
        pass

    def get_pagination_progress(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_footer(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_header(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def get_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_top_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def paginate(self, *args, **kwargs): # real signature unknown
        pass

    def set_body_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_bottom_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_footer_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_footer_format(self, *args, **kwargs): # real signature unknown
        pass

    def set_header_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_header_format(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def set_left_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_numbers_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_footer(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_header(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_top_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class SearchFlags(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
    }
    __gtype__ = None # (!) real value is ''


class SmartHomeEndType(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __gtype__ = None # (!) real value is ''


class Style(__gobject__gobject.GObject):
    """
    Object GtkSourceStyle
    
    Properties from GtkSourceStyle:
      line-background -> gchararray: Line background
        Line background color
      line-background-set -> gboolean: Line background set
        Whether line background color is set
      background -> gchararray: Background
        Background color
      background-set -> gboolean: Background set
        Whether background color is set
      foreground -> gchararray: Foreground
        Foreground color
      foreground-set -> gboolean: Foreground set
        Whether foreground color is set
      bold -> gboolean: Bold
        Bold
      bold-set -> gboolean: Bold set
        Whether bold attribute is set
      italic -> gboolean: Italic
        Italic
      italic-set -> gboolean: Italic set
        Whether italic attribute is set
      underline -> gboolean: Underline
        Underline
      underline-set -> gboolean: Underline set
        Whether underline attribute is set
      strikethrough -> gboolean: Strikethrough
        Strikethrough
      strikethrough-set -> gboolean: Strikethrough set
        Whether strikethrough attribute is set
    
    Signals from GObject:
      notify (GParam)
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class StyleScheme(__gobject__gobject.GObject):
    """
    Object GtkSourceStyleScheme
    
    Properties from GtkSourceStyleScheme:
      id -> gchararray: Style scheme id
        Style scheme id
      name -> gchararray: Style scheme name
        Style scheme name
      description -> gchararray: Style scheme description
        Style scheme description
      filename -> gchararray: Style scheme filename
        Style scheme filename
    
    Signals from GObject:
      notify (GParam)
    """
    def get_authors(self, *args, **kwargs): # real signature unknown
        pass

    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_filename(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_style(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gtype__ = None # (!) real value is ''


class StyleSchemeManager(__gobject__gobject.GObject):
    """
    Object GtkSourceStyleSchemeManager
    
    Properties from GtkSourceStyleSchemeManager:
      search-path -> GStrv: Style scheme search path
        List of directories and files where the style schemes are located
      scheme-ids -> GStrv: Scheme ids
        List of the ids of the available style schemes
    
    Signals from GObject:
      notify (GParam)
    """
    def append_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def force_rescan(self, *args, **kwargs): # real signature unknown
        pass

    def get_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def get_scheme_ids(self, *args, **kwargs): # real signature unknown
        pass

    def get_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def prepend_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class UndoManager(__gobject.GInterface):
    # no doc
    def begin_not_undoable_action(self, *args, **kwargs): # real signature unknown
        pass

    def can_redo(self, *args, **kwargs): # real signature unknown
        pass

    def can_redo_changed(self, *args, **kwargs): # real signature unknown
        pass

    def can_undo(self, *args, **kwargs): # real signature unknown
        pass

    def can_undo_changed(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_begin_not_undoable_action(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_can_redo(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_can_redo_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_can_undo(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_can_undo_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_end_not_undoable_action(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_redo(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_undo(cls, *args, **kwargs): # real signature unknown
        pass

    def end_not_undoable_action(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class View(__gtk.TextView):
    """
    Object GtkSourceView
    
    Signals from GtkSourceView:
      undo ()
      redo ()
      show-completion ()
      line-mark-activated (GtkTextIter, GdkEvent)
      move-lines (gboolean, gint)
    
    Properties from GtkSourceView:
      completion -> GtkSourceCompletion: Completion
        The completion object associated with the view
      show-line-numbers -> gboolean: Show Line Numbers
        Whether to display line numbers
      show-line-marks -> gboolean: Show Line Marks
        Whether to display line mark pixbufs
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      indent-width -> gint: Indent Width
        Number of spaces to use for each step of indent
      auto-indent -> gboolean: Auto Indentation
        Whether to enable auto indentation
      insert-spaces-instead-of-tabs -> gboolean: Insert Spaces Instead of Tabs
        Whether to insert spaces instead of tabs
      show-right-margin -> gboolean: Show Right Margin
        Whether to display the right margin
      right-margin-position -> guint: Right Margin Position
        Position of the right margin
      smart-home-end -> GtkSourceSmartHomeEndType: Smart Home/End
        HOME and END keys move to first/last non whitespace characters on line before going to the start/end of the line
      highlight-current-line -> gboolean: Highlight current line
        Whether to highlight the current line
      indent-on-tab -> gboolean: Indent on tab
        Whether to indent the selected text when the tab key is pressed
      draw-spaces -> GtkSourceDrawSpacesFlags: Draw Spaces
        Set if and how the spaces should be visualized
    
    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      page-horizontally (gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      populate-popup (GtkMenu)
      select-all (gboolean)
      toggle-cursor-visible ()
      preedit-changed (gchararray)
    
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
    @classmethod
    def do_line_mark_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_redo(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_undo(cls, *args, **kwargs): # real signature unknown
        pass

    def get_auto_indent(self, *args, **kwargs): # real signature unknown
        pass

    def get_completion(self, *args, **kwargs): # real signature unknown
        pass

    def get_draw_spaces(self, *args, **kwargs): # real signature unknown
        pass

    def get_gutter(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_current_line(self, *args, **kwargs): # real signature unknown
        pass

    def get_indent_on_tab(self, *args, **kwargs): # real signature unknown
        pass

    def get_indent_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_insert_spaces_instead_of_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark_category_background(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark_category_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark_category_priority(self, *args, **kwargs): # real signature unknown
        pass

    def get_right_margin_position(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_line_marks(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_smart_home_end(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_auto_indent(self, *args, **kwargs): # real signature unknown
        pass

    def set_draw_spaces(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_current_line(self, *args, **kwargs): # real signature unknown
        pass

    def set_indent_on_tab(self, *args, **kwargs): # real signature unknown
        pass

    def set_indent_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_insert_spaces_instead_of_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_background(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_icon_from_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_icon_from_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_icon_from_stock(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_priority(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_tooltip_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_tooltip_markup_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin_position(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_line_marks(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_smart_home_end(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


# variables with complex values

pygtksourceview2_version = (
    2,
    10,
    1,
)

