# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractProxyModel import QAbstractProxyModel

class QIdentityProxyModel(QAbstractProxyModel):
    """ QIdentityProxyModel(QObject parent=None) """
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def mapFromSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.mapFromSource(QModelIndex) -> QModelIndex """
        pass

    def mapSelectionFromSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.mapSelectionFromSource(QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapSelectionToSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.mapSelectionToSource(QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapToSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.mapToSource(QModelIndex) -> QModelIndex """
        pass

    def match(self, QModelIndex, p_int, QVariant, int_hits=1, Qt_MatchFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.match(QModelIndex, int, QVariant, int hits=1, Qt.MatchFlags flags=Qt.MatchStartsWith|Qt.MatchWrap) -> list-of-QModelIndex """
        pass

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.parent(QModelIndex) -> QModelIndex """
        pass

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QIdentityProxyModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setSourceModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QIdentityProxyModel.setSourceModel(QAbstractItemModel) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


