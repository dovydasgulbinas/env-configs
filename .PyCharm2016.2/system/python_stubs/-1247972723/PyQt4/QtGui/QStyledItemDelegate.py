# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemDelegate import QAbstractItemDelegate

class QStyledItemDelegate(QAbstractItemDelegate):
    """ QStyledItemDelegate(QObject parent=None) """
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.createEditor(QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        return QWidget

    def displayText(self, QVariant, QLocale): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.displayText(QVariant, QLocale) -> QString """
        pass

    def editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.editorEvent(QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.eventFilter(QObject, QEvent) -> bool """
        return False

    def initStyleOption(self, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.initStyleOption(QStyleOptionViewItem, QModelIndex) """
        pass

    def itemEditorFactory(self): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.itemEditorFactory() -> QItemEditorFactory """
        return QItemEditorFactory

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.paint(QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.setEditorData(QWidget, QModelIndex) """
        pass

    def setItemEditorFactory(self, QItemEditorFactory): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.setItemEditorFactory(QItemEditorFactory) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.setModelData(QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def sizeHint(self, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.sizeHint(QStyleOptionViewItem, QModelIndex) -> QSize """
        pass

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QStyledItemDelegate.updateEditorGeometry(QWidget, QStyleOptionViewItem, QModelIndex) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


