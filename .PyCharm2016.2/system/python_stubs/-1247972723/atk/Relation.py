# encoding: utf-8
# module atk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/atk.so
# by generator 1.143
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import __main__ as ____main__


class Relation(__gobject__gobject.GObject):
    """
    Object AtkRelation
    
    Properties from AtkRelation:
      relation-type -> AtkRelationType: Relation Type
        The type of the relation
      target -> GValueArray: Target
        An array of the targets for the relation
    
    Signals from GObject:
      notify (GParam)
    """
    def add_target(self, *args, **kwargs): # real signature unknown
        pass

    def get_relation_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_target(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


