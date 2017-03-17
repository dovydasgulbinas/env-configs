# encoding: utf-8
# module twisted.test.raiser
# from /usr/lib/python2.7/dist-packages/twisted/test/raiser.x86_64-linux-gnu.so
# by generator 1.143
"""
A trivial extension that just raises an exception.
See L{twisted.test.test_failure.test_failureConstructionWithMungedStackSucceeds}.
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# functions

def raiseException(*args, **kwargs): # real signature unknown
    """ Raise L{RaiserException}. """
    pass

# classes

class RaiserException(Exception):
    """ A speficic exception only used to be identified in tests. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__test__ = {}

