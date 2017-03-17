# encoding: utf-8
# module atk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/atk.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import __main__ as ____main__


class Object(__gobject__gobject.GObject):
    """
    Object AtkObject
    
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
    def add_relationship(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_focus_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_description(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_index_in_parent(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_layer(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_mdi_zorder(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_name(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_n_children(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_parent(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_role(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_ref_child(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_ref_relation_set(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_ref_state_set(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_remove_property_change_handler(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_description(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_name(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_parent(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_role(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_state_change(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_visible_data_changed(cls, *args, **kwargs): # real signature unknown
        pass

    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_index_in_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_layer(self, *args, **kwargs): # real signature unknown
        pass

    def get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_accessible_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_role(self, *args, **kwargs): # real signature unknown
        pass

    def ref_accessible_child(self, *args, **kwargs): # real signature unknown
        pass

    def ref_relation_set(self, *args, **kwargs): # real signature unknown
        pass

    def ref_state_set(self, *args, **kwargs): # real signature unknown
        pass

    def remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        pass

    def remove_relationship(self, *args, **kwargs): # real signature unknown
        pass

    def set_description(self, *args, **kwargs): # real signature unknown
        pass

    def set_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_parent(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


