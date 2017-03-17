# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QStringListModel(__PyQt4_QtCore.QAbstractListModel):
    """
    QStringListModel(QObject parent=None)
    QStringListModel(QStringList, QObject parent=None)
    """
    def data(self, QModelIndex, p_int): # real signature unknown; restored from __doc__
        """ QStringListModel.data(QModelIndex, int) -> QVariant """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QStringListModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStringListModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStringListModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStringListModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QStringListModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setStringList(self, QStringList): # real signature unknown; restored from __doc__
        """ QStringListModel.setStringList(QStringList) """
        pass

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QStringListModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def stringList(self): # real signature unknown; restored from __doc__
        """ QStringListModel.stringList() -> QStringList """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QStringListModel.supportedDropActions() -> Qt.DropActions """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


