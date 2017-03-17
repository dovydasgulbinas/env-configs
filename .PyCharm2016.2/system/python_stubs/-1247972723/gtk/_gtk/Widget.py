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


from Object import Object

from Buildable import Buildable

class Widget(Object, __atk.ImplementorIface, Buildable):
    """
    Object GtkWidget
    
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
    def activate(self, *args, **kwargs): # real signature unknown
        pass

    def add_accelerator(self, *args, **kwargs): # real signature unknown
        pass

    def add_events(self, *args, **kwargs): # real signature unknown
        pass

    def add_mnemonic_label(self, *args, **kwargs): # real signature unknown
        pass

    def can_activate_accel(self, *args, **kwargs): # real signature unknown
        pass

    def child_focus(self, *args, **kwargs): # real signature unknown
        pass

    def child_notify(self, *args, **kwargs): # real signature unknown
        pass

    def class_path(self, *args, **kwargs): # real signature unknown
        pass

    def create_pango_context(self, *args, **kwargs): # real signature unknown
        pass

    def create_pango_layout(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_button_press_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_button_release_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_can_activate_accel(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_client_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_composited_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_configure_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delete_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_destroy_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_direction_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_begin(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_data_delete(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_data_get(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_data_received(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_drop(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_end(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_leave(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_drag_motion(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_enter_notify_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_expose_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus_in_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus_out_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_accessible(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_grab_broken_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_grab_focus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_grab_notify(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_hide(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_hide_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_hierarchy_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_key_press_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_key_release_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_leave_notify_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_map(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_map_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_mnemonic_activate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_motion_notify_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_no_expose_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_parent_set(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_popup_menu(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_property_notify_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_proximity_in_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_proximity_out_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_realize(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_screen_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_scroll_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_selection_clear_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_selection_get(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_selection_notify_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_selection_received(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_selection_request_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_show(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_show_all(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_show_help(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_size_allocate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_size_request(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_state_changed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_style_set(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unmap(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unmap_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unrealize(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_visibility_notify_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_window_state_event(cls, *args, **kwargs): # real signature unknown
        pass

    def drag_begin(self, *args, **kwargs): # real signature unknown
        pass

    def drag_check_threshold(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_add_image_targets(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_add_text_targets(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_add_uri_targets(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_find_target(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_get_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_get_track_motion(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_set(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_set_proxy(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_set_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_set_track_motion(self, *args, **kwargs): # real signature unknown
        pass

    def drag_dest_unset(self, *args, **kwargs): # real signature unknown
        pass

    def drag_get_data(self, *args, **kwargs): # real signature unknown
        pass

    def drag_highlight(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_add_image_targets(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_add_text_targets(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_add_uri_targets(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_get_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_set(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_set_icon(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_set_icon_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_set_icon_stock(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_set_target_list(self, *args, **kwargs): # real signature unknown
        pass

    def drag_source_unset(self, *args, **kwargs): # real signature unknown
        pass

    def drag_unhighlight(self, *args, **kwargs): # real signature unknown
        pass

    def draw(self, *args, **kwargs): # real signature unknown
        pass

    def ensure_style(self, *args, **kwargs): # real signature unknown
        pass

    def error_bell(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def freeze_child_notify(self, *args, **kwargs): # real signature unknown
        pass

    def get_accessible(self, *args, **kwargs): # real signature unknown
        pass

    def get_action(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_activate_signal(cls, *args, **kwargs): # real signature unknown
        pass

    def get_allocation(self, *args, **kwargs): # real signature unknown
        pass

    def get_ancestor(self, *args, **kwargs): # real signature unknown
        pass

    def get_app_paintable(self, *args, **kwargs): # real signature unknown
        pass

    def get_can_default(self, *args, **kwargs): # real signature unknown
        pass

    def get_can_focus(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_requisition(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def get_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def get_composite_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_direction(self, *args, **kwargs): # real signature unknown
        pass

    def get_display(self, *args, **kwargs): # real signature unknown
        pass

    def get_double_buffered(self, *args, **kwargs): # real signature unknown
        pass

    def get_events(self, *args, **kwargs): # real signature unknown
        pass

    def get_extension_events(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_mapped(self, *args, **kwargs): # real signature unknown
        pass

    def get_modifier_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_no_show_all(self, *args, **kwargs): # real signature unknown
        pass

    def get_pango_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def get_realized(self, *args, **kwargs): # real signature unknown
        pass

    def get_receives_default(self, *args, **kwargs): # real signature unknown
        pass

    def get_requisition(self, *args, **kwargs): # real signature unknown
        pass

    def get_root_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def get_settings(self, *args, **kwargs): # real signature unknown
        pass

    def get_size_request(self, *args, **kwargs): # real signature unknown
        pass

    def get_snapshot(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_markup(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_toplevel(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_visual(self, *args, **kwargs): # real signature unknown
        pass

    def get_window(self, *args, **kwargs): # real signature unknown
        pass

    def grab_add(self, *args, **kwargs): # real signature unknown
        pass

    def grab_default(self, *args, **kwargs): # real signature unknown
        pass

    def grab_focus(self, *args, **kwargs): # real signature unknown
        pass

    def grab_remove(self, *args, **kwargs): # real signature unknown
        pass

    def has_default(self, *args, **kwargs): # real signature unknown
        pass

    def has_focus(self, *args, **kwargs): # real signature unknown
        pass

    def has_grab(self, *args, **kwargs): # real signature unknown
        pass

    def has_rc_style(self, *args, **kwargs): # real signature unknown
        pass

    def has_screen(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def hide_all(self, *args, **kwargs): # real signature unknown
        pass

    def hide_on_delete(self, *args, **kwargs): # real signature unknown
        pass

    def input_shape_combine_mask(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        pass

    def is_ancestor(self, *args, **kwargs): # real signature unknown
        pass

    def is_composited(self, *args, **kwargs): # real signature unknown
        pass

    def is_drawable(self, *args, **kwargs): # real signature unknown
        pass

    def is_focus(self, *args, **kwargs): # real signature unknown
        pass

    def is_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def is_toplevel(self, *args, **kwargs): # real signature unknown
        pass

    def keynav_failed(self, *args, **kwargs): # real signature unknown
        pass

    def list_accel_closures(self, *args, **kwargs): # real signature unknown
        pass

    def list_mnemonic_labels(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def menu_get_for_attach_widget(self, *args, **kwargs): # real signature unknown
        pass

    def mnemonic_activate(self, *args, **kwargs): # real signature unknown
        pass

    def modify_base(self, *args, **kwargs): # real signature unknown
        pass

    def modify_bg(self, *args, **kwargs): # real signature unknown
        pass

    def modify_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def modify_fg(self, *args, **kwargs): # real signature unknown
        pass

    def modify_font(self, *args, **kwargs): # real signature unknown
        pass

    def modify_style(self, *args, **kwargs): # real signature unknown
        pass

    def modify_text(self, *args, **kwargs): # real signature unknown
        pass

    def path(self, *args, **kwargs): # real signature unknown
        pass

    def queue_clear(self, *args, **kwargs): # real signature unknown
        pass

    def queue_clear_area(self, *args, **kwargs): # real signature unknown
        pass

    def queue_draw(self, *args, **kwargs): # real signature unknown
        pass

    def queue_draw_area(self, *args, **kwargs): # real signature unknown
        pass

    def queue_resize(self, *args, **kwargs): # real signature unknown
        pass

    def queue_resize_no_redraw(self, *args, **kwargs): # real signature unknown
        pass

    def rc_get_style(self, *args, **kwargs): # real signature unknown
        pass

    def realize(self, *args, **kwargs): # real signature unknown
        pass

    def region_intersect(self, *args, **kwargs): # real signature unknown
        pass

    def remove_accelerator(self, *args, **kwargs): # real signature unknown
        pass

    def remove_mnemonic_label(self, *args, **kwargs): # real signature unknown
        pass

    def render_icon(self, *args, **kwargs): # real signature unknown
        pass

    def reparent(self, *args, **kwargs): # real signature unknown
        pass

    def reset_rc_styles(self, *args, **kwargs): # real signature unknown
        pass

    def reset_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def selection_add_target(self, *args, **kwargs): # real signature unknown
        pass

    def selection_add_targets(self, *args, **kwargs): # real signature unknown
        pass

    def selection_clear_targets(self, *args, **kwargs): # real signature unknown
        pass

    def selection_convert(self, *args, **kwargs): # real signature unknown
        pass

    def selection_owner_set(self, *args, **kwargs): # real signature unknown
        pass

    def selection_remove_all(self, *args, **kwargs): # real signature unknown
        pass

    def send_expose(self, *args, **kwargs): # real signature unknown
        pass

    def send_focus_change(self, *args, **kwargs): # real signature unknown
        pass

    def set_accel_path(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def set_activate_signal(cls, *args, **kwargs): # real signature unknown
        pass

    def set_allocation(self, *args, **kwargs): # real signature unknown
        pass

    def set_app_paintable(self, *args, **kwargs): # real signature unknown
        pass

    def set_can_default(self, *args, **kwargs): # real signature unknown
        pass

    def set_can_focus(self, *args, **kwargs): # real signature unknown
        pass

    def set_child_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def set_composite_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_direction(self, *args, **kwargs): # real signature unknown
        pass

    def set_double_buffered(self, *args, **kwargs): # real signature unknown
        pass

    def set_events(self, *args, **kwargs): # real signature unknown
        pass

    def set_extension_events(self, *args, **kwargs): # real signature unknown
        pass

    def set_has_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def set_has_window(self, *args, **kwargs): # real signature unknown
        pass

    def set_mapped(self, *args, **kwargs): # real signature unknown
        pass

    def set_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_no_show_all(self, *args, **kwargs): # real signature unknown
        pass

    def set_parent(self, *args, **kwargs): # real signature unknown
        pass

    def set_parent_window(self, *args, **kwargs): # real signature unknown
        pass

    def set_realized(self, *args, **kwargs): # real signature unknown
        pass

    def set_receives_default(self, *args, **kwargs): # real signature unknown
        pass

    def set_redraw_on_allocate(self, *args, **kwargs): # real signature unknown
        pass

    def set_scroll_adjustments(self, *args, **kwargs): # real signature unknown
        pass

    def set_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def set_set_scroll_adjustments_signal(cls, *args, **kwargs): # real signature unknown
        pass

    def set_size_request(self, *args, **kwargs): # real signature unknown
        pass

    def set_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_markup(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_window(self, *args, **kwargs): # real signature unknown
        pass

    def set_uposition(self, *args, **kwargs): # real signature unknown
        pass

    def set_usize(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_window(self, *args, **kwargs): # real signature unknown
        pass

    def shape_combine_mask(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def show_all(self, *args, **kwargs): # real signature unknown
        pass

    def show_now(self, *args, **kwargs): # real signature unknown
        pass

    def size_allocate(self, *args, **kwargs): # real signature unknown
        pass

    def size_request(self, *args, **kwargs): # real signature unknown
        pass

    def style_attach(self, *args, **kwargs): # real signature unknown
        pass

    def style_get_property(self, *args, **kwargs): # real signature unknown
        pass

    def thaw_child_notify(self, *args, **kwargs): # real signature unknown
        pass

    def translate_coordinates(self, *args, **kwargs): # real signature unknown
        pass

    def trigger_tooltip_query(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def unparent(self, *args, **kwargs): # real signature unknown
        pass

    def unrealize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    requisition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


