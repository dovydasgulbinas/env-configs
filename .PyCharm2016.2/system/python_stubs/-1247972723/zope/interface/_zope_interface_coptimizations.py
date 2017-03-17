# encoding: utf-8
# module zope.interface._zope_interface_coptimizations
# from /usr/lib/python2.7/dist-packages/zope/interface/_zope_interface_coptimizations.x86_64-linux-gnu.so
# by generator 1.143
""" C optimizations for zope.interface """

# imports
import _interface_coptimizations as ___interface_coptimizations
import _zope_interface_coptimizations as ___zope_interface_coptimizations


# functions

def getObjectSpecification(*args, **kwargs): # real signature unknown
    """ Get an object's interfaces (internal api) """
    pass

def implementedBy(*args, **kwargs): # real signature unknown
    """
    Interfaces implemented by a class or factory.
    Raises TypeError if argument is neither a class nor a callable.
    """
    pass

def providedBy(*args, **kwargs): # real signature unknown
    """ Get an object's interfaces """
    pass

# classes

class SpecificationBase(object):
    """ Base type for Specification objects """
    def implementedBy(self, *args, **kwargs): # real signature unknown
        """
        Test whether the specification is implemented by a class or factory.
        Raise TypeError if argument is neither a class nor a callable.
        """
        pass

    def isOrExtends(self, *args, **kwargs): # real signature unknown
        """ Test whether a specification is or extends another """
        pass

    def providedBy(self, *args, **kwargs): # real signature unknown
        """ Test whether an interface is implemented by the specification """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ClassProvidesBase(___interface_coptimizations.SpecificationBase):
    """ C Base class for ClassProvides """
    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class InterfaceBase(object):
    """ Interface base type providing __call__ and __adapt__ """
    def __adapt__(self, *args, **kwargs): # real signature unknown
        """ Adapt an object to the reciever """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class LookupBase(object):
    # no doc
    def adapter_hook(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def lookup1(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def lookupAll(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def queryAdapter(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def subscriptions(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ObjectSpecificationDescriptor(object):
    """ Object Specification Descriptor """
    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class VerifyingBase(___zope_interface_coptimizations.LookupBase):
    # no doc
    def adapter_hook(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def lookup1(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def lookupAll(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def queryAdapter(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def subscriptions(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


# variables with complex values

adapter_hooks = []

