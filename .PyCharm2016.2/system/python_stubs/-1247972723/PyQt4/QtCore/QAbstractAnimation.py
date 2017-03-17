# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractAnimation(QObject):
    """ QAbstractAnimation(QObject parent=None) """
    def currentLoop(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.currentLoop() -> int """
        return 0

    def currentLoopChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractAnimation.currentLoopChanged[int] [signal] """
        pass

    def currentLoopTime(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.currentLoopTime() -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.currentTime() -> int """
        return 0

    def direction(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.direction() -> QAbstractAnimation.Direction """
        pass

    def directionChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractAnimation.directionChanged[QAbstractAnimation.Direction] [signal] """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.duration() -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.event(QEvent) -> bool """
        return False

    def finished(self, *args, **kwargs): # real signature unknown
        """ QAbstractAnimation.finished [signal] """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.group() -> QAnimationGroup """
        return QAnimationGroup

    def loopCount(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.loopCount() -> int """
        return 0

    def pause(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.pause() """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.resume() """
        pass

    def setCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.setCurrentTime(int) """
        pass

    def setDirection(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.setDirection(QAbstractAnimation.Direction) """
        pass

    def setLoopCount(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.setLoopCount(int) """
        pass

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.setPaused(bool) """
        pass

    def start(self, QAbstractAnimation_DeletionPolicy_policy=None): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.start(QAbstractAnimation.DeletionPolicy policy=QAbstractAnimation.KeepWhenStopped) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.state() -> QAbstractAnimation.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractAnimation.stateChanged[QAbstractAnimation.State, QAbstractAnimation.State] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.stop() """
        pass

    def totalDuration(self): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.totalDuration() -> int """
        return 0

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.updateCurrentTime(int) """
        pass

    def updateDirection(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.updateDirection(QAbstractAnimation.Direction) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ QAbstractAnimation.updateState(QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Backward = 1
    DeleteWhenStopped = 1
    Forward = 0
    KeepWhenStopped = 0
    Paused = 1
    Running = 2
    Stopped = 0


