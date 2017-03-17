# encoding: utf-8
# module gevent._semaphore
# from /opt/odoo/_venv/local/lib/python2.7/site-packages/gevent/_semaphore.so
# by generator 1.143
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>
from greenlet import getcurrent


# functions

def get_hub(*args, **kwargs): # reliably restored by inspect
    """
    Return the hub for the current thread.
    
        If hub does not exists in the current thread, the new one is created with call to :meth:`get_hub_class`.
    """
    pass

# classes

class Semaphore(object):
    """
    A semaphore manages a counter representing the number of release() calls minus the number of acquire() calls,
        plus an initial value. The acquire() method blocks if necessary until it can return without making the counter
        negative.
    
        If not given, value defaults to 1.
    
        This Semaphore's __exit__ method does not call the trace function.
    """
    def acquire(self, *args, **kwargs): # real signature unknown
        pass

    def locked(self, *args, **kwargs): # real signature unknown
        pass

    def rawlink(self, *args, **kwargs): # real signature unknown
        """
        Register a callback to call when a counter is more than zero.
        
                *callback* will be called in the :class:`Hub <gevent.hub.Hub>`, so it must not use blocking gevent API.
                *callback* will be passed one argument: this instance.
        """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def unlink(self, *args, **kwargs): # real signature unknown
        """ Remove the callback set by :meth:`rawlink` """
        pass

    def wait(self, *args, **kwargs): # real signature unknown
        pass

    def _notify_links(self, *args, **kwargs): # real signature unknown
        pass

    def _start_notify(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __qualname__ = 'Semaphore'


class Timeout(BaseException):
    """
    Raise *exception* in the current greenlet after given time period::
    
            timeout = Timeout(seconds, exception)
            timeout.start()
            try:
                ...  # exception will be raised here, after *seconds* passed since start() call
            finally:
                timeout.cancel()
    
        When *exception* is omitted or ``None``, the :class:`Timeout` instance itself is raised:
    
            >>> import gevent
            >>> gevent.Timeout(0.1).start()
            >>> gevent.sleep(0.2)
            Traceback (most recent call last):
             ...
            Timeout: 0.1 seconds
    
        For Python 2.5 and newer ``with`` statement can be used::
    
            with gevent.Timeout(seconds, exception) as timeout:
                pass  # ... code block ...
    
        This is equivalent to try/finally block above with one additional feature:
        if *exception* is ``False``, the timeout is still raised, but context manager
        suppresses it, so the code outside the with-block won't see it.
    
        This is handy for adding a timeout to the functions that don't support *timeout* parameter themselves::
    
            data = None
            with gevent.Timeout(5, False):
                data = mysock.makefile().readline()
            if data is None:
                ...  # 5 seconds passed without reading a line
            else:
                ...  # a line was read within 5 seconds
    
        Note that, if ``readline()`` above catches and doesn't re-raise :class:`BaseException`
        (for example, with ``except:``), then your timeout is screwed.
    
        When catching timeouts, keep in mind that the one you catch maybe not the
        one you have set; if you going to silent a timeout, always check that it's
        the one you need::
    
            timeout = Timeout(1)
            timeout.start()
            try:
                ...
            except Timeout, t:
                if t is not timeout:
                    raise # not my timeout
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        """ If the timeout is pending, cancel it. Otherwise, do nothing. """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        """ Schedule the timeout. """
        pass

    @classmethod
    def start_new(cls, *args, **kwargs): # real signature unknown
        """
        Create a started :class:`Timeout`.
        
                This is a shortcut, the exact action depends on *timeout*'s type:
        
                * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method.
                * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
                  arguments, then call its :meth:`start` method.
        
                Returns the :class:`Timeout` instance.
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """
        >>> raise Timeout
                Traceback (most recent call last):
                    ...
                Timeout
        """
        pass

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return True if the timeout is scheduled to be raised."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    'Semaphore',
]

__test__ = {}

