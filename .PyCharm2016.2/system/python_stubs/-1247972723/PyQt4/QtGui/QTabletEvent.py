# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QInputEvent import QInputEvent

class QTabletEvent(QInputEvent):
    """
    QTabletEvent(QEvent.Type, QPoint, QPoint, QPointF, int, int, float, int, int, float, float, int, Qt.KeyboardModifiers, int)
    QTabletEvent(QTabletEvent)
    """
    def device(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.device() -> QTabletEvent.TabletDevice """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.globalPos() -> QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.globalX() -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.globalY() -> int """
        return 0

    def hiResGlobalPos(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.hiResGlobalPos() -> QPointF """
        pass

    def hiResGlobalX(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.hiResGlobalX() -> float """
        return 0.0

    def hiResGlobalY(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.hiResGlobalY() -> float """
        return 0.0

    def pointerType(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.pointerType() -> QTabletEvent.PointerType """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.pos() -> QPoint """
        pass

    def pressure(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.pressure() -> float """
        return 0.0

    def rotation(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.rotation() -> float """
        return 0.0

    def tangentialPressure(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.tangentialPressure() -> float """
        return 0.0

    def uniqueId(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.uniqueId() -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.x() -> int """
        return 0

    def xTilt(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.xTilt() -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.y() -> int """
        return 0

    def yTilt(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.yTilt() -> int """
        return 0

    def z(self): # real signature unknown; restored from __doc__
        """ QTabletEvent.z() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Airbrush = 3
    Cursor = 2
    Eraser = 3
    FourDMouse = 4
    NoDevice = 0
    Pen = 1
    Puck = 1
    RotationStylus = 6
    Stylus = 2
    UnknownPointer = 0
    XFreeEraser = 5


