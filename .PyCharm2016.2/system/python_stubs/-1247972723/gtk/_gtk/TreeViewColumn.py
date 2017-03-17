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

from CellLayout import CellLayout

from Buildable import Buildable

class TreeViewColumn(Object, CellLayout, Buildable):
    """
    Object GtkTreeViewColumn
    
    Signals from GtkTreeViewColumn:
      clicked ()
    
    Properties from GtkTreeViewColumn:
      visible -> gboolean: Visible
        Whether to display the column
      resizable -> gboolean: Resizable
        Column is user-resizable
      width -> gint: Width
        Current width of the column
      spacing -> gint: Spacing
        Space which is inserted between cells
      sizing -> GtkTreeViewColumnSizing: Sizing
        Resize mode of the column
      fixed-width -> gint: Fixed Width
        Current fixed width of the column
      min-width -> gint: Minimum Width
        Minimum allowed width of the column
      max-width -> gint: Maximum Width
        Maximum allowed width of the column
      title -> gchararray: Title
        Title to appear in column header
      expand -> gboolean: Expand
        Column gets share of extra width allocated to the widget
      clickable -> gboolean: Clickable
        Whether the header can be clicked
      widget -> GtkWidget: Widget
        Widget to put in column header button instead of column title
      alignment -> gfloat: Alignment
        X Alignment of the column header text or widget
      reorderable -> gboolean: Reorderable
        Whether the column can be reordered around the headers
      sort-indicator -> gboolean: Sort indicator
        Whether to show a sort indicator
      sort-order -> GtkSortType: Sort order
        Sort direction the sort indicator should indicate
      sort-column-id -> gint: Sort column ID
        Logical sort column ID this column sorts on when selected for sorting
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def add_attribute(self, *args, **kwargs): # real signature unknown
        pass

    def cell_get_position(self, *args, **kwargs): # real signature unknown
        pass

    def cell_get_size(self, *args, **kwargs): # real signature unknown
        pass

    def cell_is_visible(self, *args, **kwargs): # real signature unknown
        pass

    def cell_set_cell_data(self, *args, **kwargs): # real signature unknown
        pass

    def clear_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_clicked(cls, *args, **kwargs): # real signature unknown
        pass

    def focus_cell(self, *args, **kwargs): # real signature unknown
        pass

    def get_alignment(self, *args, **kwargs): # real signature unknown
        pass

    def get_cell_renderers(self, *args, **kwargs): # real signature unknown
        pass

    def get_clickable(self, *args, **kwargs): # real signature unknown
        pass

    def get_expand(self, *args, **kwargs): # real signature unknown
        pass

    def get_fixed_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_max_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_min_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def get_resizable(self, *args, **kwargs): # real signature unknown
        pass

    def get_sizing(self, *args, **kwargs): # real signature unknown
        pass

    def get_sort_column_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_sort_indicator(self, *args, **kwargs): # real signature unknown
        pass

    def get_sort_order(self, *args, **kwargs): # real signature unknown
        pass

    def get_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def get_title(self, *args, **kwargs): # real signature unknown
        pass

    def get_tree_view(self, *args, **kwargs): # real signature unknown
        pass

    def get_visible(self, *args, **kwargs): # real signature unknown
        pass

    def get_widget(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def queue_resize(self, *args, **kwargs): # real signature unknown
        pass

    def set_alignment(self, *args, **kwargs): # real signature unknown
        pass

    def set_clickable(self, *args, **kwargs): # real signature unknown
        pass

    def set_expand(self, *args, **kwargs): # real signature unknown
        pass

    def set_fixed_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_max_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_min_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_reorderable(self, *args, **kwargs): # real signature unknown
        pass

    def set_resizable(self, *args, **kwargs): # real signature unknown
        pass

    def set_sizing(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_column_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_indicator(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_order(self, *args, **kwargs): # real signature unknown
        pass

    def set_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible(self, *args, **kwargs): # real signature unknown
        pass

    def set_widget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


