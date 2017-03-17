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

class xmlfile(object):
    """
    xmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)
    
        A simple mechanism for incremental XML serialisation.
    
        Usage example::
    
             with xmlfile("somefile.xml", encoding='utf-8') as xf:
                 xf.write_declaration(standalone=True)
                 xf.write_doctype('<!DOCTYPE root SYSTEM "some.dtd">')
    
                 # generate an element (the root element)
                 with xf.element('root'):
                      # write a complete Element into the open root element
                      xf.write(etree.Element('test'))
    
                      # generate and write more Elements, e.g. through iterparse
                      for element in generate_some_elements():
                          # serialise generated elements into the XML file
                          xf.write(element)
    
                      # or write multiple Elements or strings at once
                      xf.write(etree.Element('start'), "text", etree.Element('end'))
    
        If 'output_file' is a file(-like) object, passing ``close=True`` will
        close it when exiting the context manager.  By default, it is left
        to the owner to do that.  When a file path is used, lxml will take care
        of opening and closing the file itself.  Also, when a compression level
        is set, lxml will deliberately close the file to make sure all data gets
        compressed and written.
    
        Setting ``buffered=False`` will flush the output after each operation,
        such as opening or closing an ``xf.element()`` block or calling
        ``xf.write()``.  Alternatively, calling ``xf.flush()`` can be used to
        explicitly flush any pending output when buffering is enabled.
    """
    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, output_file, encoding=None, compression=None, close=False, buffered=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


