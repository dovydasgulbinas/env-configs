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


class StatusIcon(__gobject__gobject.GObject):
    """
    Object GtkStatusIcon
    
    Signals from GtkStatusIcon:
      size-changed (gint) -> gboolean
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu (guint, guint)
      activate ()
    
    Properties from GtkStatusIcon:
      pixbuf -> GdkPixbuf: Pixbuf
        A GdkPixbuf to display
      file -> gchararray: Filename
        Filename to load and display
      stock -> gchararray: Stock ID
        Stock ID for a stock image to display
      icon-name -> gchararray: Icon Name
        The name of the icon from the icon theme
      gicon -> GIcon: GIcon
        The GIcon being displayed
      storage-type -> GtkImageType: Storage type
        The representation being used for image data
      size -> gint: Size
        The size of the icon
      screen -> GdkScreen: Screen
        The screen where this status icon will be displayed
      visible -> gboolean: Visible
        Whether or not the status icon is visible
      orientation -> GtkOrientation: Orientation
        The orientation of the tray
      embedded -> gboolean: Embedded
        Whether or not the status icon is embedded
      blinking -> gboolean: Blinking
        Whether or not the status icon is blinking
      has-tooltip -> gboolean: Has tooltip
        Whether this tray icon has a tooltip
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this tray icon
      title -> gchararray: Title
        The title of this tray icon
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_activate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_popup_menu(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_size_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_blinking(self, *args, **kwargs): # real signature unknown
        pass

    def get_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def get_gicon(self, *args, **kwargs): # real signature unknown
        pass

    def get_has_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_stock(self, *args, **kwargs): # real signature unknown
        pass

    def get_storage_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_markup(self, *args, **kwargs): # real signature unknown
        pass

    def get_tooltip_text(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_x11_window_id(self, *args, **kwargs): # real signature unknown
        pass

    def is_embedded(self, *args, **kwargs): # real signature unknown
        pass

    def set_blinking(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_file(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_gicon(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_stock(self, *args, **kwargs): # real signature unknown
        pass

    def set_has_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def set_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_markup(self, *args, **kwargs): # real signature unknown
        pass

    def set_tooltip_text(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


