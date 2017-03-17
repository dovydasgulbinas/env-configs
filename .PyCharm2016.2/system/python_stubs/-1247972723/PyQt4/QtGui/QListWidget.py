# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QListView import QListView

class QListWidget(QListView):
    """ QListWidget(QWidget parent=None) """
    def addItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QListWidget.addItem(QListWidgetItem)
        QListWidget.addItem(QString)
        """
        pass

    def addItems(self, QStringList): # real signature unknown; restored from __doc__
        """ QListWidget.addItems(QStringList) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QListWidget.clear() """
        pass

    def closePersistentEditor(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.closePersistentEditor(QListWidgetItem) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QListWidget.count() -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ QListWidget.currentItem() -> QListWidgetItem """
        return QListWidgetItem

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        """ QListWidget.currentItemChanged[QListWidgetItem, QListWidgetItem] [signal] """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ QListWidget.currentRow() -> int """
        return 0

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
        """ QListWidget.currentRowChanged[int] [signal] """
        pass

    def currentTextChanged(self, *args, **kwargs): # real signature unknown
        """ QListWidget.currentTextChanged[QString] [signal] """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QListWidget.dropEvent(QDropEvent) """
        pass

    def dropMimeData(self, p_int, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QListWidget.dropMimeData(int, QMimeData, Qt.DropAction) -> bool """
        return False

    def editItem(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.editItem(QListWidgetItem) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QListWidget.event(QEvent) -> bool """
        return False

    def findItems(self, QString, Qt_MatchFlags): # real signature unknown; restored from __doc__
        """ QListWidget.findItems(QString, Qt.MatchFlags) -> list-of-QListWidgetItem """
        pass

    def indexFromItem(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.indexFromItem(QListWidgetItem) -> QModelIndex """
        pass

    def insertItem(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QListWidget.insertItem(int, QListWidgetItem)
        QListWidget.insertItem(int, QString)
        """
        pass

    def insertItems(self, p_int, QStringList): # real signature unknown; restored from __doc__
        """ QListWidget.insertItems(int, QStringList) """
        pass

    def isItemHidden(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.isItemHidden(QListWidgetItem) -> bool """
        return False

    def isItemSelected(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.isItemSelected(QListWidgetItem) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ QListWidget.isSortingEnabled() -> bool """
        return False

    def item(self, p_int): # real signature unknown; restored from __doc__
        """ QListWidget.item(int) -> QListWidgetItem """
        return QListWidgetItem

    def itemActivated(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemActivated[QListWidgetItem] [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QListWidget.itemAt(QPoint) -> QListWidgetItem
        QListWidget.itemAt(int, int) -> QListWidgetItem
        """
        return QListWidgetItem

    def itemChanged(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemChanged[QListWidgetItem] [signal] """
        pass

    def itemClicked(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemClicked[QListWidgetItem] [signal] """
        pass

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemDoubleClicked[QListWidgetItem] [signal] """
        pass

    def itemEntered(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemEntered[QListWidgetItem] [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QListWidget.itemFromIndex(QModelIndex) -> QListWidgetItem """
        return QListWidgetItem

    def itemPressed(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemPressed[QListWidgetItem] [signal] """
        pass

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ QListWidget.items(QMimeData) -> list-of-QListWidgetItem """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        """ QListWidget.itemSelectionChanged [signal] """
        pass

    def itemWidget(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.itemWidget(QListWidgetItem) -> QWidget """
        return QWidget

    def mimeData(self, list_of_QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.mimeData(list-of-QListWidgetItem) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QListWidget.mimeTypes() -> QStringList """
        pass

    def openPersistentEditor(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.openPersistentEditor(QListWidgetItem) """
        pass

    def removeItemWidget(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.removeItemWidget(QListWidgetItem) """
        pass

    def row(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.row(QListWidgetItem) -> int """
        return 0

    def scrollToItem(self, QListWidgetItem, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QListWidget.scrollToItem(QListWidgetItem, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ QListWidget.selectedItems() -> list-of-QListWidgetItem """
        pass

    def setCurrentItem(self, QListWidgetItem, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QListWidget.setCurrentItem(QListWidgetItem)
        QListWidget.setCurrentItem(QListWidgetItem, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setCurrentRow(self, p_int, QItemSelectionModel_SelectionFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QListWidget.setCurrentRow(int)
        QListWidget.setCurrentRow(int, QItemSelectionModel.SelectionFlags)
        """
        pass

    def setItemHidden(self, QListWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QListWidget.setItemHidden(QListWidgetItem, bool) """
        pass

    def setItemSelected(self, QListWidgetItem, bool): # real signature unknown; restored from __doc__
        """ QListWidget.setItemSelected(QListWidgetItem, bool) """
        pass

    def setItemWidget(self, QListWidgetItem, QWidget): # real signature unknown; restored from __doc__
        """ QListWidget.setItemWidget(QListWidgetItem, QWidget) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QListWidget.setSortingEnabled(bool) """
        pass

    def sortItems(self, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QListWidget.sortItems(Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QListWidget.supportedDropActions() -> Qt.DropActions """
        pass

    def takeItem(self, p_int): # real signature unknown; restored from __doc__
        """ QListWidget.takeItem(int) -> QListWidgetItem """
        return QListWidgetItem

    def visualItemRect(self, QListWidgetItem): # real signature unknown; restored from __doc__
        """ QListWidget.visualItemRect(QListWidgetItem) -> QRect """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


