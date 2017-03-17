# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemView import QAbstractItemView

class QTreeView(QAbstractItemView):
    """ QTreeView(QWidget parent=None) """
    def allColumnsShowFocus(self): # real signature unknown; restored from __doc__
        """ QTreeView.allColumnsShowFocus() -> bool """
        return False

    def autoExpandDelay(self): # real signature unknown; restored from __doc__
        """ QTreeView.autoExpandDelay() -> int """
        return 0

    def collapse(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.collapse(QModelIndex) """
        pass

    def collapseAll(self): # real signature unknown; restored from __doc__
        """ QTreeView.collapseAll() """
        pass

    def collapsed(self, *args, **kwargs): # real signature unknown
        """ QTreeView.collapsed[QModelIndex] [signal] """
        pass

    def columnAt(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.columnAt(int) -> int """
        return 0

    def columnCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeView.columnCountChanged(int, int) """
        pass

    def columnMoved(self): # real signature unknown; restored from __doc__
        """ QTreeView.columnMoved() """
        pass

    def columnResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QTreeView.columnResized(int, int, int) """
        pass

    def columnViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.columnViewportPosition(int) -> int """
        return 0

    def columnWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.columnWidth(int) -> int """
        return 0

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QTreeView.currentChanged(QModelIndex, QModelIndex) """
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QTreeView.dataChanged(QModelIndex, QModelIndex) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QTreeView.dragMoveEvent(QDragMoveEvent) """
        pass

    def drawBranches(self, QPainter, QRect, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.drawBranches(QPainter, QRect, QModelIndex) """
        pass

    def drawRow(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.drawRow(QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def drawTree(self, QPainter, QRegion): # real signature unknown; restored from __doc__
        """ QTreeView.drawTree(QPainter, QRegion) """
        pass

    def expand(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.expand(QModelIndex) """
        pass

    def expandAll(self): # real signature unknown; restored from __doc__
        """ QTreeView.expandAll() """
        pass

    def expanded(self, *args, **kwargs): # real signature unknown
        """ QTreeView.expanded[QModelIndex] [signal] """
        pass

    def expandsOnDoubleClick(self): # real signature unknown; restored from __doc__
        """ QTreeView.expandsOnDoubleClick() -> bool """
        return False

    def expandToDepth(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.expandToDepth(int) """
        pass

    def header(self): # real signature unknown; restored from __doc__
        """ QTreeView.header() -> QHeaderView """
        return QHeaderView

    def hideColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.hideColumn(int) """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ QTreeView.horizontalOffset() -> int """
        return 0

    def horizontalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.horizontalScrollbarAction(int) """
        pass

    def indentation(self): # real signature unknown; restored from __doc__
        """ QTreeView.indentation() -> int """
        return 0

    def indexAbove(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.indexAbove(QModelIndex) -> QModelIndex """
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QTreeView.indexAt(QPoint) -> QModelIndex """
        pass

    def indexBelow(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.indexBelow(QModelIndex) -> QModelIndex """
        pass

    def indexRowSizeHint(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.indexRowSizeHint(QModelIndex) -> int """
        return 0

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ QTreeView.isAnimated() -> bool """
        return False

    def isColumnHidden(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.isColumnHidden(int) -> bool """
        return False

    def isExpanded(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.isExpanded(QModelIndex) -> bool """
        return False

    def isFirstColumnSpanned(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.isFirstColumnSpanned(int, QModelIndex) -> bool """
        return False

    def isHeaderHidden(self): # real signature unknown; restored from __doc__
        """ QTreeView.isHeaderHidden() -> bool """
        return False

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.isIndexHidden(QModelIndex) -> bool """
        return False

    def isRowHidden(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.isRowHidden(int, QModelIndex) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ QTreeView.isSortingEnabled() -> bool """
        return False

    def itemsExpandable(self): # real signature unknown; restored from __doc__
        """ QTreeView.itemsExpandable() -> bool """
        return False

    def keyboardSearch(self, QString): # real signature unknown; restored from __doc__
        """ QTreeView.keyboardSearch(QString) """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QTreeView.keyPressEvent(QKeyEvent) """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTreeView.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTreeView.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTreeView.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTreeView.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveCursor(self, QAbstractItemView_CursorAction, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QTreeView.moveCursor(QAbstractItemView.CursorAction, Qt.KeyboardModifiers) -> QModelIndex """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QTreeView.paintEvent(QPaintEvent) """
        pass

    def reexpand(self): # real signature unknown; restored from __doc__
        """ QTreeView.reexpand() """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QTreeView.reset() """
        pass

    def resizeColumnToContents(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.resizeColumnToContents(int) """
        pass

    def rootIsDecorated(self): # real signature unknown; restored from __doc__
        """ QTreeView.rootIsDecorated() -> bool """
        return False

    def rowHeight(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.rowHeight(QModelIndex) -> int """
        return 0

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeView.rowsAboutToBeRemoved(QModelIndex, int, int) """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeView.rowsInserted(QModelIndex, int, int) """
        pass

    def rowsRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeView.rowsRemoved(QModelIndex, int, int) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeView.scrollContentsBy(int, int) """
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QTreeView.scrollTo(QModelIndex, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ QTreeView.selectAll() """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ QTreeView.selectedIndexes() -> list-of-QModelIndex """
        pass

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ QTreeView.selectionChanged(QItemSelection, QItemSelection) """
        pass

    def setAllColumnsShowFocus(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setAllColumnsShowFocus(bool) """
        pass

    def setAnimated(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setAnimated(bool) """
        pass

    def setAutoExpandDelay(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.setAutoExpandDelay(int) """
        pass

    def setColumnHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setColumnHidden(int, bool) """
        pass

    def setColumnWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeView.setColumnWidth(int, int) """
        pass

    def setExpanded(self, QModelIndex, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setExpanded(QModelIndex, bool) """
        pass

    def setExpandsOnDoubleClick(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setExpandsOnDoubleClick(bool) """
        pass

    def setFirstColumnSpanned(self, p_int, QModelIndex, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setFirstColumnSpanned(int, QModelIndex, bool) """
        pass

    def setHeader(self, QHeaderView): # real signature unknown; restored from __doc__
        """ QTreeView.setHeader(QHeaderView) """
        pass

    def setHeaderHidden(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setHeaderHidden(bool) """
        pass

    def setIndentation(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.setIndentation(int) """
        pass

    def setItemsExpandable(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setItemsExpandable(bool) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QTreeView.setModel(QAbstractItemModel) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.setRootIndex(QModelIndex) """
        pass

    def setRootIsDecorated(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setRootIsDecorated(bool) """
        pass

    def setRowHidden(self, p_int, QModelIndex, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setRowHidden(int, QModelIndex, bool) """
        pass

    def setSelection(self, QRect, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QTreeView.setSelection(QRect, QItemSelectionModel.SelectionFlags) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ QTreeView.setSelectionModel(QItemSelectionModel) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setSortingEnabled(bool) """
        pass

    def setUniformRowHeights(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setUniformRowHeights(bool) """
        pass

    def setWordWrap(self, bool): # real signature unknown; restored from __doc__
        """ QTreeView.setWordWrap(bool) """
        pass

    def showColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.showColumn(int) """
        pass

    def sizeHintForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeView.sizeHintForColumn(int) -> int """
        return 0

    def sortByColumn(self, p_int, Qt_SortOrder=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTreeView.sortByColumn(int)
        QTreeView.sortByColumn(int, Qt.SortOrder)
        """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QTreeView.timerEvent(QTimerEvent) """
        pass

    def uniformRowHeights(self): # real signature unknown; restored from __doc__
        """ QTreeView.uniformRowHeights() -> bool """
        return False

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ QTreeView.updateGeometries() """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ QTreeView.verticalOffset() -> int """
        return 0

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QTreeView.viewportEvent(QEvent) -> bool """
        return False

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeView.visualRect(QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QTreeView.visualRegionForSelection(QItemSelection) -> QRegion """
        return QRegion

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ QTreeView.wordWrap() -> bool """
        return False

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


