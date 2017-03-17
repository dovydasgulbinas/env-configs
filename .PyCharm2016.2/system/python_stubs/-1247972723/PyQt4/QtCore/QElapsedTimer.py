# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QElapsedTimer(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QElapsedTimer()
    QElapsedTimer(QElapsedTimer)
    """
    def clockType(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.clockType() -> QElapsedTimer.ClockType """
        pass

    def elapsed(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.elapsed() -> int """
        return 0

    def hasExpired(self, p_int): # real signature unknown; restored from __doc__
        """ QElapsedTimer.hasExpired(int) -> bool """
        return False

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.invalidate() """
        pass

    def isMonotonic(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.isMonotonic() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.isValid() -> bool """
        return False

    def msecsSinceReference(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.msecsSinceReference() -> int """
        return 0

    def msecsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ QElapsedTimer.msecsTo(QElapsedTimer) -> int """
        return 0

    def nsecsElapsed(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.nsecsElapsed() -> int """
        return 0

    def restart(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.restart() -> int """
        return 0

    def secsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ QElapsedTimer.secsTo(QElapsedTimer) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.start() """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, QElapsedTimer=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MachAbsoluteTime = 3
    MonotonicClock = 1
    PerformanceCounter = 4
    SystemTime = 0
    TickCounter = 2


