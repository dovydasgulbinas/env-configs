# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QKeyEventTransition(__PyQt4_QtCore.QEventTransition):
    """
    QKeyEventTransition(QState sourceState=None)
    QKeyEventTransition(QObject, QEvent.Type, int, QState sourceState=None)
    """
    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ QKeyEventTransition.eventTest(QEvent) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QKeyEventTransition.key() -> int """
        return 0

    def modifierMask(self): # real signature unknown; restored from __doc__
        """ QKeyEventTransition.modifierMask() -> Qt.KeyboardModifiers """
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ QKeyEventTransition.onTransition(QEvent) """
        pass

    def setKey(self, p_int): # real signature unknown; restored from __doc__
        """ QKeyEventTransition.setKey(int) """
        pass

    def setModifierMask(self, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QKeyEventTransition.setModifierMask(Qt.KeyboardModifiers) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


