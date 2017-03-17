# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractItemView import QAbstractItemView

class QHeaderView(QAbstractItemView):
    """ QHeaderView(Qt.Orientation, QWidget parent=None) """
    def cascadingSectionResizes(self): # real signature unknown; restored from __doc__
        """ QHeaderView.cascadingSectionResizes() -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ QHeaderView.count() -> int """
        return 0

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QHeaderView.currentChanged(QModelIndex, QModelIndex) """
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QHeaderView.dataChanged(QModelIndex, QModelIndex) """
        pass

    def defaultAlignment(self): # real signature unknown; restored from __doc__
        """ QHeaderView.defaultAlignment() -> Qt.Alignment """
        pass

    def defaultSectionSize(self): # real signature unknown; restored from __doc__
        """ QHeaderView.defaultSectionSize() -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.event(QEvent) -> bool """
        return False

    def geometriesChanged(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.geometriesChanged [signal] """
        pass

    def headerDataChanged(self, Qt_Orientation, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.headerDataChanged(Qt.Orientation, int, int) """
        pass

    def hiddenSectionCount(self): # real signature unknown; restored from __doc__
        """ QHeaderView.hiddenSectionCount() -> int """
        return 0

    def hideSection(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.hideSection(int) """
        pass

    def highlightSections(self): # real signature unknown; restored from __doc__
        """ QHeaderView.highlightSections() -> bool """
        return False

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ QHeaderView.horizontalOffset() -> int """
        return 0

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QHeaderView.indexAt(QPoint) -> QModelIndex """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ QHeaderView.initialize() """
        pass

    def initializeSections(self, p_int=None, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHeaderView.initializeSections()
        QHeaderView.initializeSections(int, int)
        """
        pass

    def initStyleOption(self, QStyleOptionHeader): # real signature unknown; restored from __doc__
        """ QHeaderView.initStyleOption(QStyleOptionHeader) """
        pass

    def isClickable(self): # real signature unknown; restored from __doc__
        """ QHeaderView.isClickable() -> bool """
        return False

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QHeaderView.isIndexHidden(QModelIndex) -> bool """
        return False

    def isMovable(self): # real signature unknown; restored from __doc__
        """ QHeaderView.isMovable() -> bool """
        return False

    def isSectionHidden(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.isSectionHidden(int) -> bool """
        return False

    def isSortIndicatorShown(self): # real signature unknown; restored from __doc__
        """ QHeaderView.isSortIndicatorShown() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QHeaderView.length() -> int """
        return 0

    def logicalIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.logicalIndex(int) -> int """
        return 0

    def logicalIndexAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHeaderView.logicalIndexAt(int) -> int
        QHeaderView.logicalIndexAt(int, int) -> int
        QHeaderView.logicalIndexAt(QPoint) -> int
        """
        return 0

    def minimumSectionSize(self): # real signature unknown; restored from __doc__
        """ QHeaderView.minimumSectionSize() -> int """
        return 0

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveCursor(self, QAbstractItemView_CursorAction, Qt_KeyboardModifiers): # real signature unknown; restored from __doc__
        """ QHeaderView.moveCursor(QAbstractItemView.CursorAction, Qt.KeyboardModifiers) -> QModelIndex """
        pass

    def moveSection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.moveSection(int, int) """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ QHeaderView.offset() -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ QHeaderView.orientation() -> Qt.Orientation """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.paintEvent(QPaintEvent) """
        pass

    def paintSection(self, QPainter, QRect, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.paintSection(QPainter, QRect, int) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QHeaderView.reset() """
        pass

    def resizeMode(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.resizeMode(int) -> QHeaderView.ResizeMode """
        pass

    def resizeSection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.resizeSection(int, int) """
        pass

    def resizeSections(self, QHeaderView_ResizeMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHeaderView.resizeSections()
        QHeaderView.resizeSections(QHeaderView.ResizeMode)
        """
        pass

    def restoreState(self, QByteArray): # real signature unknown; restored from __doc__
        """ QHeaderView.restoreState(QByteArray) -> bool """
        return False

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.rowsInserted(QModelIndex, int, int) """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ QHeaderView.saveState() -> QByteArray """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.scrollContentsBy(int, int) """
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint): # real signature unknown; restored from __doc__
        """ QHeaderView.scrollTo(QModelIndex, QAbstractItemView.ScrollHint) """
        pass

    def sectionAutoResize(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionAutoResize[int, QHeaderView.ResizeMode] [signal] """
        pass

    def sectionClicked(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionClicked[int] [signal] """
        pass

    def sectionCountChanged(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionCountChanged[int, int] [signal] """
        pass

    def sectionDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionDoubleClicked[int] [signal] """
        pass

    def sectionEntered(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionEntered[int] [signal] """
        pass

    def sectionHandleDoubleClicked(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionHandleDoubleClicked[int] [signal] """
        pass

    def sectionMoved(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionMoved[int, int, int] [signal] """
        pass

    def sectionPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionPosition(int) -> int """
        return 0

    def sectionPressed(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionPressed[int] [signal] """
        pass

    def sectionResized(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sectionResized[int, int, int] [signal] """
        pass

    def sectionsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionsAboutToBeRemoved(QModelIndex, int, int) """
        pass

    def sectionsHidden(self): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionsHidden() -> bool """
        return False

    def sectionsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionsInserted(QModelIndex, int, int) """
        pass

    def sectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionSize(int) -> int """
        return 0

    def sectionSizeFromContents(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionSizeFromContents(int) -> QSize """
        pass

    def sectionSizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionSizeHint(int) -> int """
        return 0

    def sectionsMoved(self): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionsMoved() -> bool """
        return False

    def sectionViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.sectionViewportPosition(int) -> int """
        return 0

    def setCascadingSectionResizes(self, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setCascadingSectionResizes(bool) """
        pass

    def setClickable(self, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setClickable(bool) """
        pass

    def setDefaultAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QHeaderView.setDefaultAlignment(Qt.Alignment) """
        pass

    def setDefaultSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.setDefaultSectionSize(int) """
        pass

    def setHighlightSections(self, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setHighlightSections(bool) """
        pass

    def setMinimumSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.setMinimumSectionSize(int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QHeaderView.setModel(QAbstractItemModel) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setMovable(bool) """
        pass

    def setOffset(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.setOffset(int) """
        pass

    def setOffsetToLastSection(self): # real signature unknown; restored from __doc__
        """ QHeaderView.setOffsetToLastSection() """
        pass

    def setOffsetToSectionPosition(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.setOffsetToSectionPosition(int) """
        pass

    def setResizeMode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHeaderView.setResizeMode(QHeaderView.ResizeMode)
        QHeaderView.setResizeMode(int, QHeaderView.ResizeMode)
        """
        pass

    def setSectionHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setSectionHidden(int, bool) """
        pass

    def setSelection(self, QRect, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QHeaderView.setSelection(QRect, QItemSelectionModel.SelectionFlags) """
        pass

    def setSortIndicator(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ QHeaderView.setSortIndicator(int, Qt.SortOrder) """
        pass

    def setSortIndicatorShown(self, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setSortIndicatorShown(bool) """
        pass

    def setStretchLastSection(self, bool): # real signature unknown; restored from __doc__
        """ QHeaderView.setStretchLastSection(bool) """
        pass

    def showSection(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.showSection(int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QHeaderView.sizeHint() -> QSize """
        pass

    def sortIndicatorChanged(self, *args, **kwargs): # real signature unknown
        """ QHeaderView.sortIndicatorChanged[int, Qt.SortOrder] [signal] """
        pass

    def sortIndicatorOrder(self): # real signature unknown; restored from __doc__
        """ QHeaderView.sortIndicatorOrder() -> Qt.SortOrder """
        pass

    def sortIndicatorSection(self): # real signature unknown; restored from __doc__
        """ QHeaderView.sortIndicatorSection() -> int """
        return 0

    def stretchLastSection(self): # real signature unknown; restored from __doc__
        """ QHeaderView.stretchLastSection() -> bool """
        return False

    def stretchSectionCount(self): # real signature unknown; restored from __doc__
        """ QHeaderView.stretchSectionCount() -> int """
        return 0

    def swapSections(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHeaderView.swapSections(int, int) """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ QHeaderView.updateGeometries() """
        pass

    def updateSection(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.updateSection(int) """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ QHeaderView.verticalOffset() -> int """
        return 0

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QHeaderView.viewportEvent(QEvent) -> bool """
        return False

    def visualIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.visualIndex(int) -> int """
        return 0

    def visualIndexAt(self, p_int): # real signature unknown; restored from __doc__
        """ QHeaderView.visualIndexAt(int) -> int """
        return 0

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QHeaderView.visualRect(QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QHeaderView.visualRegionForSelection(QItemSelection) -> QRegion """
        return QRegion

    def __init__(self, Qt_Orientation, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    Custom = 2
    Fixed = 2
    Interactive = 0
    ResizeToContents = 3
    Stretch = 1


