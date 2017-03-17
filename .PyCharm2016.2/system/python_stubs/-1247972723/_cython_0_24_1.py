# encoding: utf-8
# module _cython_0_24_1
# from /usr/local/lib/python2.7/dist-packages/gevent/corecext.so
# by generator 1.143
# no doc
# no imports

# no functions
# classes

class generator(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside generator. """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def throw(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """
        throw(typ[,val[,tb]]) -> raise exception in generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    gi_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_yieldfrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being iterated by 'yield from', or None"""

    __qualname__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """qualified name of the generator"""


    __name__ = 'generator'


