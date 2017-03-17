# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractEventDispatcher(QObject):
    """ QAbstractEventDispatcher(QObject parent=None) """
    def aboutToBlock(self, *args, **kwargs): # real signature unknown
        """ QAbstractEventDispatcher.aboutToBlock [signal] """
        pass

    def awake(self, *args, **kwargs): # real signature unknown
        """ QAbstractEventDispatcher.awake [signal] """
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.closingDown() """
        pass

    def filterEvent(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.filterEvent(sip.voidptr) -> bool """
        return False

    def flush(self): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.flush() """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.hasPendingEvents() -> bool """
        return False

    def instance(self, QThread_thread=None): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.instance(QThread thread=None) -> QAbstractEventDispatcher """
        return QAbstractEventDispatcher

    def interrupt(self): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.interrupt() """
        pass

    def processEvents(self, QEventLoop_ProcessEventsFlags): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.processEvents(QEventLoop.ProcessEventsFlags) -> bool """
        return False

    def registeredTimers(self, QObject): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.registeredTimers(QObject) -> list-of-tuple-of-int-int """
        pass

    def registerSocketNotifier(self, QSocketNotifier): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.registerSocketNotifier(QSocketNotifier) """
        pass

    def registerTimer(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractEventDispatcher.registerTimer(int, QObject) -> int
        QAbstractEventDispatcher.registerTimer(int, int, QObject)
        """
        return 0

    def setEventFilter(self, callable): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.setEventFilter(callable) -> callable """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.startingUp() """
        pass

    def unregisterSocketNotifier(self, QSocketNotifier): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.unregisterSocketNotifier(QSocketNotifier) """
        pass

    def unregisterTimer(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.unregisterTimer(int) -> bool """
        return False

    def unregisterTimers(self, QObject): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.unregisterTimers(QObject) -> bool """
        return False

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ QAbstractEventDispatcher.wakeUp() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


