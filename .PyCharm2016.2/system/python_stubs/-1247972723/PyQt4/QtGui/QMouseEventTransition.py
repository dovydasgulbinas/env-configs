# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QMouseEventTransition(__PyQt4_QtCore.QEventTransition):
    """
    QMouseEventTransition(QState sourceState=None)
    QMouseEventTransition(QObject, QEvent.Type, Qt.MouseButton, QState sourceState=None)
    """
    def button(self): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.button() -> Qt.MouseButton """
        pass

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.eventTest(QEvent) -> bool """
        return False

    def hitTestPath(self): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.hitTestPath() -> QPainterPath """
        return QPainterPath

    def modifierMask(self): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.modifierMask() -> Qt.KeyboardModifiers """
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.onTransition(QEvent) """
        pass

    def setButton(self, Qt_MouseButton): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.setButton(Qt.MouseButton) """
        pass

    def setHitTestPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.setHitTestPath(QPainterPath) """
        pass

    def setModifierMask(self, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QMouseEventTransition.setModifierMask(Qt.KeyboardModifiers) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


