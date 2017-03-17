# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGesture import QGesture

class QSwipeGesture(QGesture):
    """ QSwipeGesture(QObject parent=None) """
    def horizontalDirection(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.horizontalDirection() -> QSwipeGesture.SwipeDirection """
        pass

    def setSwipeAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QSwipeGesture.setSwipeAngle(float) """
        pass

    def swipeAngle(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.swipeAngle() -> float """
        return 0.0

    def verticalDirection(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.verticalDirection() -> QSwipeGesture.SwipeDirection """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Down = 4
    Left = 1
    NoDirection = 0
    Right = 2
    Up = 3


