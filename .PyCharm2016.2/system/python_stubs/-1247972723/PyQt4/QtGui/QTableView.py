# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemView import QAbstractItemView

class QTableView(QAbstractItemView):
    """ QTableView(QWidget parent=None) """
    def clearSpans(self): # real signature unknown; restored from __doc__
        """ QTableView.clearSpans() """
        pass

    def columnAt(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.columnAt(int) -> int """
        return 0

    def columnCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.columnCountChanged(int, int) """
        pass

    def columnMoved(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QTableView.columnMoved(int, int, int) """
        pass

    def columnResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QTableView.columnResized(int, int, int) """
        pass

    def columnSpan(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.columnSpan(int, int) -> int """
        return 0

    def columnViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.columnViewportPosition(int) -> int """
        return 0

    def columnWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.columnWidth(int) -> int """
        return 0

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QTableView.currentChanged(QModelIndex, QModelIndex) """
        pass

    def gridStyle(self): # real signature unknown; restored from __doc__
        """ QTableView.gridStyle() -> Qt.PenStyle """
        pass

    def hideColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.hideColumn(int) """
        pass

    def hideRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.hideRow(int) """
        pass

    def horizontalHeader(self): # real signature unknown; restored from __doc__
        """ QTableView.horizontalHeader() -> QHeaderView """
        return QHeaderView

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ QTableView.horizontalOffset() -> int """
        return 0

    def horizontalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.horizontalScrollbarAction(int) """
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QTableView.indexAt(QPoint) -> QModelIndex """
        pass

    def isColumnHidden(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.isColumnHidden(int) -> bool """
        return False

    def isCornerButtonEnabled(self): # real signature unknown; restored from __doc__
        """ QTableView.isCornerButtonEnabled() -> bool """
        return False

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTableView.isIndexHidden(QModelIndex) -> bool """
        return False

    def isRowHidden(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.isRowHidden(int) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ QTableView.isSortingEnabled() -> bool """
        return False

    def moveCursor(self, QAbstractItemView_CursorAction, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QTableView.moveCursor(QAbstractItemView.CursorAction, Qt.KeyboardModifiers) -> QModelIndex """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QTableView.paintEvent(QPaintEvent) """
        pass

    def resizeColumnsToContents(self): # real signature unknown; restored from __doc__
        """ QTableView.resizeColumnsToContents() """
        pass

    def resizeColumnToContents(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.resizeColumnToContents(int) """
        pass

    def resizeRowsToContents(self): # real signature unknown; restored from __doc__
        """ QTableView.resizeRowsToContents() """
        pass

    def resizeRowToContents(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.resizeRowToContents(int) """
        pass

    def rowAt(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.rowAt(int) -> int """
        return 0

    def rowCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.rowCountChanged(int, int) """
        pass

    def rowHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.rowHeight(int) -> int """
        return 0

    def rowMoved(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QTableView.rowMoved(int, int, int) """
        pass

    def rowResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QTableView.rowResized(int, int, int) """
        pass

    def rowSpan(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.rowSpan(int, int) -> int """
        return 0

    def rowViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.rowViewportPosition(int) -> int """
        return 0

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.scrollContentsBy(int, int) """
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QTableView.scrollTo(QModelIndex, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.selectColumn(int) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ QTableView.selectedIndexes() -> list-of-QModelIndex """
        pass

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ QTableView.selectionChanged(QItemSelection, QItemSelection) """
        pass

    def selectRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.selectRow(int) """
        pass

    def setColumnHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QTableView.setColumnHidden(int, bool) """
        pass

    def setColumnWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.setColumnWidth(int, int) """
        pass

    def setCornerButtonEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTableView.setCornerButtonEnabled(bool) """
        pass

    def setGridStyle(self, Qt_PenStyle): # real signature unknown; restored from __doc__
        """ QTableView.setGridStyle(Qt.PenStyle) """
        pass

    def setHorizontalHeader(self, QHeaderView): # real signature unknown; restored from __doc__
        """ QTableView.setHorizontalHeader(QHeaderView) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QTableView.setModel(QAbstractItemModel) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTableView.setRootIndex(QModelIndex) """
        pass

    def setRowHeight(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableView.setRowHeight(int, int) """
        pass

    def setRowHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QTableView.setRowHidden(int, bool) """
        pass

    def setSelection(self, QRect, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QTableView.setSelection(QRect, QItemSelectionModel.SelectionFlags) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ QTableView.setSelectionModel(QItemSelectionModel) """
        pass

    def setShowGrid(self, bool): # real signature unknown; restored from __doc__
        """ QTableView.setShowGrid(bool) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTableView.setSortingEnabled(bool) """
        pass

    def setSpan(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QTableView.setSpan(int, int, int, int) """
        pass

    def setVerticalHeader(self, QHeaderView): # real signature unknown; restored from __doc__
        """ QTableView.setVerticalHeader(QHeaderView) """
        pass

    def setWordWrap(self, bool): # real signature unknown; restored from __doc__
        """ QTableView.setWordWrap(bool) """
        pass

    def showColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.showColumn(int) """
        pass

    def showGrid(self): # real signature unknown; restored from __doc__
        """ QTableView.showGrid() -> bool """
        return False

    def showRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.showRow(int) """
        pass

    def sizeHintForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.sizeHintForColumn(int) -> int """
        return 0

    def sizeHintForRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.sizeHintForRow(int) -> int """
        return 0

    def sortByColumn(self, p_int, Qt_SortOrder=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableView.sortByColumn(int)
        QTableView.sortByColumn(int, Qt.SortOrder)
        """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QTableView.timerEvent(QTimerEvent) """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ QTableView.updateGeometries() """
        pass

    def verticalHeader(self): # real signature unknown; restored from __doc__
        """ QTableView.verticalHeader() -> QHeaderView """
        return QHeaderView

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ QTableView.verticalOffset() -> int """
        return 0

    def verticalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ QTableView.verticalScrollbarAction(int) """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ QTableView.viewOptions() -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTableView.visualRect(QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QTableView.visualRegionForSelection(QItemSelection) -> QRegion """
        return QRegion

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ QTableView.wordWrap() -> bool """
        return False

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


