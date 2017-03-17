# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QTableView import QTableView

class QTableWidget(QTableView):
    """
    QTableWidget(QWidget parent=None)
    QTableWidget(int, int, QWidget parent=None)
    """
    def cellActivated(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.cellActivated[int, int] [signal] """
        pass

    def cellChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.cellChanged[int, int] [signal] """
        pass

    def cellClicked(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.cellClicked[int, int] [signal] """
        pass

    def cellDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.cellDoubleClicked[int, int] [signal] """
        pass

    def cellEntered(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.cellEntered[int, int] [signal] """
        pass

    def cellPressed(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.cellPressed[int, int] [signal] """
        pass

    def cellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableWidget.cellWidget(int, int) -> QWidget """
        return QWidget

    def clear(self): # real signature unknown; restored from __doc__
        """ QTableWidget.clear() """
        pass

    def clearContents(self): # real signature unknown; restored from __doc__
        """ QTableWidget.clearContents() """
        pass

    def closePersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.closePersistentEditor(QTableWidgetItem) """
        pass

    def column(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.column(QTableWidgetItem) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QTableWidget.columnCount() -> int """
        return 0

    def currentCellChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.currentCellChanged[int, int, int, int] [signal] """
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ QTableWidget.currentColumn() -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ QTableWidget.currentItem() -> QTableWidgetItem """
        return QTableWidgetItem

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.currentItemChanged[QTableWidgetItem, QTableWidgetItem] [signal] """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ QTableWidget.currentRow() -> int """
        return 0

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QTableWidget.dropEvent(QDropEvent) """
        pass

    def dropMimeData(self, p_int, p_int_1, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QTableWidget.dropMimeData(int, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def editItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.editItem(QTableWidgetItem) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QTableWidget.event(QEvent) -> bool """
        return False

    def findItems(self, QString, Qt_MatchFlags): # real signature unknown; restored from __doc__
        """ QTableWidget.findItems(QString, Qt.MatchFlags) -> list-of-QTableWidgetItem """
        pass

    def horizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.horizontalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def indexFromItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.indexFromItem(QTableWidgetItem) -> QModelIndex """
        pass

    def insertColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.insertColumn(int) """
        pass

    def insertRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.insertRow(int) """
        pass

    def isItemSelected(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.isItemSelected(QTableWidgetItem) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ QTableWidget.isSortingEnabled() -> bool """
        return False

    def item(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableWidget.item(int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemActivated(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemActivated[QTableWidgetItem] [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableWidget.itemAt(QPoint) -> QTableWidgetItem
        QTableWidget.itemAt(int, int) -> QTableWidgetItem
        """
        return QTableWidgetItem

    def itemChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemChanged[QTableWidgetItem] [signal] """
        pass

    def itemClicked(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemClicked[QTableWidgetItem] [signal] """
        pass

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemDoubleClicked[QTableWidgetItem] [signal] """
        pass

    def itemEntered(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemEntered[QTableWidgetItem] [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTableWidget.itemFromIndex(QModelIndex) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemPressed(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemPressed[QTableWidgetItem] [signal] """
        pass

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ QTableWidget.itemPrototype() -> QTableWidgetItem """
        return QTableWidgetItem

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ QTableWidget.items(QMimeData) -> list-of-QTableWidgetItem """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        """ QTableWidget.itemSelectionChanged [signal] """
        pass

    def mimeData(self, list_of_QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.mimeData(list-of-QTableWidgetItem) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QTableWidget.mimeTypes() -> QStringList """
        pass

    def openPersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.openPersistentEditor(QTableWidgetItem) """
        pass

    def removeCellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableWidget.removeCellWidget(int, int) """
        pass

    def removeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.removeColumn(int) """
        pass

    def removeRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.removeRow(int) """
        pass

    def row(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.row(QTableWidgetItem) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ QTableWidget.rowCount() -> int """
        return 0

    def scrollToItem(self, QTableWidgetItem, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QTableWidget.scrollToItem(QTableWidgetItem, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ QTableWidget.selectedItems() -> list-of-QTableWidgetItem """
        pass

    def selectedRanges(self): # real signature unknown; restored from __doc__
        """ QTableWidget.selectedRanges() -> list-of-QTableWidgetSelectionRange """
        pass

    def setCellWidget(self, p_int, p_int_1, QWidget): # real signature unknown; restored from __doc__
        """ QTableWidget.setCellWidget(int, int, QWidget) """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.setColumnCount(int) """
        pass

    def setCurrentCell(self, p_int, p_int_1, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableWidget.setCurrentCell(int, int)
        QTableWidget.setCurrentCell(int, int, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setCurrentItem(self, QTableWidgetItem, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTableWidget.setCurrentItem(QTableWidgetItem)
        QTableWidget.setCurrentItem(QTableWidgetItem, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setHorizontalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setHorizontalHeaderItem(int, QTableWidgetItem) """
        pass

    def setHorizontalHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QTableWidget.setHorizontalHeaderLabels(QStringList) """
        pass

    def setItem(self, p_int, p_int_1, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setItem(int, int, QTableWidgetItem) """
        pass

    def setItemPrototype(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setItemPrototype(QTableWidgetItem) """
        pass

    def setItemSelected(self, QTableWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QTableWidget.setItemSelected(QTableWidgetItem, bool) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setRangeSelected(self, QTableWidgetSelectionRange, bool): # real signature unknown; restored from __doc__
        """ QTableWidget.setRangeSelected(QTableWidgetSelectionRange, bool) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.setRowCount(int) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTableWidget.setSortingEnabled(bool) """
        pass

    def setVerticalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.setVerticalHeaderItem(int, QTableWidgetItem) """
        pass

    def setVerticalHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QTableWidget.setVerticalHeaderLabels(QStringList) """
        pass

    def sortItems(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QTableWidget.sortItems(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QTableWidget.supportedDropActions() -> Qt.DropActions """
        pass

    def takeHorizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.takeHorizontalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeItem(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTableWidget.takeItem(int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeVerticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.takeVerticalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def verticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.verticalHeaderItem(int) -> QTableWidgetItem """
        return QTableWidgetItem

    def visualColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.visualColumn(int) -> int """
        return 0

    def visualItemRect(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ QTableWidget.visualItemRect(QTableWidgetItem) -> QRect """
        pass

    def visualRow(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidget.visualRow(int) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


