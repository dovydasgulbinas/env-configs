# encoding: utf-8
# module atk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/atk.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import __main__ as ____main__


from Object import Object

from Component import Component

from Action import Action

from EditableText import EditableText

from Image import Image

from Selection import Selection

from Table import Table

from Text import Text

from Hypertext import Hypertext

from Value import Value

from Document import Document

class NoOpObject(Object, Component, Action, EditableText, Image, Selection, Table, ____main__.atk.TableCell, Text, Hypertext, Value, Document, ____main__.atk.Window):
    """
    Object AtkNoOpObject
    
    Signals from AtkComponent:
      bounds-changed (AtkRectangle)
    
    Signals from AtkSelection:
      selection-changed ()
    
    Signals from AtkTable:
      row-inserted (gint, gint)
      column-inserted (gint, gint)
      row-deleted (gint, gint)
      column-deleted (gint, gint)
      row-reordered ()
      column-reordered ()
      model-changed ()
    
    Signals from AtkText:
      text-changed (gint, gint)
      text-insert (gint, gint, gchararray)
      text-remove (gint, gint, gchararray)
      text-caret-moved (gint)
      text-selection-changed ()
      text-attributes-changed ()
    
    Signals from AtkHypertext:
      link-selected (gint)
    
    Signals from AtkValue:
      value-changed (gdouble, gchararray)
    
    Signals from AtkDocument:
      load-complete ()
      reload ()
      load-stopped ()
      page-changed (gint)
    
    Signals from AtkWindow:
      activate ()
      create ()
      deactivate ()
      destroy ()
      maximize ()
      minimize ()
      move ()
      resize ()
      restore ()
    
    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
    
    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance's name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Parent of the current accessible as returned by atk_object_get_parent()
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> gint: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


