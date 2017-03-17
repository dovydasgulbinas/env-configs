# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QCursor(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QCursor()
    QCursor(Qt.CursorShape)
    QCursor(QBitmap, QBitmap, int hotX=-1, int hotY=-1)
    QCursor(QPixmap, int hotX=-1, int hotY=-1)
    QCursor(QCursor)
    QCursor(QVariant)
    """
    def bitmap(self): # real signature unknown; restored from __doc__
        """ QCursor.bitmap() -> QBitmap """
        return QBitmap

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ QCursor.hotSpot() -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ QCursor.mask() -> QBitmap """
        return QBitmap

    def pixmap(self): # real signature unknown; restored from __doc__
        """ QCursor.pixmap() -> QPixmap """
        return QPixmap

    def pos(self): # real signature unknown; restored from __doc__
        """ QCursor.pos() -> QPoint """
        pass

    def setPos(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCursor.setPos(int, int)
        QCursor.setPos(QPoint)
        """
        pass

    def setShape(self, Qt_CursorShape): # real signature unknown; restored from __doc__
        """ QCursor.setShape(Qt.CursorShape) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QCursor.shape() -> Qt.CursorShape """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



