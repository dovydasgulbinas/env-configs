# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from object import object

class pyqtProperty(object):
    """
    pyqtProperty(type, fget=None, fset=None, freset=None, fdel=None, doc=None,
            designable=True, scriptable=True, stored=True, user=False,
            constant=False, final=False, notify=None) -> property attribute
    
    type is the type of the property.  It is either a type object or a string
    that is the name of a C++ type.
    freset is a function for resetting an attribute to its default value.
    designable sets the DESIGNABLE flag (the default is True for writable
    properties and False otherwise).
    scriptable sets the SCRIPTABLE flag.
    stored sets the STORED flag.
    user sets the USER flag.
    constant sets the CONSTANT flag.
    final sets the FINAL flag.
    notify is the NOTIFY signal.
    The other parameters are the same as those required by the standard Python
    property type.  Properties defined using pyqtProperty behave as both Python
    and Qt properties.
    Decorators can be used to define new properties or to modify existing ones.
    """
    def deleter(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the deleter on a property. """
        pass

    def getter(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the getter on a property. """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the getter on a property. """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the reset on a property. """
        pass

    def setter(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the setter on a property. """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the setter on a property. """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __delete__(self, obj): # real signature unknown; restored from __doc__
        """ descr.__delete__(obj) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, type, fget=None, fset=None, freset=None, fdel=None, doc=None, designable=True, scriptable=True, stored=True, user=False, constant=False, final=False, notify=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __set__(self, obj, value): # real signature unknown; restored from __doc__
        """ descr.__set__(obj, value) """
        pass

    fdel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



