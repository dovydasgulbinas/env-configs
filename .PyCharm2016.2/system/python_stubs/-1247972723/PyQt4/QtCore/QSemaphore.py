# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QSemaphore(): # skipped bases: <type 'sip.simplewrapper'>
    """ QSemaphore(int n=0) """
    def acquire(self, int_n=1): # real signature unknown; restored from __doc__
        """ QSemaphore.acquire(int n=1) """
        pass

    def available(self): # real signature unknown; restored from __doc__
        """ QSemaphore.available() -> int """
        return 0

    def release(self, int_n=1): # real signature unknown; restored from __doc__
        """ QSemaphore.release(int n=1) """
        pass

    def tryAcquire(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSemaphore.tryAcquire(int n=1) -> bool
        QSemaphore.tryAcquire(int, int) -> bool
        """
        return False

    def __init__(self, int_n=0): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



