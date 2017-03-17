# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAbstractAnimation import QAbstractAnimation

class QAnimationGroup(QAbstractAnimation):
    """ QAnimationGroup(QObject parent=None) """
    def addAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QAnimationGroup.addAnimation(QAbstractAnimation) """
        pass

    def animationAt(self, p_int): # real signature unknown; restored from __doc__
        """ QAnimationGroup.animationAt(int) -> QAbstractAnimation """
        return QAbstractAnimation

    def animationCount(self): # real signature unknown; restored from __doc__
        """ QAnimationGroup.animationCount() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QAnimationGroup.clear() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAnimationGroup.event(QEvent) -> bool """
        return False

    def indexOfAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QAnimationGroup.indexOfAnimation(QAbstractAnimation) -> int """
        return 0

    def insertAnimation(self, p_int, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QAnimationGroup.insertAnimation(int, QAbstractAnimation) """
        pass

    def removeAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ QAnimationGroup.removeAnimation(QAbstractAnimation) """
        pass

    def takeAnimation(self, p_int): # real signature unknown; restored from __doc__
        """ QAnimationGroup.takeAnimation(int) -> QAbstractAnimation """
        return QAbstractAnimation

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


