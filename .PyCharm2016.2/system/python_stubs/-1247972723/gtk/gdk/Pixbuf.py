# encoding: utf-8
# module gtk.gdk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.143
# no doc

# imports
from exceptions import Warning

import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import pango as __pango
import pangocairo as __pangocairo


class Pixbuf(__gobject__gobject.GObject, __gio.Icon, __gio.LoadableIcon):
    """
    Object GdkPixbuf
    
    Properties from GdkPixbuf:
      colorspace -> GdkColorspace: Colorspace
        The colorspace in which the samples are interpreted
      n-channels -> gint: Number of Channels
        The number of samples per pixel
      has-alpha -> gboolean: Has Alpha
        Whether the pixbuf has an alpha channel
      bits-per-sample -> gint: Bits per Sample
        The number of bits per sample
      width -> gint: Width
        The number of columns of the pixbuf
      height -> gint: Height
        The number of rows of the pixbuf
      rowstride -> gint: Rowstride
        The number of bytes between the start of a row and the start of the next row
      pixels -> gpointer: Pixels
        A pointer to the pixel data of the pixbuf
      pixel-bytes -> GBytes: Pixel Bytes
        Readonly pixel data
    
    Signals from GObject:
      notify (GParam)
    """
    def add_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def apply_embedded_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def composite(self, *args, **kwargs): # real signature unknown
        pass

    def composite_color(self, *args, **kwargs): # real signature unknown
        pass

    def composite_color_simple(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_area(self, *args, **kwargs): # real signature unknown
        pass

    def fill(self, *args, **kwargs): # real signature unknown
        pass

    def flip(self, *args, **kwargs): # real signature unknown
        pass

    def get_bits_per_sample(self, *args, **kwargs): # real signature unknown
        pass

    def get_colorspace(self, *args, **kwargs): # real signature unknown
        pass

    def get_from_drawable(self, *args, **kwargs): # real signature unknown
        pass

    def get_from_image(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_channels(self, *args, **kwargs): # real signature unknown
        pass

    def get_option(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixels(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixels_array(self, *args, **kwargs): # real signature unknown
        pass

    def get_rowstride(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def render_pixmap_and_mask(self, *args, **kwargs): # real signature unknown
        pass

    def render_threshold_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def render_to_drawable(self, *args, **kwargs): # real signature unknown
        pass

    def render_to_drawable_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def rotate_simple(self, *args, **kwargs): # real signature unknown
        pass

    def saturate_and_pixelate(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def save_to_callback(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def scale_simple(self, *args, **kwargs): # real signature unknown
        pass

    def subpixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    pixel_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


