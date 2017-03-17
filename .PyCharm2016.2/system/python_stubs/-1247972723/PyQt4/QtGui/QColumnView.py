# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemView import QAbstractItemView

class QColumnView(QAbstractItemView):
    """ QColumnView(QWidget parent=None) """
    def columnWidths(self): # real signature unknown; restored from __doc__
        """ QColumnView.columnWidths() -> list-of-int """
        pass

    def createColumn(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QColumnView.createColumn(QModelIndex) -> QAbstractItemView """
        return QAbstractItemView

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QColumnView.currentChanged(QModelIndex, QModelIndex) """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ QColumnView.horizontalOffset() -> int """
        return 0

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QColumnView.indexAt(QPoint) -> QModelIndex """
        pass

    def initializeColumn(self, QAbstractItemView): # real signature unknown; restored from __doc__
        """ QColumnView.initializeColumn(QAbstractItemView) """
        pass

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QColumnView.isIndexHidden(QModelIndex) -> bool """
        return False

    def moveCursor(self, QAbstractItemView_CursorAction, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QColumnView.moveCursor(QAbstractItemView.CursorAction, Qt.KeyboardModifiers) -> QModelIndex """
        pass

    def previewWidget(self): # real signature unknown; restored from __doc__
        """ QColumnView.previewWidget() -> QWidget """
        return QWidget

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QColumnView.resizeEvent(QResizeEvent) """
        pass

    def resizeGripsVisible(self): # real signature unknown; restored from __doc__
        """ QColumnView.resizeGripsVisible() -> bool """
        return False

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QColumnView.rowsInserted(QModelIndex, int, int) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QColumnView.scrollContentsBy(int, int) """
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QColumnView.scrollTo(QModelIndex, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ QColumnView.selectAll() """
        pass

    def setColumnWidths(self, list_of_int): # real signature unknown; restored from __doc__
        """ QColumnView.setColumnWidths(list-of-int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QColumnView.setModel(QAbstractItemModel) """
        pass

    def setPreviewWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QColumnView.setPreviewWidget(QWidget) """
        pass

    def setResizeGripsVisible(self, bool): # real signature unknown; restored from __doc__
        """ QColumnView.setResizeGripsVisible(bool) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QColumnView.setRootIndex(QModelIndex) """
        pass

    def setSelection(self, QRect, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QColumnView.setSelection(QRect, QItemSelectionModel.SelectionFlags) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ QColumnView.setSelectionModel(QItemSelectionModel) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QColumnView.sizeHint() -> QSize """
        pass

    def updatePreviewWidget(self, *args, **kwargs): # real signature unknown
        """ QColumnView.updatePreviewWidget[QModelIndex] [signal] """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ QColumnView.verticalOffset() -> int """
        return 0

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QColumnView.visualRect(QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QColumnView.visualRegionForSelection(QItemSelection) -> QRegion """
        return QRegion

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


