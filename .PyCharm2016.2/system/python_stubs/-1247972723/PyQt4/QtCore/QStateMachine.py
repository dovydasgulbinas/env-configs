# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QState import QState

class QStateMachine(QState):
    """ QStateMachine(QObject parent=None) """
    def addDefaultAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QStateMachine.addDefaultAnimation(QAbstractAnimation) """
        pass

    def addState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QStateMachine.addState(QAbstractState) """
        pass

    def cancelDelayedEvent(self, p_int): # real signature unknown; restored from __doc__
        """ QStateMachine.cancelDelayedEvent(int) -> bool """
        return False

    def clearError(self): # real signature unknown; restored from __doc__
        """ QStateMachine.clearError() """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ QStateMachine.configuration() -> list-of-QAbstractState """
        pass

    def defaultAnimations(self): # real signature unknown; restored from __doc__
        """ QStateMachine.defaultAnimations() -> list-of-QAbstractAnimation """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QStateMachine.error() -> QStateMachine.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QStateMachine.errorString() -> QString """
        return QString

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QStateMachine.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QStateMachine.eventFilter(QObject, QEvent) -> bool """
        return False

    def globalRestorePolicy(self): # real signature unknown; restored from __doc__
        """ QStateMachine.globalRestorePolicy() -> QStateMachine.RestorePolicy """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ QStateMachine.isAnimated() -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ QStateMachine.isRunning() -> bool """
        return False

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ QStateMachine.onEntry(QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ QStateMachine.onExit(QEvent) """
        pass

    def postDelayedEvent(self, QEvent, p_int): # real signature unknown; restored from __doc__
        """ QStateMachine.postDelayedEvent(QEvent, int) -> int """
        return 0

    def postEvent(self, QEvent, QStateMachine_EventPriority_priority=None): # real signature unknown; restored from __doc__
        """ QStateMachine.postEvent(QEvent, QStateMachine.EventPriority priority=QStateMachine.NormalPriority) """
        pass

    def removeDefaultAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QStateMachine.removeDefaultAnimation(QAbstractAnimation) """
        pass

    def removeState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QStateMachine.removeState(QAbstractState) """
        pass

    def setAnimated(self, bool): # real signature unknown; restored from __doc__
        """ QStateMachine.setAnimated(bool) """
        pass

    def setGlobalRestorePolicy(self, QStateMachine_RestorePolicy): # real signature unknown; restored from __doc__
        """ QStateMachine.setGlobalRestorePolicy(QStateMachine.RestorePolicy) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ QStateMachine.start() """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """ QStateMachine.started [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QStateMachine.stop() """
        pass

    def stopped(self, *args, **kwargs): # real signature unknown
        """ QStateMachine.stopped [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    DontRestoreProperties = 0
    HighPriority = 1
    NoCommonAncestorForTransitionError = 3
    NoDefaultStateInHistoryStateError = 2
    NoError = 0
    NoInitialStateError = 1
    NormalPriority = 0
    RestoreProperties = 1


