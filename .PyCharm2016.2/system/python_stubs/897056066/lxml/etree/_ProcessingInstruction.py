# encoding: utf-8
# module lxml.etree
# from /home/hermes/miniconda3/envs/zeep_env/lib/python2.7/site-packages/lxml/etree.so
# by generator 1.143
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from __ContentOnlyElement import __ContentOnlyElement

class _ProcessingInstruction(__ContentOnlyElement):
    # no doc
    def get(self, key, default=None): # real signature unknown; restored from __doc__
        """
        get(self, key, default=None)
        
                Try to parse pseudo-attributes from the text content of the
                processing instruction, search for one with the given key as
                name and return its associated value.
        
                Note that this is only a convenience method for the most
                common case that all text content is structured in
                attribute-like name-value pairs with properly quoted values.
                It is not guaranteed to work for all possible text content.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    attrib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a dict containing all pseudo-attributes that can be
        parsed from the text content of this processing instruction.
        Note that modifying the dict currently has no effect on the
        XML node, although this is not guaranteed to stay this way.
        """

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


