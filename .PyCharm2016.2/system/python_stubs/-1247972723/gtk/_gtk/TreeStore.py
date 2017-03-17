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


from TreeModel import TreeModel

from TreeDragSource import TreeDragSource

from TreeDragDest import TreeDragDest

from TreeSortable import TreeSortable

from Buildable import Buildable

class TreeStore(__gobject__gobject.GObject, TreeModel, TreeDragSource, TreeDragDest, TreeSortable, Buildable):
    """
    Object GtkTreeStore
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GtkTreeSortable:
      sort-column-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def insert_after(self, *args, **kwargs): # real signature unknown
        pass

    def insert_before(self, *args, **kwargs): # real signature unknown
        pass

    def is_ancestor(self, *args, **kwargs): # real signature unknown
        pass

    def iter_depth(self, *args, **kwargs): # real signature unknown
        pass

    def iter_is_valid(self, *args, **kwargs): # real signature unknown
        pass

    def move_after(self, *args, **kwargs): # real signature unknown
        pass

    def move_before(self, *args, **kwargs): # real signature unknown
        pass

    def prepend(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def reorder(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def set_column_types(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def swap(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    __gtype__ = None # (!) real value is ''


