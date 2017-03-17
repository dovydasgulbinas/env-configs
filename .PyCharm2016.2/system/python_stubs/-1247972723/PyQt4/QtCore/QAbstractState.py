# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractState(QObject):
    """ QAbstractState(QState parent=None) """
    def entered(self, *args, **kwargs): # real signature unknown
        """ QAbstractState.entered [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractState.event(QEvent) -> bool """
        return False

    def exited(self, *args, **kwargs): # real signature unknown
        """ QAbstractState.exited [signal] """
        pass

    def machine(self): # real signature unknown; restored from __doc__
        """ QAbstractState.machine() -> QStateMachine """
        return QStateMachine

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractState.onEntry(QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractState.onExit(QEvent) """
        pass

    def parentState(self): # real signature unknown; restored from __doc__
        """ QAbstractState.parentState() -> QState """
        return QState

    def __init__(self, QState_parent=None): # real signature unknown; restored from __doc__
        pass


