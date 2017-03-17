# encoding: utf-8
# module gtk.gdk
# from /usr/lib/python2.7/dist-packages/webkit/webkit.x86_64-linux-gnu.so
# by generator 1.143
# no doc

# imports
from exceptions import Warning

import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import pango as __pango
import pangocairo as __pangocairo


from Drawable import Drawable

class Window(Drawable):
    """
    Object GdkWindow
    
    Signals from GdkWindow:
      pick-embedded-child (gdouble, gdouble) -> GdkWindow
      to-embedder (gdouble, gdouble, gpointer, gpointer)
      from-embedder (gdouble, gdouble, gpointer, gpointer)
    
    Properties from GdkWindow:
      cursor -> GdkCursor: Cursor
        Cursor
    
    Signals from GObject:
      notify (GParam)
    """
    def add_filter(self, *args, **kwargs): # real signature unknown
        pass

    def beep(self, *args, **kwargs): # real signature unknown
        pass

    def begin_move_drag(self, *args, **kwargs): # real signature unknown
        pass

    def begin_paint_rect(self, *args, **kwargs): # real signature unknown
        pass

    def begin_paint_region(self, *args, **kwargs): # real signature unknown
        pass

    def begin_resize_drag(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clear_area(self, *args, **kwargs): # real signature unknown
        pass

    def clear_area_e(self, *args, **kwargs): # real signature unknown
        pass

    def configure_finished(self, *args, **kwargs): # real signature unknown
        pass

    def deiconify(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def destroy_notify(self, *args, **kwargs): # real signature unknown
        pass

    def drag_begin(self, *args, **kwargs): # real signature unknown
        pass

    def enable_synchronized_configure(self, *args, **kwargs): # real signature unknown
        pass

    def end_paint(self, *args, **kwargs): # real signature unknown
        pass

    def ensure_native(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def focus(self, *args, **kwargs): # real signature unknown
        pass

    def freeze_updates(self, *args, **kwargs): # real signature unknown
        pass

    def fullscreen(self, *args, **kwargs): # real signature unknown
        pass

    def geometry_changed(self, *args, **kwargs): # real signature unknown
        pass

    def get_accept_focus(self, *args, **kwargs): # real signature unknown
        pass

    def get_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_composited(self, *args, **kwargs): # real signature unknown
        pass

    def get_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def get_decorations(self, *args, **kwargs): # real signature unknown
        pass

    def get_deskrelative_origin(self, *args, **kwargs): # real signature unknown
        pass

    def get_effective_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_effective_toplevel(self, *args, **kwargs): # real signature unknown
        pass

    def get_events(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_on_map(self, *args, **kwargs): # real signature unknown
        pass

    def get_frame_extents(self, *args, **kwargs): # real signature unknown
        pass

    def get_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def get_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_modal_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_origin(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def get_position(self, *args, **kwargs): # real signature unknown
        pass

    def get_root_origin(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_toplevel(self, *args, **kwargs): # real signature unknown
        pass

    def get_type_hint(self, *args, **kwargs): # real signature unknown
        pass

    def get_update_area(self, *args, **kwargs): # real signature unknown
        pass

    def get_user_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_type(self, *args, **kwargs): # real signature unknown
        pass

    def has_native(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def iconify(self, *args, **kwargs): # real signature unknown
        pass

    def input_set_extension_events(self, *args, **kwargs): # real signature unknown
        pass

    def input_shape_combine_mask(self, *args, **kwargs): # real signature unknown
        pass

    def input_shape_combine_region(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate_rect(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate_region(self, *args, **kwargs): # real signature unknown
        pass

    def is_destroyed(self, *args, **kwargs): # real signature unknown
        pass

    def is_input_only(self, *args, **kwargs): # real signature unknown
        pass

    def is_shaped(self, *args, **kwargs): # real signature unknown
        pass

    def is_viewable(self, *args, **kwargs): # real signature unknown
        pass

    def is_visible(self, *args, **kwargs): # real signature unknown
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        pass

    def maximize(self, *args, **kwargs): # real signature unknown
        pass

    def merge_child_input_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def merge_child_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def move_region(self, *args, **kwargs): # real signature unknown
        pass

    def move_resize(self, *args, **kwargs): # real signature unknown
        pass

    def move_to_current_desktop(self, *args, **kwargs): # real signature unknown
        pass

    def process_updates(self, *args, **kwargs): # real signature unknown
        pass

    def property_change(self, *args, **kwargs): # real signature unknown
        pass

    def property_delete(self, *args, **kwargs): # real signature unknown
        pass

    def property_get(self, *args, **kwargs): # real signature unknown
        pass

    def raise_(self, *args, **kwargs): # real signature unknown
        pass

    def redirect_to_drawable(self, *args, **kwargs): # real signature unknown
        pass

    def register_dnd(self, *args, **kwargs): # real signature unknown
        pass

    def remove_redirection(self, *args, **kwargs): # real signature unknown
        pass

    def reparent(self, *args, **kwargs): # real signature unknown
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def restack(self, *args, **kwargs): # real signature unknown
        pass

    def scroll(self, *args, **kwargs): # real signature unknown
        pass

    def selection_convert(self, *args, **kwargs): # real signature unknown
        pass

    def set_accept_focus(self, *args, **kwargs): # real signature unknown
        pass

    def set_background(self, *args, **kwargs): # real signature unknown
        pass

    def set_back_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def set_child_input_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def set_child_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def set_composited(self, *args, **kwargs): # real signature unknown
        pass

    def set_cursor(self, *args, **kwargs): # real signature unknown
        pass

    def set_decorations(self, *args, **kwargs): # real signature unknown
        pass

    def set_events(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_on_map(self, *args, **kwargs): # real signature unknown
        pass

    def set_functions(self, *args, **kwargs): # real signature unknown
        pass

    def set_geometry_hints(self, *args, **kwargs): # real signature unknown
        pass

    def set_group(self, *args, **kwargs): # real signature unknown
        pass

    def set_hints(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_keep_above(self, *args, **kwargs): # real signature unknown
        pass

    def set_keep_below(self, *args, **kwargs): # real signature unknown
        pass

    def set_modal_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_opacity(self, *args, **kwargs): # real signature unknown
        pass

    def set_override_redirect(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_pager_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_taskbar_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_startup_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_static_gravities(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, *args, **kwargs): # real signature unknown
        pass

    def set_transient_for(self, *args, **kwargs): # real signature unknown
        pass

    def set_type_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_urgency_hint(self, *args, **kwargs): # real signature unknown
        pass

    def set_user_data(self, *args, **kwargs): # real signature unknown
        pass

    def set_user_time(self, *args, **kwargs): # real signature unknown
        pass

    def shape_combine_mask(self, *args, **kwargs): # real signature unknown
        pass

    def shape_combine_region(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def show_unraised(self, *args, **kwargs): # real signature unknown
        pass

    def stick(self, *args, **kwargs): # real signature unknown
        pass

    def thaw_updates(self, *args, **kwargs): # real signature unknown
        pass

    def unfullscreen(self, *args, **kwargs): # real signature unknown
        pass

    def unmaximize(self, *args, **kwargs): # real signature unknown
        pass

    def unstick(self, *args, **kwargs): # real signature unknown
        pass

    def withdraw(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


