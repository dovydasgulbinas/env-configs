# encoding: utf-8
# module atk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/atk.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import __main__ as ____main__


from Action import Action

class Hyperlink(__gobject__gobject.GObject, Action):
    """
    Object AtkHyperlink
    
    Signals from AtkHyperlink:
      link-activated ()
    
    Properties from AtkHyperlink:
      selected-link -> gboolean: Selected Link
        Specifies whether the AtkHyperlink object is selected
      number-of-anchors -> gint: Number of Anchors
        The number of anchors associated with the AtkHyperlink object
      end-index -> gint: End index
        The end index of the AtkHyperlink object
      start-index -> gint: Start index
        The start index of the AtkHyperlink object
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_get_end_index(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_n_anchors(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_object(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_start_index(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_uri(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_is_selected_link(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_is_valid(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_link_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_link_state(cls, *args, **kwargs): # real signature unknown
        pass

    def get_end_index(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_anchors(self, *args, **kwargs): # real signature unknown
        pass

    def get_object(self, *args, **kwargs): # real signature unknown
        pass

    def get_start_index(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def is_inline(self, *args, **kwargs): # real signature unknown
        pass

    def is_selected_link(self, *args, **kwargs): # real signature unknown
        pass

    def is_valid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


