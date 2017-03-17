# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsRectItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsRectItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsRectItem(QRectF, QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsRectItem(float, float, float, float, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.contains(QPointF) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.rect() -> QRectF """
        pass

    def setRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsRectItem.setRect(QRectF)
        QGraphicsRectItem.setRect(float, float, float, float)
        """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.shape() -> QPainterPath """
        return QPainterPath

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsRectItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


