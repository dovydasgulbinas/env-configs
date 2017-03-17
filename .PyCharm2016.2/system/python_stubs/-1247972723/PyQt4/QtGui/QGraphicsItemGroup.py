# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsItem import QGraphicsItem

class QGraphicsItemGroup(QGraphicsItem):
    """ QGraphicsItemGroup(QGraphicsItem parent=None, QGraphicsScene scene=None) """
    def addToGroup(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.addToGroup(QGraphicsItem) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.boundingRect() -> QRectF """
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def removeFromGroup(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.removeFromGroup(QGraphicsItem) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsItemGroup.type() -> int """
        return 0

    def __init__(self, QGraphicsItem_parent=None, QGraphicsScene_scene=None): # real signature unknown; restored from __doc__
        pass


