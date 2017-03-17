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


from CellRenderer import CellRenderer

class CellRendererSpinner(CellRenderer):
    """
    Object GtkCellRendererSpinner
    
    Properties from GtkCellRendererSpinner:
      active -> gboolean: Active
        Whether the spinner is active (ie. shown) in the cell
      pulse -> guint: Pulse
        Pulse of the spinner
      size -> GtkIconSize: Size
        The GtkIconSize value that specifies the size of the rendered spinner
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
        Editable mode of the CellRenderer
      visible -> gboolean: visible
        Display the cell
      sensitive -> gboolean: Sensitive
        Display the cell sensitive
      xalign -> gfloat: xalign
        The x-align
      yalign -> gfloat: yalign
        The y-align
      xpad -> guint: xpad
        The xpad
      ypad -> guint: ypad
        The ypad
      width -> gint: width
        The fixed width
      height -> gint: height
        The fixed height
      is-expander -> gboolean: Is Expander
        Row has children
      is-expanded -> gboolean: Is Expanded
        Row is an expander row, and is expanded
      cell-background -> gchararray: Cell background color name
        Cell background color as a string
      cell-background-gdk -> GdkColor: Cell background color
        Cell background color as a GdkColor
      cell-background-set -> gboolean: Cell background set
        Whether this tag affects the cell background color
      editing -> gboolean: Editing
        Whether the cell renderer is currently in editing mode
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


