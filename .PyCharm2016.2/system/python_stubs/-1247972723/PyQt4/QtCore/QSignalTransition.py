# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractTransition import QAbstractTransition

class QSignalTransition(QAbstractTransition):
    """
    QSignalTransition(QState sourceState=None)
    QSignalTransition(QObject, SIGNAL(), QState sourceState=None)
    QSignalTransition(signal, QState sourceState=None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSignalTransition.event(QEvent) -> bool """
        return False

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ QSignalTransition.eventTest(QEvent) -> bool """
        return False

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ QSignalTransition.onTransition(QEvent) """
        pass

    def senderObject(self): # real signature unknown; restored from __doc__
        """ QSignalTransition.senderObject() -> QObject """
        return QObject

    def setSenderObject(self, QObject): # real signature unknown; restored from __doc__
        """ QSignalTransition.setSenderObject(QObject) """
        pass

    def setSignal(self, QByteArray): # real signature unknown; restored from __doc__
        """ QSignalTransition.setSignal(QByteArray) """
        pass

    def signal(self): # real signature unknown; restored from __doc__
        """ QSignalTransition.signal() -> QByteArray """
        return QByteArray

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


