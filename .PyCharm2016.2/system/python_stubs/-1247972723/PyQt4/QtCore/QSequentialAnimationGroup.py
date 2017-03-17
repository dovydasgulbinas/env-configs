# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QAnimationGroup import QAnimationGroup

class QSequentialAnimationGroup(QAnimationGroup):
    """ QSequentialAnimationGroup(QObject parent=None) """
    def addPause(self, p_int): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.addPause(int) -> QPauseAnimation """
        return QPauseAnimation

    def currentAnimation(self): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.currentAnimation() -> QAbstractAnimation """
        return QAbstractAnimation

    def currentAnimationChanged(self, *args, **kwargs): # real signature unknown
        """ QSequentialAnimationGroup.currentAnimationChanged[QAbstractAnimation] [signal] """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.duration() -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.event(QEvent) -> bool """
        return False

    def insertPause(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.insertPause(int, int) -> QPauseAnimation """
        return QPauseAnimation

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.updateCurrentTime(int) """
        pass

    def updateDirection(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.updateDirection(QAbstractAnimation.Direction) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ QSequentialAnimationGroup.updateState(QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


