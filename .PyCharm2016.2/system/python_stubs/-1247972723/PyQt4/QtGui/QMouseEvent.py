# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QInputEvent import QInputEvent

class QMouseEvent(QInputEvent):
    """
    QMouseEvent(QEvent.Type, QPoint, Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers)
    QMouseEvent(QEvent.Type, QPoint, QPoint, Qt.MouseButton, Qt.MouseButtons, Qt.KeyboardModifiers)
    QMouseEvent(QMouseEvent)
    """
    def button(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.button() -> Qt.MouseButton """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.buttons() -> Qt.MouseButtons """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.globalPos() -> QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.globalX() -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.globalY() -> int """
        return 0

    def hasExtendedInfo(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.hasExtendedInfo() -> bool """
        return False

    def pos(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.pos() -> QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.posF() -> QPointF """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.x() -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ QMouseEvent.y() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


