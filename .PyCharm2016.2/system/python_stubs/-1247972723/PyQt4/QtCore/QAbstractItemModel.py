# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractItemModel(QObject):
    """ QAbstractItemModel(QObject parent=None) """
    def beginInsertColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginInsertColumns(QModelIndex, int, int) """
        pass

    def beginInsertRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginInsertRows(QModelIndex, int, int) """
        pass

    def beginMoveColumns(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginMoveColumns(QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginMoveRows(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginMoveRows(QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginRemoveColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginRemoveColumns(QModelIndex, int, int) """
        pass

    def beginRemoveRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginRemoveRows(QModelIndex, int, int) """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.beginResetModel() """
        pass

    def buddy(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.buddy(QModelIndex) -> QModelIndex """
        return QModelIndex

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.canFetchMore(QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.changePersistentIndex(QModelIndex, QModelIndex) """
        pass

    def changePersistentIndexList(self, list_of_QModelIndex, list_of_QModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.changePersistentIndexList(list-of-QModelIndex, list-of-QModelIndex) """
        pass

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def columnsAboutToBeInserted(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.columnsAboutToBeInserted[QModelIndex, int, int] [signal] """
        pass

    def columnsAboutToBeMoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.columnsAboutToBeMoved[QModelIndex, int, int, QModelIndex, int] [signal] """
        pass

    def columnsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.columnsAboutToBeRemoved[QModelIndex, int, int] [signal] """
        pass

    def columnsInserted(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.columnsInserted[QModelIndex, int, int] [signal] """
        pass

    def columnsMoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.columnsMoved[QModelIndex, int, int, QModelIndex, int] [signal] """
        pass

    def columnsRemoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.columnsRemoved[QModelIndex, int, int] [signal] """
        pass

    def createIndex(self, p_int, p_int_1, object_object=0): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.createIndex(int, int, object object=0) -> QModelIndex """
        return QModelIndex

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        return QVariant

    def dataChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.dataChanged[QModelIndex, QModelIndex] [signal] """
        pass

    def decodeData(self, p_int, p_int_1, QModelIndex, QDataStream): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.decodeData(int, int, QModelIndex, QDataStream) -> bool """
        return False

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def encodeData(self, list_of_QModelIndex, QDataStream): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.encodeData(list-of-QModelIndex, QDataStream) """
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endInsertColumns() """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endInsertRows() """
        pass

    def endMoveColumns(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endMoveColumns() """
        pass

    def endMoveRows(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endMoveRows() """
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endRemoveColumns() """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endRemoveRows() """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.endResetModel() """
        pass

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.fetchMore(QModelIndex) """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def hasIndex(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.hasIndex(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        return QVariant

    def headerDataChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.headerDataChanged[Qt.Orientation, int, int] [signal] """
        pass

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def insertColumn(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.insertColumn(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRow(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.insertRow(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.itemData(QModelIndex) -> dict-of-int-QVariant """
        pass

    def layoutAboutToBeChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.layoutAboutToBeChanged [signal] """
        pass

    def layoutChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.layoutChanged [signal] """
        pass

    def match(self, QModelIndex, p_int, QVariant, int_hits=1, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.match(QModelIndex, int, QVariant, int hits=1, Qt.MatchFlags flags=Qt.MatchStartsWith|Qt.MatchWrap) -> list-of-QModelIndex """
        pass

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.mimeData(list-of-QModelIndex) -> QMimeData """
        return QMimeData

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.mimeTypes() -> QStringList """
        return QStringList

    def modelAboutToBeReset(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.modelAboutToBeReset [signal] """
        pass

    def modelReset(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.modelReset [signal] """
        pass

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractItemModel.parent(QModelIndex) -> QModelIndex
        QAbstractItemModel.parent() -> QObject
        """
        return QModelIndex or QObject

    def persistentIndexList(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.persistentIndexList() -> list-of-QModelIndex """
        pass

    def removeColumn(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.removeColumn(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRow(self, p_int, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.removeRow(int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.reset() """
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.resetInternalData() """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.revert() """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.roleNames() -> dict-of-int-QByteArray """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractItemModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def rowsAboutToBeInserted(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.rowsAboutToBeInserted[QModelIndex, int, int] [signal] """
        pass

    def rowsAboutToBeMoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.rowsAboutToBeMoved[QModelIndex, int, int, QModelIndex, int] [signal] """
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.rowsAboutToBeRemoved[QModelIndex, int, int] [signal] """
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.rowsInserted[QModelIndex, int, int] [signal] """
        pass

    def rowsMoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.rowsMoved[QModelIndex, int, int, QModelIndex, int] [signal] """
        pass

    def rowsRemoved(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemModel.rowsRemoved[QModelIndex, int, int] [signal] """
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setItemData(self, QModelIndex, dict_of_int_QVariant): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setItemData(QModelIndex, dict-of-int-QVariant) -> bool """
        return False

    def setRoleNames(self, dict_of_int_QByteArray): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setRoleNames(dict-of-int-QByteArray) """
        pass

    def setSupportedDragActions(self, Qt_DropActions): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.setSupportedDragActions(Qt.DropActions) """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.sibling(int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.span(QModelIndex) -> QSize """
        return QSize

    def submit(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.submit() -> bool """
        return False

    def supportedDragActions(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.supportedDragActions() -> Qt.DropActions """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QAbstractItemModel.supportedDropActions() -> Qt.DropActions """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


