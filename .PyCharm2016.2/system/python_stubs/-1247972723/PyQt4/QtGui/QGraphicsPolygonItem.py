# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsPolygonItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsPolygonItem(QPolygonF, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.contains(QPointF) -> bool """
        return False

    def fillRule(self): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.fillRule() -> Qt.FillRule """
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def polygon(self): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.polygon() -> QPolygonF """
        return QPolygonF

    def setFillRule(self, Qt_FillRule): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.setFillRule(Qt.FillRule) """
        pass

    def setPolygon(self, QPolygonF): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.setPolygon(QPolygonF) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.shape() -> QPainterPath """
        return QPainterPath

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsPolygonItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


