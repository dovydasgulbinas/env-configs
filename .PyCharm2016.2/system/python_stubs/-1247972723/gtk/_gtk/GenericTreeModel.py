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

class GenericTreeModel(__gobject__gobject.GObject, TreeModel):
    """
    Object PyGtkGenericTreeModel
    
    Properties from PyGtkGenericTreeModel:
      leak-references -> gboolean: Leak references
        Enable referencing iterator objects (this will cause a memory leak or at least a reference counting leak). You might need it though, if you return newly created objects.
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GObject:
      notify (GParam)
    """
    def create_tree_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_user_data(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate_iters(self, *args, **kwargs): # real signature unknown
        pass

    def iter_is_valid(self, *args, **kwargs): # real signature unknown
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


