# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QTreeView import QTreeView

class QTreeWidget(QTreeView):
    """ QTreeWidget(QWidget parent=None) """
    def addTopLevelItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.addTopLevelItem(QTreeWidgetItem) """
        pass

    def addTopLevelItems(self, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.addTopLevelItems(list-of-QTreeWidgetItem) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.clear() """
        pass

    def closePersistentEditor(self, QTreeWidgetItem, int_column=0): # real signature unknown; restored from __doc__
        """ QTreeWidget.closePersistentEditor(QTreeWidgetItem, int column=0) """
        pass

    def collapseItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.collapseItem(QTreeWidgetItem) """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.columnCount() -> int """
        return 0

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.currentColumn() -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.currentItem() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.currentItemChanged[QTreeWidgetItem, QTreeWidgetItem] [signal] """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QTreeWidget.dropEvent(QDropEvent) """
        pass

    def dropMimeData(self, QTreeWidgetItem, p_int, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QTreeWidget.dropMimeData(QTreeWidgetItem, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def editItem(self, QTreeWidgetItem, int_column=0): # real signature unknown; restored from __doc__
        """ QTreeWidget.editItem(QTreeWidgetItem, int column=0) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QTreeWidget.event(QEvent) -> bool """
        return False

    def expandItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.expandItem(QTreeWidgetItem) """
        pass

    def findItems(self, QString, Qt_MatchFlags, int_column=0): # real signature unknown; restored from __doc__
        """ QTreeWidget.findItems(QString, Qt.MatchFlags, int column=0) -> list-of-QTreeWidgetItem """
        pass

    def headerItem(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.headerItem() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def indexFromItem(self, QTreeWidgetItem, int_column=0): # real signature unknown; restored from __doc__
        """ QTreeWidget.indexFromItem(QTreeWidgetItem, int column=0) -> QModelIndex """
        pass

    def indexOfTopLevelItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.indexOfTopLevelItem(QTreeWidgetItem) -> int """
        return 0

    def insertTopLevelItem(self, p_int, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.insertTopLevelItem(int, QTreeWidgetItem) """
        pass

    def insertTopLevelItems(self, p_int, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.insertTopLevelItems(int, list-of-QTreeWidgetItem) """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.invisibleRootItem() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def isFirstItemColumnSpanned(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.isFirstItemColumnSpanned(QTreeWidgetItem) -> bool """
        return False

    def isItemExpanded(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.isItemExpanded(QTreeWidgetItem) -> bool """
        return False

    def isItemHidden(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.isItemHidden(QTreeWidgetItem) -> bool """
        return False

    def isItemSelected(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.isItemSelected(QTreeWidgetItem) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.isSortingEnabled() -> bool """
        return False

    def itemAbove(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.itemAbove(QTreeWidgetItem) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemActivated(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemActivated[QTreeWidgetItem, int] [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTreeWidget.itemAt(QPoint) -> QTreeWidgetItem
        QTreeWidget.itemAt(int, int) -> QTreeWidgetItem
        """
        return QTreeWidgetItem

    def itemBelow(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.itemBelow(QTreeWidgetItem) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemChanged(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemChanged[QTreeWidgetItem, int] [signal] """
        pass

    def itemClicked(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemClicked[QTreeWidgetItem, int] [signal] """
        pass

    def itemCollapsed(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemCollapsed[QTreeWidgetItem] [signal] """
        pass

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemDoubleClicked[QTreeWidgetItem, int] [signal] """
        pass

    def itemEntered(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemEntered[QTreeWidgetItem, int] [signal] """
        pass

    def itemExpanded(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemExpanded[QTreeWidgetItem] [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QTreeWidget.itemFromIndex(QModelIndex) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemPressed(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemPressed[QTreeWidgetItem, int] [signal] """
        pass

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ QTreeWidget.items(QMimeData) -> list-of-QTreeWidgetItem """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        """ QTreeWidget.itemSelectionChanged [signal] """
        pass

    def itemWidget(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidget.itemWidget(QTreeWidgetItem, int) -> QWidget """
        return QWidget

    def mimeData(self, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.mimeData(list-of-QTreeWidgetItem) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.mimeTypes() -> QStringList """
        pass

    def openPersistentEditor(self, QTreeWidgetItem, int_column=0): # real signature unknown; restored from __doc__
        """ QTreeWidget.openPersistentEditor(QTreeWidgetItem, int column=0) """
        pass

    def removeItemWidget(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidget.removeItemWidget(QTreeWidgetItem, int) """
        pass

    def scrollToItem(self, QTreeWidgetItem, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QTreeWidget.scrollToItem(QTreeWidgetItem, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.selectedItems() -> list-of-QTreeWidgetItem """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidget.setColumnCount(int) """
        pass

    def setCurrentItem(self, QTreeWidgetItem, p_int=None, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTreeWidget.setCurrentItem(QTreeWidgetItem)
        QTreeWidget.setCurrentItem(QTreeWidgetItem, int)
        QTreeWidget.setCurrentItem(QTreeWidgetItem, int, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setFirstItemColumnSpanned(self, QTreeWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QTreeWidget.setFirstItemColumnSpanned(QTreeWidgetItem, bool) """
        pass

    def setHeaderItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.setHeaderItem(QTreeWidgetItem) """
        pass

    def setHeaderLabel(self, QString): # real signature unknown; restored from __doc__
        """ QTreeWidget.setHeaderLabel(QString) """
        pass

    def setHeaderLabels(self, QStringList): # real signature unknown; restored from __doc__
        """ QTreeWidget.setHeaderLabels(QStringList) """
        pass

    def setItemExpanded(self, QTreeWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QTreeWidget.setItemExpanded(QTreeWidgetItem, bool) """
        pass

    def setItemHidden(self, QTreeWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QTreeWidget.setItemHidden(QTreeWidgetItem, bool) """
        pass

    def setItemSelected(self, QTreeWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QTreeWidget.setItemSelected(QTreeWidgetItem, bool) """
        pass

    def setItemWidget(self, QTreeWidgetItem, p_int, QWidget): # real signature unknown; restored from __doc__
        """ QTreeWidget.setItemWidget(QTreeWidgetItem, int, QWidget) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ QTreeWidget.setSelectionModel(QItemSelectionModel) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidget.setSortingEnabled(bool) """
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.sortColumn() -> int """
        return 0

    def sortItems(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ QTreeWidget.sortItems(int, Qt.SortOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.supportedDropActions() -> Qt.DropActions """
        pass

    def takeTopLevelItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidget.takeTopLevelItem(int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def topLevelItem(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidget.topLevelItem(int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def topLevelItemCount(self): # real signature unknown; restored from __doc__
        """ QTreeWidget.topLevelItemCount() -> int """
        return 0

    def visualItemRect(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidget.visualItemRect(QTreeWidgetItem) -> QRect """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


