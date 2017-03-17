# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsEllipseItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsEllipseItem(QRectF, QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsEllipseItem(float, float, float, float, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.contains(QPointF) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.rect() -> QRectF """
        pass

    def setRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsEllipseItem.setRect(QRectF)
        QGraphicsEllipseItem.setRect(float, float, float, float)
        """
        pass

    def setSpanAngle(self, p_int): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.setSpanAngle(int) """
        pass

    def setStartAngle(self, p_int): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.setStartAngle(int) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.shape() -> QPainterPath """
        return QPainterPath

    def spanAngle(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.spanAngle() -> int """
        return 0

    def startAngle(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.startAngle() -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsEllipseItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


