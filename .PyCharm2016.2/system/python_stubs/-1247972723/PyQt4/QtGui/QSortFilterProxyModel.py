# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractProxyModel import QAbstractProxyModel

class QSortFilterProxyModel(QAbstractProxyModel):
    """ QSortFilterProxyModel(QObject parent=None) """
    def buddy(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.buddy(QModelIndex) -> QModelIndex """
        pass

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.canFetchMore(QModelIndex) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.clear() """
        pass

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def dynamicSortFilter(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.dynamicSortFilter() -> bool """
        return False

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.fetchMore(QModelIndex) """
        pass

    def filterAcceptsColumn(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterAcceptsColumn(int, QModelIndex) -> bool """
        return False

    def filterAcceptsRow(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterAcceptsRow(int, QModelIndex) -> bool """
        return False

    def filterCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterCaseSensitivity() -> Qt.CaseSensitivity """
        pass

    def filterChanged(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterChanged() """
        pass

    def filterKeyColumn(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterKeyColumn() -> int """
        return 0

    def filterRegExp(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterRegExp() -> QRegExp """
        pass

    def filterRole(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.filterRole() -> int """
        return 0

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.headerData(int, Qt.Orientation, int role=Qt.EditRole) -> QVariant """
        pass

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.invalidate() """
        pass

    def invalidateFilter(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.invalidateFilter() """
        pass

    def isSortLocaleAware(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.isSortLocaleAware() -> bool """
        return False

    def lessThan(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.lessThan(QModelIndex, QModelIndex) -> bool """
        return False

    def mapFromSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.mapFromSource(QModelIndex) -> QModelIndex """
        pass

    def mapSelectionFromSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.mapSelectionFromSource(QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapSelectionToSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.mapSelectionToSource(QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapToSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.mapToSource(QModelIndex) -> QModelIndex """
        pass

    def match(self, QModelIndex, p_int, QVariant, int_hits=1, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.match(QModelIndex, int, QVariant, int hits=1, Qt.MatchFlags flags=Qt.MatchStartsWith|Qt.MatchWrap) -> list-of-QModelIndex """
        pass

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.mimeData(list-of-QModelIndex) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.mimeTypes() -> QStringList """
        pass

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSortFilterProxyModel.parent(QModelIndex) -> QModelIndex
        QSortFilterProxyModel.parent() -> QObject
        """
        pass

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSortFilterProxyModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setDynamicSortFilter(self, bool): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setDynamicSortFilter(bool) """
        pass

    def setFilterCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setFilterCaseSensitivity(Qt.CaseSensitivity) """
        pass

    def setFilterFixedString(self, QString): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setFilterFixedString(QString) """
        pass

    def setFilterKeyColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setFilterKeyColumn(int) """
        pass

    def setFilterRegExp(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSortFilterProxyModel.setFilterRegExp(QRegExp)
        QSortFilterProxyModel.setFilterRegExp(QString)
        """
        pass

    def setFilterRole(self, p_int): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setFilterRole(int) """
        pass

    def setFilterWildcard(self, QString): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setFilterWildcard(QString) """
        pass

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setSortCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setSortCaseSensitivity(Qt.CaseSensitivity) """
        pass

    def setSortLocaleAware(self, bool): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setSortLocaleAware(bool) """
        pass

    def setSortRole(self, p_int): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setSortRole(int) """
        pass

    def setSourceModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.setSourceModel(QAbstractItemModel) """
        pass

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def sortCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.sortCaseSensitivity() -> Qt.CaseSensitivity """
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.sortColumn() -> int """
        return 0

    def sortOrder(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.sortOrder() -> Qt.SortOrder """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.sortRole() -> int """
        return 0

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.span(QModelIndex) -> QSize """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QSortFilterProxyModel.supportedDropActions() -> Qt.DropActions """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


