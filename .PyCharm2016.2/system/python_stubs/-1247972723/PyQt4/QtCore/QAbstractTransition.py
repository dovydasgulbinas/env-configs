# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractTransition(QObject):
    """ QAbstractTransition(QState sourceState=None) """
    def addAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QAbstractTransition.addAnimation(QAbstractAnimation) """
        pass

    def animations(self): # real signature unknown; restored from __doc__
        """ QAbstractTransition.animations() -> list-of-QAbstractAnimation """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractTransition.event(QEvent) -> bool """
        return False

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractTransition.eventTest(QEvent) -> bool """
        return False

    def machine(self): # real signature unknown; restored from __doc__
        """ QAbstractTransition.machine() -> QStateMachine """
        return QStateMachine

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractTransition.onTransition(QEvent) """
        pass

    def removeAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QAbstractTransition.removeAnimation(QAbstractAnimation) """
        pass

    def setTargetState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ QAbstractTransition.setTargetState(QAbstractState) """
        pass

    def setTargetStates(self, list_of_QAbstractState): # real signature unknown; restored from __doc__
        """ QAbstractTransition.setTargetStates(list-of-QAbstractState) """
        pass

    def sourceState(self): # real signature unknown; restored from __doc__
        """ QAbstractTransition.sourceState() -> QState """
        return QState

    def targetState(self): # real signature unknown; restored from __doc__
        """ QAbstractTransition.targetState() -> QAbstractState """
        return QAbstractState

    def targetStates(self): # real signature unknown; restored from __doc__
        """ QAbstractTransition.targetStates() -> list-of-QAbstractState """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        """ QAbstractTransition.triggered [signal] """
        pass

    def __init__(self, QState_sourceState=None): # real signature unknown; restored from __doc__
        pass


