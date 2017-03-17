# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QVariantAnimation import QVariantAnimation

class QPropertyAnimation(QVariantAnimation):
    """
    QPropertyAnimation(QObject parent=None)
    QPropertyAnimation(QObject, QByteArray, QObject parent=None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.event(QEvent) -> bool """
        return False

    def propertyName(self): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.propertyName() -> QByteArray """
        return QByteArray

    def setPropertyName(self, QByteArray): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.setPropertyName(QByteArray) """
        pass

    def setTargetObject(self, QObject): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.setTargetObject(QObject) """
        pass

    def targetObject(self): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.targetObject() -> QObject """
        return QObject

    def updateCurrentValue(self, QVariant): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.updateCurrentValue(QVariant) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ QPropertyAnimation.updateState(QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


