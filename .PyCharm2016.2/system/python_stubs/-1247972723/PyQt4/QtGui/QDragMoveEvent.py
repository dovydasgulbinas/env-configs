# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDropEvent import QDropEvent

class QDragMoveEvent(QDropEvent):
    """
    QDragMoveEvent(QPoint, Qt.DropActions, QMimeData, Qt.MouseButtons, Qt.KeyboardModifiers, QEvent.Type type=QEvent.DragMove)
    QDragMoveEvent(QDragMoveEvent)
    """
    def accept(self, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDragMoveEvent.accept()
        QDragMoveEvent.accept(QRect)
        """
        pass

    def answerRect(self): # real signature unknown; restored from __doc__
        """ QDragMoveEvent.answerRect() -> QRect """
        pass

    def ignore(self, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDragMoveEvent.ignore()
        QDragMoveEvent.ignore(QRect)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


