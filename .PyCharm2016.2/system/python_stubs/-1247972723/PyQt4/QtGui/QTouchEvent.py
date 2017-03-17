# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QInputEvent import QInputEvent

class QTouchEvent(QInputEvent):
    """
    QTouchEvent(QEvent.Type, QTouchEvent.DeviceType deviceType=QTouchEvent.TouchScreen, Qt.KeyboardModifiers modifiers=Qt.NoModifier, Qt.TouchPointStates touchPointStates=0, list-of-QTouchEvent.TouchPoint touchPoints=QList&lt;QTouchEvent.TouchPoint&gt;())
    QTouchEvent(QTouchEvent)
    """
    def deviceType(self): # real signature unknown; restored from __doc__
        """ QTouchEvent.deviceType() -> QTouchEvent.DeviceType """
        pass

    def touchPoints(self): # real signature unknown; restored from __doc__
        """ QTouchEvent.touchPoints() -> list-of-QTouchEvent.TouchPoint """
        pass

    def touchPointStates(self): # real signature unknown; restored from __doc__
        """ QTouchEvent.touchPointStates() -> Qt.TouchPointStates """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ QTouchEvent.widget() -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    TouchPad = 1
    TouchScreen = 0


