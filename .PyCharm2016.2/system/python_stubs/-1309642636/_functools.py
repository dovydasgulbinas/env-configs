# encoding: utf-8
# module _functools
# from (built-in)
# by generator 1.143
""" Tools that operate on functions. """
# no imports

# functions

def reduce(function, sequence, initial=None): # real signature unknown; restored from __doc__
    """
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    """
    pass

# classes

class partial(object):
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, func, *args, **keywords): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of arguments to future partial calls"""

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """function object to use in future partial calls"""

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dictionary of keyword arguments to future partial calls"""


    __dict__ = None # (!) real value is ''


