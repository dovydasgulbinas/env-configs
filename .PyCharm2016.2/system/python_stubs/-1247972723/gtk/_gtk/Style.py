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


class Style(__gobject__gobject.GObject):
    """
    Object GtkStyle
    
    Signals from GtkStyle:
      realize ()
      unrealize ()
    
    Signals from GObject:
      notify (GParam)
    """
    def apply_default_background(self, *args, **kwargs): # real signature unknown
        pass

    def apply_default_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def attach(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_clone(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_copy(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_arrow(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_box(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_box_gap(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_check(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_diamond(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_expander(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_extension(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_flat_box(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_focus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_handle(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_hline(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_layout(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_option(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_resize_grip(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_shadow(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_shadow_gap(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_slider(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_string(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_tab(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_vline(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_init_from_rc(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_realize(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_render_icon(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_background(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unrealize(cls, *args, **kwargs): # real signature unknown
        pass

    def get_font(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_color(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_icon_set(self, *args, **kwargs): # real signature unknown
        pass

    def paint_arrow(self, *args, **kwargs): # real signature unknown
        pass

    def paint_box(self, *args, **kwargs): # real signature unknown
        pass

    def paint_box_gap(self, *args, **kwargs): # real signature unknown
        pass

    def paint_check(self, *args, **kwargs): # real signature unknown
        pass

    def paint_diamond(self, *args, **kwargs): # real signature unknown
        pass

    def paint_expander(self, *args, **kwargs): # real signature unknown
        pass

    def paint_extension(self, *args, **kwargs): # real signature unknown
        pass

    def paint_flat_box(self, *args, **kwargs): # real signature unknown
        pass

    def paint_focus(self, *args, **kwargs): # real signature unknown
        pass

    def paint_handle(self, *args, **kwargs): # real signature unknown
        pass

    def paint_hline(self, *args, **kwargs): # real signature unknown
        pass

    def paint_layout(self, *args, **kwargs): # real signature unknown
        pass

    def paint_option(self, *args, **kwargs): # real signature unknown
        pass

    def paint_polygon(self, *args, **kwargs): # real signature unknown
        pass

    def paint_resize_grip(self, *args, **kwargs): # real signature unknown
        pass

    def paint_shadow(self, *args, **kwargs): # real signature unknown
        pass

    def paint_shadow_gap(self, *args, **kwargs): # real signature unknown
        pass

    def paint_slider(self, *args, **kwargs): # real signature unknown
        pass

    def paint_string(self, *args, **kwargs): # real signature unknown
        pass

    def paint_tab(self, *args, **kwargs): # real signature unknown
        pass

    def paint_vline(self, *args, **kwargs): # real signature unknown
        pass

    def render_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_background(self, *args, **kwargs): # real signature unknown
        pass

    def set_font(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bg_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bg_pixmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    black = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    black_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dark_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fg_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mid_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_aa = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_aa_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    white = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    white_gc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xthickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ythickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


