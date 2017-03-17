# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QWaitCondition(): # skipped bases: <type 'sip.simplewrapper'>
    """ QWaitCondition() """
    def wait(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWaitCondition.wait(QMutex, int msecs=ULONG_MAX) -> bool
        QWaitCondition.wait(QReadWriteLock, int msecs=ULONG_MAX) -> bool
        """
        return False

    def wakeAll(self): # real signature unknown; restored from __doc__
        """ QWaitCondition.wakeAll() """
        pass

    def wakeOne(self): # real signature unknown; restored from __doc__
        """ QWaitCondition.wakeOne() """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



