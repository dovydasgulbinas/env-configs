# encoding: utf-8
# module lxml.etree
# from /usr/lib/python2.7/dist-packages/lxml/etree.so
# by generator 1.143
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from LxmlError import LxmlError

from SyntaxError import SyntaxError

class LxmlSyntaxError(LxmlError, SyntaxError):
    """ Base class for all syntax errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'LxmlSyntaxError'


