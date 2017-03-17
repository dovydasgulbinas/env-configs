# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(QState sourceState=None)
    QEventTransition(QObject, QEvent.Type, QState sourceState=None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QEventTransition.event(QEvent) -> bool """
        return False

    def eventSource(self): # real signature unknown; restored from __doc__
        """ QEventTransition.eventSource() -> QObject """
        return QObject

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ QEventTransition.eventTest(QEvent) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ QEventTransition.eventType() -> QEvent.Type """
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ QEventTransition.onTransition(QEvent) """
        pass

    def setEventSource(self, QObject): # real signature unknown; restored from __doc__
        """ QEventTransition.setEventSource(QObject) """
        pass

    def setEventType(self, QEvent_Type): # real signature unknown; restored from __doc__
        """ QEventTransition.setEventType(QEvent.Type) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


