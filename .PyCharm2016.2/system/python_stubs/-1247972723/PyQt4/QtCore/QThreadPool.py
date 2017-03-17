# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QThreadPool(QObject):
    """ QThreadPool(QObject parent=None) """
    def activeThreadCount(self): # real signature unknown; restored from __doc__
        """ QThreadPool.activeThreadCount() -> int """
        return 0

    def expiryTimeout(self): # real signature unknown; restored from __doc__
        """ QThreadPool.expiryTimeout() -> int """
        return 0

    def globalInstance(self): # real signature unknown; restored from __doc__
        """ QThreadPool.globalInstance() -> QThreadPool """
        return QThreadPool

    def maxThreadCount(self): # real signature unknown; restored from __doc__
        """ QThreadPool.maxThreadCount() -> int """
        return 0

    def releaseThread(self): # real signature unknown; restored from __doc__
        """ QThreadPool.releaseThread() """
        pass

    def reserveThread(self): # real signature unknown; restored from __doc__
        """ QThreadPool.reserveThread() """
        pass

    def setExpiryTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ QThreadPool.setExpiryTimeout(int) """
        pass

    def setMaxThreadCount(self, p_int): # real signature unknown; restored from __doc__
        """ QThreadPool.setMaxThreadCount(int) """
        pass

    def start(self, QRunnable, int_priority=0): # real signature unknown; restored from __doc__
        """ QThreadPool.start(QRunnable, int priority=0) """
        pass

    def tryStart(self, QRunnable): # real signature unknown; restored from __doc__
        """ QThreadPool.tryStart(QRunnable) -> bool """
        return False

    def waitForDone(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QThreadPool.waitForDone()
        QThreadPool.waitForDone(int) -> bool
        """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


