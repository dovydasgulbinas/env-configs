# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QAbstractItemView(QAbstractScrollArea):
    """ QAbstractItemView(QWidget parent=None) """
    def activated(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemView.activated[QModelIndex] [signal] """
        pass

    def alternatingRowColors(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.alternatingRowColors() -> bool """
        return False

    def autoScrollMargin(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.autoScrollMargin() -> int """
        return 0

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.clearSelection() """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemView.clicked[QModelIndex] [signal] """
        pass

    def closeEditor(self, QWidget, QAbstractItemDelegate_EndEditHint): # real signature unknown; restored from __doc__
        """ QAbstractItemView.closeEditor(QWidget, QAbstractItemDelegate.EndEditHint) """
        pass

    def closePersistentEditor(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.closePersistentEditor(QModelIndex) """
        pass

    def commitData(self, QWidget): # real signature unknown; restored from __doc__
        """ QAbstractItemView.commitData(QWidget) """
        pass

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractItemView.currentChanged(QModelIndex, QModelIndex) """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.currentIndex() -> QModelIndex """
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dataChanged(QModelIndex, QModelIndex) """
        pass

    def defaultDropAction(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.defaultDropAction() -> Qt.DropAction """
        pass

    def dirtyRegionOffset(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dirtyRegionOffset() -> QPoint """
        pass

    def doubleClicked(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemView.doubleClicked[QModelIndex] [signal] """
        pass

    def dragDropMode(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dragDropMode() -> QAbstractItemView.DragDropMode """
        pass

    def dragDropOverwriteMode(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dragDropOverwriteMode() -> bool """
        return False

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dragEnabled() -> bool """
        return False

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dragMoveEvent(QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dropEvent(QDropEvent) """
        pass

    def dropIndicatorPosition(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.dropIndicatorPosition() -> QAbstractItemView.DropIndicatorPosition """
        pass

    def edit(self, QModelIndex, QAbstractItemView_EditTrigger=None, QEvent=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractItemView.edit(QModelIndex)
        QAbstractItemView.edit(QModelIndex, QAbstractItemView.EditTrigger, QEvent) -> bool
        """
        return False

    def editorDestroyed(self, QObject): # real signature unknown; restored from __doc__
        """ QAbstractItemView.editorDestroyed(QObject) """
        pass

    def editTriggers(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.editTriggers() -> QAbstractItemView.EditTriggers """
        pass

    def entered(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemView.entered[QModelIndex] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.event(QEvent) -> bool """
        return False

    def executeDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.executeDelayedItemsLayout() """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.focusOutEvent(QFocusEvent) """
        pass

    def hasAutoScroll(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.hasAutoScroll() -> bool """
        return False

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.horizontalOffset() -> int """
        return 0

    def horizontalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.horizontalScrollbarAction(int) """
        pass

    def horizontalScrollbarValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.horizontalScrollbarValueChanged(int) """
        pass

    def horizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.horizontalScrollMode() -> QAbstractItemView.ScrollMode """
        pass

    def horizontalStepsPerItem(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.horizontalStepsPerItem() -> int """
        return 0

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.iconSize() -> QSize """
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QAbstractItemView.indexAt(QPoint) -> QModelIndex """
        pass

    def indexWidget(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.indexWidget(QModelIndex) -> QWidget """
        return QWidget

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QAbstractItemView.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.isIndexHidden(QModelIndex) -> bool """
        return False

    def itemDelegate(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractItemView.itemDelegate() -> QAbstractItemDelegate
        QAbstractItemView.itemDelegate(QModelIndex) -> QAbstractItemDelegate
        """
        return QAbstractItemDelegate

    def itemDelegateForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.itemDelegateForColumn(int) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def itemDelegateForRow(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.itemDelegateForRow(int) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def keyboardSearch(self, QString): # real signature unknown; restored from __doc__
        """ QAbstractItemView.keyboardSearch(QString) """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.keyPressEvent(QKeyEvent) """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.model() -> QAbstractItemModel """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveCursor(self, QAbstractItemView_CursorAction, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QAbstractItemView.moveCursor(QAbstractItemView.CursorAction, Qt.KeyboardModifiers) -> QModelIndex """
        pass

    def openPersistentEditor(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.openPersistentEditor(QModelIndex) """
        pass

    def pressed(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemView.pressed[QModelIndex] [signal] """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.reset() """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.resizeEvent(QResizeEvent) """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.rootIndex() -> QModelIndex """
        pass

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemView.rowsAboutToBeRemoved(QModelIndex, int, int) """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemView.rowsInserted(QModelIndex, int, int) """
        pass

    def scheduleDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.scheduleDelayedItemsLayout() """
        pass

    def scrollDirtyRegion(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractItemView.scrollDirtyRegion(int, int) """
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint_hint=None): # real signature unknown; restored from __doc__
        """ QAbstractItemView.scrollTo(QModelIndex, QAbstractItemView.ScrollHint hint=QAbstractItemView.EnsureVisible) """
        pass

    def scrollToBottom(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.scrollToBottom() """
        pass

    def scrollToTop(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.scrollToTop() """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectAll() """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectedIndexes() -> list-of-QModelIndex """
        pass

    def selectionBehavior(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectionBehavior() -> QAbstractItemView.SelectionBehavior """
        pass

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectionChanged(QItemSelection, QItemSelection) """
        pass

    def selectionCommand(self, QModelIndex, QEvent_event=None): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectionCommand(QModelIndex, QEvent event=None) -> QItemSelectionModel.SelectionFlags """
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectionMode() -> QAbstractItemView.SelectionMode """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.selectionModel() -> QItemSelectionModel """
        return QItemSelectionModel

    def setAlternatingRowColors(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setAlternatingRowColors(bool) """
        pass

    def setAutoScroll(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setAutoScroll(bool) """
        pass

    def setAutoScrollMargin(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setAutoScrollMargin(int) """
        pass

    def setCurrentIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setCurrentIndex(QModelIndex) """
        pass

    def setDefaultDropAction(self, Qt_DropAction): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setDefaultDropAction(Qt.DropAction) """
        pass

    def setDirtyRegion(self, QRegion): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setDirtyRegion(QRegion) """
        pass

    def setDragDropMode(self, QAbstractItemView_DragDropMode): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setDragDropMode(QAbstractItemView.DragDropMode) """
        pass

    def setDragDropOverwriteMode(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setDragDropOverwriteMode(bool) """
        pass

    def setDragEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setDragEnabled(bool) """
        pass

    def setDropIndicatorShown(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setDropIndicatorShown(bool) """
        pass

    def setEditTriggers(self, QAbstractItemView_EditTriggers): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setEditTriggers(QAbstractItemView.EditTriggers) """
        pass

    def setHorizontalScrollMode(self, QAbstractItemView_ScrollMode): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setHorizontalScrollMode(QAbstractItemView.ScrollMode) """
        pass

    def setHorizontalStepsPerItem(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setHorizontalStepsPerItem(int) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setIconSize(QSize) """
        pass

    def setIndexWidget(self, QModelIndex, QWidget): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setIndexWidget(QModelIndex, QWidget) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setItemDelegate(QAbstractItemDelegate) """
        pass

    def setItemDelegateForColumn(self, p_int, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setItemDelegateForColumn(int, QAbstractItemDelegate) """
        pass

    def setItemDelegateForRow(self, p_int, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setItemDelegateForRow(int, QAbstractItemDelegate) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setModel(QAbstractItemModel) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setRootIndex(QModelIndex) """
        pass

    def setSelection(self, QRect, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setSelection(QRect, QItemSelectionModel.SelectionFlags) """
        pass

    def setSelectionBehavior(self, QAbstractItemView_SelectionBehavior): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setSelectionBehavior(QAbstractItemView.SelectionBehavior) """
        pass

    def setSelectionMode(self, QAbstractItemView_SelectionMode): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setSelectionMode(QAbstractItemView.SelectionMode) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setSelectionModel(QItemSelectionModel) """
        pass

    def setState(self, QAbstractItemView_State): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setState(QAbstractItemView.State) """
        pass

    def setTabKeyNavigation(self, bool): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setTabKeyNavigation(bool) """
        pass

    def setTextElideMode(self, Qt_TextElideMode): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setTextElideMode(Qt.TextElideMode) """
        pass

    def setVerticalScrollMode(self, QAbstractItemView_ScrollMode): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setVerticalScrollMode(QAbstractItemView.ScrollMode) """
        pass

    def setVerticalStepsPerItem(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.setVerticalStepsPerItem(int) """
        pass

    def showDropIndicator(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.showDropIndicator() -> bool """
        return False

    def sizeHintForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.sizeHintForColumn(int) -> int """
        return 0

    def sizeHintForIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.sizeHintForIndex(QModelIndex) -> QSize """
        pass

    def sizeHintForRow(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.sizeHintForRow(int) -> int """
        return 0

    def startDrag(self, Qt_DropActions): # real signature unknown; restored from __doc__
        """ QAbstractItemView.startDrag(Qt.DropActions) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.state() -> QAbstractItemView.State """
        pass

    def tabKeyNavigation(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.tabKeyNavigation() -> bool """
        return False

    def textElideMode(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.textElideMode() -> Qt.TextElideMode """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.timerEvent(QTimerEvent) """
        pass

    def update(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAbstractItemView.update()
        QAbstractItemView.update(QModelIndex)
        """
        pass

    def updateEditorData(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.updateEditorData() """
        pass

    def updateEditorGeometries(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.updateEditorGeometries() """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.updateGeometries() """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.verticalOffset() -> int """
        return 0

    def verticalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.verticalScrollbarAction(int) """
        pass

    def verticalScrollbarValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractItemView.verticalScrollbarValueChanged(int) """
        pass

    def verticalScrollMode(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.verticalScrollMode() -> QAbstractItemView.ScrollMode """
        pass

    def verticalStepsPerItem(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.verticalStepsPerItem() -> int """
        return 0

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ QAbstractItemView.viewOptions() -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportEntered(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemView.viewportEntered [signal] """
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QAbstractItemView.viewportEvent(QEvent) -> bool """
        return False

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemView.visualRect(QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QAbstractItemView.visualRegionForSelection(QItemSelection) -> QRegion """
        return QRegion

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    AboveItem = 1
    AllEditTriggers = 31
    AnimatingState = 6
    AnyKeyPressed = 16
    BelowItem = 2
    CollapsingState = 5
    ContiguousSelection = 4
    CurrentChanged = 1
    DoubleClicked = 2
    DragDrop = 3
    DraggingState = 1
    DragOnly = 1
    DragSelectingState = 2
    DropOnly = 2
    EditingState = 3
    EditKeyPressed = 8
    EnsureVisible = 0
    ExpandingState = 4
    ExtendedSelection = 3
    InternalMove = 4
    MoveDown = 1
    MoveEnd = 5
    MoveHome = 4
    MoveLeft = 2
    MoveNext = 8
    MovePageDown = 7
    MovePageUp = 6
    MovePrevious = 9
    MoveRight = 3
    MoveUp = 0
    MultiSelection = 2
    NoDragDrop = 0
    NoEditTriggers = 0
    NoSelection = 0
    NoState = 0
    OnItem = 0
    OnViewport = 3
    PositionAtBottom = 2
    PositionAtCenter = 3
    PositionAtTop = 1
    ScrollPerItem = 0
    ScrollPerPixel = 1
    SelectColumns = 2
    SelectedClicked = 4
    SelectItems = 0
    SelectRows = 1
    SingleSelection = 1


