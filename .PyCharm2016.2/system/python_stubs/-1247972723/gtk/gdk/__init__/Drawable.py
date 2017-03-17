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


class Drawable(__gobject__gobject.GObject):
    """
    Object GdkDrawable
    
    Signals from GObject:
      notify (GParam)
    """
    def cairo_create(self, *args, **kwargs): # real signature unknown
        pass

    def copy_to_image(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_arc(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_drawable(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_glyphs(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_glyphs_transformed(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_image(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_pixbuf(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_rectangle(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_draw_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_clip_region(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_colormap(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_depth(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_image(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_screen(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_visible_region(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_visual(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_colormap(cls, *args, **kwargs): # real signature unknown
        pass

    def draw_arc(self, *args, **kwargs): # real signature unknown
        pass

    def draw_drawable(self, *args, **kwargs): # real signature unknown
        pass

    def draw_glyphs(self, *args, **kwargs): # real signature unknown
        pass

    def draw_gray_image(self, *args, **kwargs): # real signature unknown
        pass

    def draw_image(self, *args, **kwargs): # real signature unknown
        pass

    def draw_indexed_image(self, *args, **kwargs): # real signature unknown
        pass

    def draw_layout(self, *args, **kwargs): # real signature unknown
        pass

    def draw_layout_line(self, *args, **kwargs): # real signature unknown
        pass

    def draw_line(self, *args, **kwargs): # real signature unknown
        pass

    def draw_lines(self, *args, **kwargs): # real signature unknown
        pass

    def draw_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def draw_point(self, *args, **kwargs): # real signature unknown
        pass

    def draw_points(self, *args, **kwargs): # real signature unknown
        pass

    def draw_polygon(self, *args, **kwargs): # real signature unknown
        pass

    def draw_rectangle(self, *args, **kwargs): # real signature unknown
        pass

    def draw_rgb_32_image(self, *args, **kwargs): # real signature unknown
        pass

    def draw_rgb_image(self, *args, **kwargs): # real signature unknown
        pass

    def draw_segments(self, *args, **kwargs): # real signature unknown
        pass

    def draw_string(self, *args, **kwargs): # real signature unknown
        pass

    def draw_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_clip_region(self, *args, **kwargs): # real signature unknown
        pass

    def get_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def get_depth(self, *args, **kwargs): # real signature unknown
        pass

    def get_display(self, *args, **kwargs): # real signature unknown
        pass

    def get_image(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible_region(self, *args, **kwargs): # real signature unknown
        pass

    def get_visual(self, *args, **kwargs): # real signature unknown
        pass

    def image_get(self, *args, **kwargs): # real signature unknown
        pass

    def new_gc(self, *args, **kwargs): # real signature unknown
        pass

    def set_colormap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nsview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nswindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


