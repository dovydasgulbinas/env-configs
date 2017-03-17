# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QProxyModel(__PyQt4_QtCore.QAbstractItemModel):
    """ QProxyModel(QObject parent=None) """
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QProxyModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QProxyModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QProxyModel.fetchMore(QModelIndex) """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QProxyModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QProxyModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        pass

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def match(self, QModelIndex, p_int, QVariant, int_hits=1, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.match(QModelIndex, int, QVariant, int hits=1, Qt.MatchFlags flags=Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap)) -> list-of-QModelIndex """
        pass

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QProxyModel.mimeData(list-of-QModelIndex) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QProxyModel.mimeTypes() -> QStringList """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ QProxyModel.model() -> QAbstractItemModel """
        pass

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QProxyModel.parent(QModelIndex) -> QModelIndex
        QProxyModel.parent() -> QObject
        """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ QProxyModel.revert() """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QProxyModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QProxyModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QProxyModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QProxyModel.setModel(QAbstractItemModel) """
        pass

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QProxyModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QProxyModel.span(QModelIndex) -> QSize """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ QProxyModel.submit() -> bool """
        return False

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QProxyModel.supportedDropActions() -> Qt.DropActions """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


