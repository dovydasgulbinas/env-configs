# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractState import QAbstractState

class QHistoryState(QAbstractState):
    """
    QHistoryState(QState parent=None)
    QHistoryState(QHistoryState.HistoryType, QState parent=None)
    """
    def defaultState(self): # real signature unknown; restored from __doc__
        """ QHistoryState.defaultState() -> QAbstractState """
        return QAbstractState

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QHistoryState.event(QEvent) -> bool """
        return False

    def historyType(self): # real signature unknown; restored from __doc__
        """ QHistoryState.historyType() -> QHistoryState.HistoryType """
        pass

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ QHistoryState.onEntry(QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ QHistoryState.onExit(QEvent) """
        pass

    def setDefaultState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QHistoryState.setDefaultState(QAbstractState) """
        pass

    def setHistoryType(self, QHistoryState_HistoryType): # real signature unknown; restored from __doc__
        """ QHistoryState.setHistoryType(QHistoryState.HistoryType) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DeepHistory = 1
    ShallowHistory = 0


