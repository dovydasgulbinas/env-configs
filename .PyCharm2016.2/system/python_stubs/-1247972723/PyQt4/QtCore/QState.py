# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractState import QAbstractState

class QState(QAbstractState):
    """
    QState(QState parent=None)
    QState(QState.ChildMode, QState parent=None)
    """
    def addTransition(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QState.addTransition(QAbstractTransition)
        QState.addTransition(QObject, SIGNAL(), QAbstractState) -> QSignalTransition
        QState.addTransition(signal, QAbstractState) -> QSignalTransition
        QState.addTransition(QAbstractState) -> QAbstractTransition
        """
        return QSignalTransition or QAbstractTransition

    def assignProperty(self, QObject, p_str, QVariant): # real signature unknown; restored from __doc__
        """ QState.assignProperty(QObject, str, QVariant) """
        pass

    def childMode(self): # real signature unknown; restored from __doc__
        """ QState.childMode() -> QState.ChildMode """
        pass

    def errorState(self): # real signature unknown; restored from __doc__
        """ QState.errorState() -> QAbstractState """
        return QAbstractState

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QState.event(QEvent) -> bool """
        return False

    def finished(self, *args, **kwargs): # real signature unknown
        """ QState.finished [signal] """
        pass

    def initialState(self): # real signature unknown; restored from __doc__
        """ QState.initialState() -> QAbstractState """
        return QAbstractState

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ QState.onEntry(QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ QState.onExit(QEvent) """
        pass

    def propertiesAssigned(self, *args, **kwargs): # real signature unknown
        """ QState.propertiesAssigned [signal] """
        pass

    def removeTransition(self, QAbstractTransition): # real signature unknown; restored from __doc__
        """ QState.removeTransition(QAbstractTransition) """
        pass

    def setChildMode(self, QState_ChildMode): # real signature unknown; restored from __doc__
        """ QState.setChildMode(QState.ChildMode) """
        pass

    def setErrorState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QState.setErrorState(QAbstractState) """
        pass

    def setInitialState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QState.setInitialState(QAbstractState) """
        pass

    def transitions(self): # real signature unknown; restored from __doc__
        """ QState.transitions() -> list-of-QAbstractTransition """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ExclusiveStates = 0
    ParallelStates = 1


