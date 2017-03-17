# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemDelegate import QAbstractItemDelegate

class QItemDelegate(QAbstractItemDelegate):
    """ QItemDelegate(QObject parent=None) """
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.createEditor(QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        return QWidget

    def drawBackground(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.drawBackground(QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def drawCheck(self, QPainter, QStyleOptionViewItem, QRect, Qt_CheckState): # real signature unknown; restored from __doc__
        """ QItemDelegate.drawCheck(QPainter, QStyleOptionViewItem, QRect, Qt.CheckState) """
        pass

    def drawDecoration(self, QPainter, QStyleOptionViewItem, QRect, QPixmap): # real signature unknown; restored from __doc__
        """ QItemDelegate.drawDecoration(QPainter, QStyleOptionViewItem, QRect, QPixmap) """
        pass

    def drawDisplay(self, QPainter, QStyleOptionViewItem, QRect, QString): # real signature unknown; restored from __doc__
        """ QItemDelegate.drawDisplay(QPainter, QStyleOptionViewItem, QRect, QString) """
        pass

    def drawFocus(self, QPainter, QStyleOptionViewItem, QRect): # real signature unknown; restored from __doc__
        """ QItemDelegate.drawFocus(QPainter, QStyleOptionViewItem, QRect) """
        pass

    def editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.editorEvent(QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QItemDelegate.eventFilter(QObject, QEvent) -> bool """
        return False

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ QItemDelegate.hasClipping() -> bool """
        return False

    def itemEditorFactory(self): # real signature unknown; restored from __doc__
        """ QItemDelegate.itemEditorFactory() -> QItemEditorFactory """
        return QItemEditorFactory

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.paint(QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def setClipping(self, bool): # real signature unknown; restored from __doc__
        """ QItemDelegate.setClipping(bool) """
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.setEditorData(QWidget, QModelIndex) """
        pass

    def setItemEditorFactory(self, QItemEditorFactory): # real signature unknown; restored from __doc__
        """ QItemDelegate.setItemEditorFactory(QItemEditorFactory) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.setModelData(QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def sizeHint(self, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.sizeHint(QStyleOptionViewItem, QModelIndex) -> QSize """
        pass

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemDelegate.updateEditorGeometry(QWidget, QStyleOptionViewItem, QModelIndex) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


