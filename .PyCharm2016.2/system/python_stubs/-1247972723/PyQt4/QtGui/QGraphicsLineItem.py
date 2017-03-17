# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsItem import QGraphicsItem

class QGraphicsLineItem(QGraphicsItem):
    """
    QGraphicsLineItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsLineItem(QLineF, QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsLineItem(float, float, float, float, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.contains(QPointF) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.line() -> QLineF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def pen(self): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.pen() -> QPen """
        return QPen

    def setLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsLineItem.setLine(QLineF)
        QGraphicsLineItem.setLine(float, float, float, float)
        """
        pass

    def setPen(self, QPen): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.setPen(QPen) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.shape() -> QPainterPath """
        return QPainterPath

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsLineItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


