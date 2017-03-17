# encoding: utf-8
# module gtkunixprint
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtkunixprint.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


# Variables with simple values

PRINT_CAPABILITY_COLLATE = 4
PRINT_CAPABILITY_COPIES = 2

PRINT_CAPABILITY_GENERATE_PDF = 32
PRINT_CAPABILITY_GENERATE_PS = 64

PRINT_CAPABILITY_NUMBER_UP = 256

PRINT_CAPABILITY_NUMBER_UP_LAYOUT = 512

PRINT_CAPABILITY_PAGE_SET = 1

PRINT_CAPABILITY_PREVIEW = 128
PRINT_CAPABILITY_REVERSE = 8
PRINT_CAPABILITY_SCALE = 16

__version__ = '2.24.0'

# functions

def enumerate_printers(*args, **kwargs): # real signature unknown
    pass

# classes

class PageSetupUnixDialog(__gtk.Dialog):
    """
    Object GtkPageSetupUnixDialog
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      has-separator -> gboolean: Has separator
        The dialog has a separator bar above its buttons
    
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
    def get_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_settings(self, *args, **kwargs): # real signature unknown
        pass

    def set_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_settings(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class PrintCapabilities(__gobject.GFlags):
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
        128: 128,
        256: 256,
        512: 512,
    }
    __gtype__ = None # (!) real value is ''


class Printer(__gobject__gobject.GObject):
    """
    Object GtkPrinter
    
    Signals from GtkPrinter:
      details-acquired (gboolean)
    
    Properties from GtkPrinter:
      name -> gchararray: Name
        Name of the printer
      backend -> GtkPrintBackend: Backend
        Backend for the printer
      is-virtual -> gboolean: Is Virtual
        FALSE if this represents a real hardware printer
      state-message -> gchararray: State Message
        String giving the current state of the printer
      location -> gchararray: Location
        The location of the printer
      icon-name -> gchararray: Icon Name
        The icon name to use for the printer
      job-count -> gint: Job Count
        Number of jobs queued in the printer
      accepts-pdf -> gboolean: Accepts PDF
        TRUE if this printer can accept PDF
      accepts-ps -> gboolean: Accepts PostScript
        TRUE if this printer can accept PostScript
      paused -> gboolean: Paused Printer
        TRUE if this printer is paused
      accepting-jobs -> gboolean: Accepting Jobs
        TRUE if this printer is accepting new jobs
    
    Signals from GObject:
      notify (GParam)
    """
    def accepts_pdf(self, *args, **kwargs): # real signature unknown
        pass

    def accepts_ps(self, *args, **kwargs): # real signature unknown
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_details_acquired(cls, *args, **kwargs): # real signature unknown
        pass

    def get_capabilities(self, *args, **kwargs): # real signature unknown
        pass

    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_job_count(self, *args, **kwargs): # real signature unknown
        pass

    def get_location(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_state_message(self, *args, **kwargs): # real signature unknown
        pass

    def has_details(self, *args, **kwargs): # real signature unknown
        pass

    def is_accepting_jobs(self, *args, **kwargs): # real signature unknown
        pass

    def is_active(self, *args, **kwargs): # real signature unknown
        pass

    def is_default(self, *args, **kwargs): # real signature unknown
        pass

    def is_paused(self, *args, **kwargs): # real signature unknown
        pass

    def is_virtual(self, *args, **kwargs): # real signature unknown
        pass

    def list_papers(self, *args, **kwargs): # real signature unknown
        pass

    def request_details(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PrintJob(__gobject__gobject.GObject):
    """
    Object GtkPrintJob
    
    Signals from GtkPrintJob:
      status-changed ()
    
    Properties from GtkPrintJob:
      title -> gchararray: Title
        Title of the print job
      printer -> GtkPrinter: Printer
        Printer to print the job to
      page-setup -> GtkPageSetup: Page Setup
        Page Setup
      settings -> GtkPrintSettings: Settings
        Printer settings
      track-print-status -> gboolean: Track Print Status
        TRUE if the print job will continue to emit status-changed signals after the print data has been sent to the printer or print server.
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_status_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_printer(self, *args, **kwargs): # real signature unknown
        pass

    def get_settings(self, *args, **kwargs): # real signature unknown
        pass

    def get_status(self, *args, **kwargs): # real signature unknown
        pass

    def get_surface(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_track_print_status(self, *args, **kwargs): # real signature unknown
        pass

    def send(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_file(self, *args, **kwargs): # real signature unknown
        pass

    def set_track_print_status(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PrintUnixDialog(__gtk.Dialog):
    """
    Object GtkPrintUnixDialog
    
    Properties from GtkPrintUnixDialog:
      page-setup -> GtkPageSetup: Page Setup
        The GtkPageSetup to use
      current-page -> gint: Current Page
        The current page in the document
      print-settings -> GtkPrintSettings: Print Settings
        The GtkPrintSettings used for initializing the dialog
      selected-printer -> GtkPrinter: Selected Printer
        The GtkPrinter which is selected
      manual-capabilities -> GtkPrintCapabilities: Manual Capabilites
        Capabilities the application can handle
      support-selection -> gboolean: Support Selection
        Whether the dialog supports selection
      has-selection -> gboolean: Has Selection
        Whether the application has a selection
      embed-page-setup -> gboolean: Embed Page Setup
        TRUE if page setup combos are embedded in GtkPrintUnixDialog
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      has-separator -> gboolean: Has separator
        The dialog has a separator bar above its buttons
    
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
    def add_custom_tab(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_page(self, *args, **kwargs): # real signature unknown
        pass

    def get_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def get_selected_printer(self, *args, **kwargs): # real signature unknown
        pass

    def get_settings(self, *args, **kwargs): # real signature unknown
        pass

    def set_current_page(self, *args, **kwargs): # real signature unknown
        pass

    def set_manual_capabilities(self, *args, **kwargs): # real signature unknown
        pass

    def set_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def set_settings(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


