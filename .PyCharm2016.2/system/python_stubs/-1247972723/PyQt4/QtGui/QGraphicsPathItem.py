# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsPathItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsPathItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsPathItem(QPainterPath, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.contains(QPointF) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.path() -> QPainterPath """
        return QPainterPath

    def setPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.setPath(QPainterPath) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.shape() -> QPainterPath """
        return QPainterPath

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsPathItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


