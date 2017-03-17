# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGestureEvent(__PyQt4_QtCore.QEvent):
    """
    QGestureEvent(list-of-QGesture)
    QGestureEvent(QGestureEvent)
    """
    def accept(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGestureEvent.accept()
        QGestureEvent.accept(QGesture)
        QGestureEvent.accept(Qt.GestureType)
        """
        pass

    def activeGestures(self): # real signature unknown; restored from __doc__
        """ QGestureEvent.activeGestures() -> list-of-QGesture """
        pass

    def canceledGestures(self): # real signature unknown; restored from __doc__
        """ QGestureEvent.canceledGestures() -> list-of-QGesture """
        pass

    def gesture(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ QGestureEvent.gesture(Qt.GestureType) -> QGesture """
        return QGesture

    def gestures(self): # real signature unknown; restored from __doc__
        """ QGestureEvent.gestures() -> list-of-QGesture """
        pass

    def ignore(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGestureEvent.ignore()
        QGestureEvent.ignore(QGesture)
        QGestureEvent.ignore(Qt.GestureType)
        """
        pass

    def isAccepted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGestureEvent.isAccepted() -> bool
        QGestureEvent.isAccepted(QGesture) -> bool
        QGestureEvent.isAccepted(Qt.GestureType) -> bool
        """
        return False

    def mapToGraphicsScene(self, QPointF): # real signature unknown; restored from __doc__
        """ QGestureEvent.mapToGraphicsScene(QPointF) -> QPointF """
        pass

    def setAccepted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGestureEvent.setAccepted(bool)
        QGestureEvent.setAccepted(QGesture, bool)
        QGestureEvent.setAccepted(Qt.GestureType, bool)
        """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ QGestureEvent.widget() -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


