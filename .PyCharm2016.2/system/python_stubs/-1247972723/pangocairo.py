# encoding: utf-8
# module pangocairo
# from /usr/lib/python2.7/dist-packages/gtk-2.0/pangocairo.so
# by generator 1.143
# no doc

# imports
import cairo as __cairo
import gobject as __gobject


# functions

def cairo_font_map_get_default(*args, **kwargs): # real signature unknown
    pass

def cairo_font_map_new(*args, **kwargs): # real signature unknown
    pass

def context_get_font_options(*args, **kwargs): # real signature unknown
    pass

def context_get_resolution(*args, **kwargs): # real signature unknown
    pass

def context_set_font_options(*args, **kwargs): # real signature unknown
    pass

def context_set_resolution(*args, **kwargs): # real signature unknown
    pass

def error_underline_path(*args, **kwargs): # real signature unknown
    pass

def show_error_underline(*args, **kwargs): # real signature unknown
    pass

# classes

class CairoContext(__cairo.Context):
    """ A cairo.Context enhanced with some additional pango methods """
    def create_layout(self, *args, **kwargs): # real signature unknown
        pass

    def glyph_string_path(self, *args, **kwargs): # real signature unknown
        pass

    def layout_line_path(self, *args, **kwargs): # real signature unknown
        pass

    def layout_path(self, *args, **kwargs): # real signature unknown
        pass

    def show_glyph_string(self, *args, **kwargs): # real signature unknown
        pass

    def show_layout(self, *args, **kwargs): # real signature unknown
        pass

    def show_layout_line(self, *args, **kwargs): # real signature unknown
        pass

    def update_context(self, *args, **kwargs): # real signature unknown
        pass

    def update_layout(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class CairoFontMap(__gobject.GInterface):
    # no doc
    def create_context(self, *args, **kwargs): # real signature unknown
        pass

    def get_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


