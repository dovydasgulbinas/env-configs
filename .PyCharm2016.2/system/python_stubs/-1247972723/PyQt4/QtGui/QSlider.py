# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractSlider import QAbstractSlider

class QSlider(QAbstractSlider):
    """
    QSlider(QWidget parent=None)
    QSlider(Qt.Orientation, QWidget parent=None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSlider.event(QEvent) -> bool """
        return False

    def initStyleOption(self, QStyleOptionSlider): # real signature unknown; restored from __doc__
        """ QSlider.initStyleOption(QStyleOptionSlider) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QSlider.minimumSizeHint() -> QSize """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QSlider.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QSlider.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QSlider.mouseReleaseEvent(QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QSlider.paintEvent(QPaintEvent) """
        pass

    def setTickInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QSlider.setTickInterval(int) """
        pass

    def setTickPosition(self, QSlider_TickPosition): # real signature unknown; restored from __doc__
        """ QSlider.setTickPosition(QSlider.TickPosition) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QSlider.sizeHint() -> QSize """
        pass

    def tickInterval(self): # real signature unknown; restored from __doc__
        """ QSlider.tickInterval() -> int """
        return 0

    def tickPosition(self): # real signature unknown; restored from __doc__
        """ QSlider.tickPosition() -> QSlider.TickPosition """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoTicks = 0
    TicksAbove = 1
    TicksBelow = 2
    TicksBothSides = 3
    TicksLeft = 1
    TicksRight = 2


