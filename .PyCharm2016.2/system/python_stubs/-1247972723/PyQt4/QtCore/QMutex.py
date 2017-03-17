# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QMutex(): # skipped bases: <type 'sip.simplewrapper'>
    """ QMutex(QMutex.RecursionMode mode=QMutex.NonRecursive) """
    def lock(self): # real signature unknown; restored from __doc__
        """ QMutex.lock() """
        pass

    def tryLock(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMutex.tryLock() -> bool
        QMutex.tryLock(int) -> bool
        """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ QMutex.unlock() """
        pass

    def __init__(self, QMutex_RecursionMode_mode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NonRecursive = 0
    Recursive = 1


