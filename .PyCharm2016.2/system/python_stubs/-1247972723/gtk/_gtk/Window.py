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

class Window(Bin):
    """
    Object GtkWindow
    
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
    def activate_default(self, *args, **kwargs): # real signature unknown
        pass

    def activate_focus(self, *args, **kwargs): # real signature unknown
        pass

    def activate_key(self, *args, **kwargs): # real signature unknown
        pass

    def add_accel_group(self, *args, **kwargs): # real signature unknown
        pass

    def add_mnemonic(self, *args, **kwargs): # real signature unknown
        pass

    def begin_move_drag(self, *args, **kwargs): # real signature unknown
        pass

    def begin_resize_drag(self, *args, **kwargs): # real signature unknown
        pass

    def deiconify(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_activate_default(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_activate_focus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_frame_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_keys_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_move_focus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_focus(cls, *args, **kwargs): # real signature unknown
        pass

    def fullscreen(self, *args, **kwargs): # real signature unknown
        pass

    def get_accept_focus(self, *args, **kwargs): # real signature unknown
        pass

    def get_decorated(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_deletable(self, *args, **kwargs): # real signature unknown
        pass

    def get_destroy_with_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_on_map(self, *args, **kwargs): # real signature unknown
        pass

    def get_frame_dimensions(self, *args, **kwargs): # real signature unknown
        pass

    def get_gravity(self, *args, **kwargs): # real signature unknown
        pass

    def get_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_frame(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_mnemonics_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_mnemonic_modifier(self, *args, **kwargs): # real signature unknown
        pass

    def get_modal(self, *args, **kwargs): # real signature unknown
        pass

    def get_opacity(self, *args, **kwargs): # real signature unknown
        pass

    def get_position(self, *args, **kwargs): # real signature unknown
        pass

    def get_resizable(self, *args, **kwargs): # real signature unknown
        pass

    def get_role(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_skip_pager_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_skip_taskbar_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_transient_for(self, *args, **kwargs): # real signature unknown
        pass

    def get_type_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_urgency_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_type(self, *args, **kwargs): # real signature unknown
        pass

    def has_group(self, *args, **kwargs): # real signature unknown
        pass

    def has_toplevel_focus(self, *args, **kwargs): # real signature unknown
        pass

    def iconify(self, *args, **kwargs): # real signature unknown
        pass

    def is_active(self, *args, **kwargs): # real signature unknown
        pass

    def maximize(self, *args, **kwargs): # real signature unknown
        pass

    def mnemonic_activate(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def parse_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def present(self, *args, **kwargs): # real signature unknown
        pass

    def present_with_time(self, *args, **kwargs): # real signature unknown
        pass

    def propagate_key_event(self, *args, **kwargs): # real signature unknown
        pass

    def remove_accel_group(self, *args, **kwargs): # real signature unknown
        pass

    def remove_mnemonic(self, *args, **kwargs): # real signature unknown
        pass

    def reshow_with_initial_size(self, *args, **kwargs): # real signature unknown
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def set_accept_focus(self, *args, **kwargs): # real signature unknown
        pass

    def set_decorated(self, *args, **kwargs): # real signature unknown
        pass

    def set_default(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_deletable(self, *args, **kwargs): # real signature unknown
        pass

    def set_destroy_with_parent(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_on_map(self, *args, **kwargs): # real signature unknown
        pass

    def set_frame_dimensions(self, *args, **kwargs): # real signature unknown
        pass

    def set_geometry_hints(self, *args, **kwargs): # real signature unknown
        pass

    def set_gravity(self, *args, **kwargs): # real signature unknown
        pass

    def set_has_frame(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_from_file(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_keep_above(self, *args, **kwargs): # real signature unknown
        pass

    def set_keep_below(self, *args, **kwargs): # real signature unknown
        pass

    def set_mnemonics_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_mnemonic_modifier(self, *args, **kwargs): # real signature unknown
        pass

    def set_modal(self, *args, **kwargs): # real signature unknown
        pass

    def set_opacity(self, *args, **kwargs): # real signature unknown
        pass

    def set_policy(self, *args, **kwargs): # real signature unknown
        pass

    def set_position(self, *args, **kwargs): # real signature unknown
        pass

    def set_resizable(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_pager_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_taskbar_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_startup_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, *args, **kwargs): # real signature unknown
        pass

    def set_transient_for(self, *args, **kwargs): # real signature unknown
        pass

    def set_type_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_urgency_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_wmclass(self, *args, **kwargs): # real signature unknown
        pass

    def stick(self, *args, **kwargs): # real signature unknown
        pass

    def tooltips_get_info_from_tip_window(self, *args, **kwargs): # real signature unknown
        pass

    def unfullscreen(self, *args, **kwargs): # real signature unknown
        pass

    def unmaximize(self, *args, **kwargs): # real signature unknown
        pass

    def unstick(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    allow_grow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_shrink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    configure_notify_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    configure_request_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decorated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_with_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_user_ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iconify_initially = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keys_changed_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maximize_initially = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mnemonic_modifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_default_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_default_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stick_initially = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transient_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wmclass_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wmclass_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wm_role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


