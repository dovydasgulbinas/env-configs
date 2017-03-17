# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QInputEvent import QInputEvent

class QContextMenuEvent(QInputEvent):
    """
    QContextMenuEvent(QContextMenuEvent.Reason, QPoint, QPoint, Qt.KeyboardModifiers)
    QContextMenuEvent(QContextMenuEvent.Reason, QPoint, QPoint)
    QContextMenuEvent(QContextMenuEvent.Reason, QPoint)
    QContextMenuEvent(QContextMenuEvent)
    """
    def globalPos(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.globalPos() -> QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.globalX() -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.globalY() -> int """
        return 0

    def pos(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.pos() -> QPoint """
        pass

    def reason(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.reason() -> QContextMenuEvent.Reason """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.x() -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ QContextMenuEvent.y() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Keyboard = 1
    Mouse = 0
    Other = 2


