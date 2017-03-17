# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QDirModel(__PyQt4_QtCore.QAbstractItemModel):
    """
    QDirModel(QStringList, QDir.Filters, QDir.SortFlags, QObject parent=None)
    QDirModel(QObject parent=None)
    """
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDirModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QDirModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def fileIcon(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.fileIcon(QModelIndex) -> QIcon """
        return QIcon

    def fileInfo(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.fileInfo(QModelIndex) -> QFileInfo """
        pass

    def fileName(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.fileName(QModelIndex) -> QString """
        pass

    def filePath(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.filePath(QModelIndex) -> QString """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ QDirModel.filter() -> QDir.Filters """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDirModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QDirModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ QDirModel.iconProvider() -> QFileIconProvider """
        return QFileIconProvider

    def index(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDirModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex
        QDirModel.index(QString, int column=0) -> QModelIndex
        """
        pass

    def isDir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.isDir(QModelIndex) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QDirModel.isReadOnly() -> bool """
        return False

    def lazyChildCount(self): # real signature unknown; restored from __doc__
        """ QDirModel.lazyChildCount() -> bool """
        return False

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.mimeData(list-of-QModelIndex) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QDirModel.mimeTypes() -> QStringList """
        pass

    def mkdir(self, QModelIndex, QString): # real signature unknown; restored from __doc__
        """ QDirModel.mkdir(QModelIndex, QString) -> QModelIndex """
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QDirModel.nameFilters() -> QStringList """
        pass

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDirModel.parent(QModelIndex) -> QModelIndex
        QDirModel.parent() -> QObject
        """
        pass

    def refresh(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDirModel.refresh(QModelIndex parent=QModelIndex()) """
        pass

    def remove(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.remove(QModelIndex) -> bool """
        return False

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ QDirModel.resolveSymlinks() -> bool """
        return False

    def rmdir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QDirModel.rmdir(QModelIndex) -> bool """
        return False

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDirModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QDirModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setFilter(self, QDir_Filters): # real signature unknown; restored from __doc__
        """ QDirModel.setFilter(QDir.Filters) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ QDirModel.setIconProvider(QFileIconProvider) """
        pass

    def setLazyChildCount(self, bool): # real signature unknown; restored from __doc__
        """ QDirModel.setLazyChildCount(bool) """
        pass

    def setNameFilters(self, QStringList): # real signature unknown; restored from __doc__
        """ QDirModel.setNameFilters(QStringList) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QDirModel.setReadOnly(bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ QDirModel.setResolveSymlinks(bool) """
        pass

    def setSorting(self, QDir_SortFlags): # real signature unknown; restored from __doc__
        """ QDirModel.setSorting(QDir.SortFlags) """
        pass

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QDirModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ QDirModel.sorting() -> QDir.SortFlags """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QDirModel.supportedDropActions() -> Qt.DropActions """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FileIconRole = 1
    FileNameRole = 34
    FilePathRole = 33


