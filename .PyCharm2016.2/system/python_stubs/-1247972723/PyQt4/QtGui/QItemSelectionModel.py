# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QItemSelectionModel(__PyQt4_QtCore.QObject):
    """
    QItemSelectionModel(QAbstractItemModel)
    QItemSelectionModel(QAbstractItemModel, QObject)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.clear() """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.clearSelection() """
        pass

    def columnIntersectsSelection(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.columnIntersectsSelection(int, QModelIndex) -> bool """
        return False

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QItemSelectionModel.currentChanged[QModelIndex, QModelIndex] [signal] """
        pass

    def currentColumnChanged(self, *args, **kwargs): # real signature unknown
        """ QItemSelectionModel.currentColumnChanged[QModelIndex, QModelIndex] [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.currentIndex() -> QModelIndex """
        pass

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
        """ QItemSelectionModel.currentRowChanged[QModelIndex, QModelIndex] [signal] """
        pass

    def emitSelectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.emitSelectionChanged(QItemSelection, QItemSelection) """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.hasSelection() -> bool """
        return False

    def isColumnSelected(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.isColumnSelected(int, QModelIndex) -> bool """
        return False

    def isRowSelected(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.isRowSelected(int, QModelIndex) -> bool """
        return False

    def isSelected(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.isSelected(QModelIndex) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.model() -> QAbstractItemModel """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.reset() """
        pass

    def rowIntersectsSelection(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.rowIntersectsSelection(int, QModelIndex) -> bool """
        return False

    def select(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QItemSelectionModel.select(QModelIndex, QItemSelectionModel.SelectionFlags)
        QItemSelectionModel.select(QItemSelection, QItemSelectionModel.SelectionFlags)
        """
        pass

    def selectedColumns(self, int_row=0): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.selectedColumns(int row=0) -> list-of-QModelIndex """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.selectedIndexes() -> list-of-QModelIndex """
        pass

    def selectedRows(self, int_column=0): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.selectedRows(int column=0) -> list-of-QModelIndex """
        pass

    def selection(self): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.selection() -> QItemSelection """
        return QItemSelection

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QItemSelectionModel.selectionChanged[QItemSelection, QItemSelection] [signal] """
        pass

    def setCurrentIndex(self, QModelIndex, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QItemSelectionModel.setCurrentIndex(QModelIndex, QItemSelectionModel.SelectionFlags) """
        pass

    def __init__(self, QAbstractItemModel, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Clear = 1
    ClearAndSelect = 3
    Columns = 64
    Current = 16
    Deselect = 4
    NoUpdate = 0
    Rows = 32
    Select = 2
    SelectCurrent = 18
    Toggle = 8
    ToggleCurrent = 24


