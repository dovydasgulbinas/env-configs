# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QReadLocker(): # skipped bases: <type 'sip.simplewrapper'>
    """ QReadLocker(QReadWriteLock) """
    def readWriteLock(self): # real signature unknown; restored from __doc__
        """ QReadLocker.readWriteLock() -> QReadWriteLock """
        return QReadWriteLock

    def relock(self): # real signature unknown; restored from __doc__
        """ QReadLocker.relock() """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ QReadLocker.unlock() """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ QReadLocker.__enter__() -> object """
        return object()

    def __exit__(self, p_object, p_object_1, p_object_2): # real signature unknown; restored from __doc__
        """ QReadLocker.__exit__(object, object, object) """
        pass

    def __init__(self, QReadWriteLock): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



