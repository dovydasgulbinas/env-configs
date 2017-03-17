# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QStandardItemModel(__PyQt4_QtCore.QAbstractItemModel):
    """
    QStandardItemModel(QObject parent=None)
    QStandardItemModel(int, int, QObject parent=None)
    """
    def appendColumn(self, list_of_QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItemModel.appendColumn(list-of-QStandardItem) """
        pass

    def appendRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItemModel.appendRow(list-of-QStandardItem)
        QStandardItemModel.appendRow(QStandardItem)
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QStandardItemModel.clear() """
        pass

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QStandardItemModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QStandardItemModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def findItems(self, QString, Qt_MatchFlags_flags=None, int_column=0): # real signature unknown; restored from __doc__
        """ QStandardItemModel.findItems(QString, Qt.MatchFlags flags=Qt.MatchExactly, int column=0) -> list-of-QStandardItem """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QStandardItemModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QStandardItemModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        pass

    def horizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.horizontalHeaderItem(int) -> QStandardItem """
        return QStandardItem

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def indexFromItem(self, QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItemModel.indexFromItem(QStandardItem) -> QModelIndex """
        pass

    def insertColumn(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItemModel.insertColumn(int, list-of-QStandardItem)
        QStandardItemModel.insertColumn(int, QModelIndex parent=QModelIndex()) -> bool
        """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRow(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItemModel.insertRow(int, list-of-QStandardItem)
        QStandardItemModel.insertRow(int, QStandardItem)
        QStandardItemModel.insertRow(int, QModelIndex parent=QModelIndex()) -> bool
        """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ QStandardItemModel.invisibleRootItem() -> QStandardItem """
        return QStandardItem

    def item(self, p_int, int_column=0): # real signature unknown; restored from __doc__
        """ QStandardItemModel.item(int, int column=0) -> QStandardItem """
        return QStandardItem

    def itemChanged(self, *args, **kwargs): # real signature unknown
        """ QStandardItemModel.itemChanged[QStandardItem] [signal] """
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QStandardItemModel.itemData(QModelIndex) -> dict-of-int-QVariant """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QStandardItemModel.itemFromIndex(QModelIndex) -> QStandardItem """
        return QStandardItem

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ QStandardItemModel.itemPrototype() -> QStandardItem """
        return QStandardItem

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QStandardItemModel.mimeData(list-of-QModelIndex) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QStandardItemModel.mimeTypes() -> QStringList """
        pass

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItemModel.parent(QModelIndex) -> QModelIndex
        QStandardItemModel.parent() -> QObject
        """
        pass

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItemModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setColumnCount(int) """
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHorizontalHeaderItem(self, p_int, QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setHorizontalHeaderItem(int, QStandardItem) """
        pass

    def setHorizontalHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setHorizontalHeaderLabels(QStringList) """
        pass

    def setItem(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItemModel.setItem(int, int, QStandardItem)
        QStandardItemModel.setItem(int, QStandardItem)
        """
        pass

    def setItemData(self, QModelIndex, dict_of_int_QVariant): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setItemData(QModelIndex, dict-of-int-QVariant) -> bool """
        return False

    def setItemPrototype(self, QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setItemPrototype(QStandardItem) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setRowCount(int) """
        pass

    def setSortRole(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setSortRole(int) """
        pass

    def setVerticalHeaderItem(self, p_int, QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setVerticalHeaderItem(int, QStandardItem) """
        pass

    def setVerticalHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QStandardItemModel.setVerticalHeaderLabels(QStringList) """
        pass

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QStandardItemModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ QStandardItemModel.sortRole() -> int """
        return 0

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QStandardItemModel.supportedDropActions() -> Qt.DropActions """
        pass

    def takeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.takeColumn(int) -> list-of-QStandardItem """
        pass

    def takeHorizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.takeHorizontalHeaderItem(int) -> QStandardItem """
        return QStandardItem

    def takeItem(self, p_int, int_column=0): # real signature unknown; restored from __doc__
        """ QStandardItemModel.takeItem(int, int column=0) -> QStandardItem """
        return QStandardItem

    def takeRow(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.takeRow(int) -> list-of-QStandardItem """
        pass

    def takeVerticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.takeVerticalHeaderItem(int) -> QStandardItem """
        return QStandardItem

    def verticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItemModel.verticalHeaderItem(int) -> QStandardItem """
        return QStandardItem

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


