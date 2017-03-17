# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QTimeLine(QObject):
    """ QTimeLine(int duration=1000, QObject parent=None) """
    def currentFrame(self): # real signature unknown; restored from __doc__
        """ QTimeLine.currentFrame() -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ QTimeLine.currentTime() -> int """
        return 0

    def currentValue(self): # real signature unknown; restored from __doc__
        """ QTimeLine.currentValue() -> float """
        return 0.0

    def curveShape(self): # real signature unknown; restored from __doc__
        """ QTimeLine.curveShape() -> QTimeLine.CurveShape """
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ QTimeLine.direction() -> QTimeLine.Direction """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ QTimeLine.duration() -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ QTimeLine.easingCurve() -> QEasingCurve """
        return QEasingCurve

    def endFrame(self): # real signature unknown; restored from __doc__
        """ QTimeLine.endFrame() -> int """
        return 0

    def finished(self, *args, **kwargs): # real signature unknown
        """ QTimeLine.finished [signal] """
        pass

    def frameChanged(self, *args, **kwargs): # real signature unknown
        """ QTimeLine.frameChanged[int] [signal] """
        pass

    def frameForTime(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.frameForTime(int) -> int """
        return 0

    def loopCount(self): # real signature unknown; restored from __doc__
        """ QTimeLine.loopCount() -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ QTimeLine.resume() """
        pass

    def setCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.setCurrentTime(int) """
        pass

    def setCurveShape(self, QTimeLine_CurveShape): # real signature unknown; restored from __doc__
        """ QTimeLine.setCurveShape(QTimeLine.CurveShape) """
        pass

    def setDirection(self, QTimeLine_Direction): # real signature unknown; restored from __doc__
        """ QTimeLine.setDirection(QTimeLine.Direction) """
        pass

    def setDuration(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.setDuration(int) """
        pass

    def setEasingCurve(self, QEasingCurve): # real signature unknown; restored from __doc__
        """ QTimeLine.setEasingCurve(QEasingCurve) """
        pass

    def setEndFrame(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.setEndFrame(int) """
        pass

    def setFrameRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTimeLine.setFrameRange(int, int) """
        pass

    def setLoopCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.setLoopCount(int) """
        pass

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ QTimeLine.setPaused(bool) """
        pass

    def setStartFrame(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.setStartFrame(int) """
        pass

    def setUpdateInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.setUpdateInterval(int) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ QTimeLine.start() """
        pass

    def startFrame(self): # real signature unknown; restored from __doc__
        """ QTimeLine.startFrame() -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ QTimeLine.state() -> QTimeLine.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QTimeLine.stateChanged[QTimeLine.State] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QTimeLine.stop() """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QTimeLine.timerEvent(QTimerEvent) """
        pass

    def toggleDirection(self): # real signature unknown; restored from __doc__
        """ QTimeLine.toggleDirection() """
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ QTimeLine.updateInterval() -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ QTimeLine.valueChanged[float] [signal] """
        pass

    def valueForTime(self, p_int): # real signature unknown; restored from __doc__
        """ QTimeLine.valueForTime(int) -> float """
        return 0.0

    def __init__(self, int_duration=1000, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Backward = 1
    CosineCurve = 5
    EaseInCurve = 0
    EaseInOutCurve = 2
    EaseOutCurve = 1
    Forward = 0
    LinearCurve = 3
    NotRunning = 0
    Paused = 1
    Running = 2
    SineCurve = 4


