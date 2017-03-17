# encoding: utf-8
# module lxml.etree
# from /usr/lib/python2.7/dist-packages/lxml/etree.so
# by generator 1.143
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from HTMLParser import HTMLParser

class HTMLPullParser(HTMLParser):
    """
    HTMLPullParser(self, events=None, *, tag=None, base_url=None, **kwargs)
    
        HTML parser that collects parse events in an iterator.
    
        The collected events are the same as for iterparse(), but the
        parser itself is non-blocking in the sense that it receives
        data chunks incrementally through its .feed() method, instead
        of reading them directly from a file(-like) object all by itself.
    
        By default, it collects Element end events.  To change that,
        pass any subset of the available events into the ``events``
        argument: ``'start'``, ``'end'``, ``'start-ns'``,
        ``'end-ns'``, ``'comment'``, ``'pi'``.
    
        To support loading external dependencies relative to the input
        source, you can pass the ``base_url``.
    """
    def read_events(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, events=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


