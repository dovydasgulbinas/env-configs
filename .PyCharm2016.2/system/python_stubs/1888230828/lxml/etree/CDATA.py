# encoding: utf-8
# module lxml.etree
# from /opt/odoo/_venv/local/lib/python2.7/site-packages/lxml/etree.so
# by generator 1.143
"""
The ``lxml.etree`` module implements the extended ElementTree API
for XML.
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from object import object

class CDATA(object):
    """
    CDATA(data)
    
        CDATA factory.  This factory creates an opaque data object that
        can be used to set Element text.  The usual way to use it is::
    
            >>> el = Element('content')
            >>> el.text = CDATA('a string')
    
            >>> print(el.text)
            a string
            >>> print(tostring(el, encoding="unicode"))
            <content><![CDATA[a string]]></content>
    """
    def __init__(self, data): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


