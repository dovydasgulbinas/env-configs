# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsItem import QGraphicsItem

class QGraphicsPixmapItem(QGraphicsItem):
    """
    QGraphicsPixmapItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsPixmapItem(QPixmap, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.contains(QPointF) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def offset(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.offset() -> QPointF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.pixmap() -> QPixmap """
        return QPixmap

    def setOffset(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsPixmapItem.setOffset(QPointF)
        QGraphicsPixmapItem.setOffset(float, float)
        """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.setPixmap(QPixmap) """
        pass

    def setShapeMode(self, QGraphicsPixmapItem_ShapeMode): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.setShapeMode(QGraphicsPixmapItem.ShapeMode) """
        pass

    def setTransformationMode(self, Qt_TransformationMode): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.setTransformationMode(Qt.TransformationMode) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.shape() -> QPainterPath """
        return QPainterPath

    def shapeMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.shapeMode() -> QGraphicsPixmapItem.ShapeMode """
        pass

    def transformationMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.transformationMode() -> Qt.TransformationMode """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsPixmapItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BoundingRectShape = 1
    HeuristicMaskShape = 2
    MaskShape = 0


