# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QTabBar(QWidget):
    """ QTabBar(QWidget parent=None) """
    def addTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTabBar.addTab(QString) -> int
        QTabBar.addTab(QIcon, QString) -> int
        """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QTabBar.changeEvent(QEvent) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QTabBar.count() -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QTabBar.currentChanged[int] [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QTabBar.currentIndex() -> int """
        return 0

    def documentMode(self): # real signature unknown; restored from __doc__
        """ QTabBar.documentMode() -> bool """
        return False

    def drawBase(self): # real signature unknown; restored from __doc__
        """ QTabBar.drawBase() -> bool """
        return False

    def elideMode(self): # real signature unknown; restored from __doc__
        """ QTabBar.elideMode() -> Qt.TextElideMode """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QTabBar.event(QEvent) -> bool """
        return False

    def expanding(self): # real signature unknown; restored from __doc__
        """ QTabBar.expanding() -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QTabBar.hideEvent(QHideEvent) """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QTabBar.iconSize() -> QSize """
        pass

    def initStyleOption(self, QStyleOptionTab, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.initStyleOption(QStyleOptionTab, int) """
        pass

    def insertTab(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTabBar.insertTab(int, QString) -> int
        QTabBar.insertTab(int, QIcon, QString) -> int
        """
        return 0

    def isMovable(self): # real signature unknown; restored from __doc__
        """ QTabBar.isMovable() -> bool """
        return False

    def isTabEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.isTabEnabled(int) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QTabBar.keyPressEvent(QKeyEvent) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QTabBar.minimumSizeHint() -> QSize """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTabBar.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTabBar.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QTabBar.mouseReleaseEvent(QMouseEvent) """
        pass

    def moveTab(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTabBar.moveTab(int, int) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QTabBar.paintEvent(QPaintEvent) """
        pass

    def removeTab(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.removeTab(int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QTabBar.resizeEvent(QResizeEvent) """
        pass

    def selectionBehaviorOnRemove(self): # real signature unknown; restored from __doc__
        """ QTabBar.selectionBehaviorOnRemove() -> QTabBar.SelectionBehavior """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.setCurrentIndex(int) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setDocumentMode(bool) """
        pass

    def setDrawBase(self, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setDrawBase(bool) """
        pass

    def setElideMode(self, Qt_TextElideMode): # real signature unknown; restored from __doc__
        """ QTabBar.setElideMode(Qt.TextElideMode) """
        pass

    def setExpanding(self, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setExpanding(bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QTabBar.setIconSize(QSize) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setMovable(bool) """
        pass

    def setSelectionBehaviorOnRemove(self, QTabBar_SelectionBehavior): # real signature unknown; restored from __doc__
        """ QTabBar.setSelectionBehaviorOnRemove(QTabBar.SelectionBehavior) """
        pass

    def setShape(self, QTabBar_Shape): # real signature unknown; restored from __doc__
        """ QTabBar.setShape(QTabBar.Shape) """
        pass

    def setTabButton(self, p_int, QTabBar_ButtonPosition, QWidget): # real signature unknown; restored from __doc__
        """ QTabBar.setTabButton(int, QTabBar.ButtonPosition, QWidget) """
        pass

    def setTabData(self, p_int, QVariant): # real signature unknown; restored from __doc__
        """ QTabBar.setTabData(int, QVariant) """
        pass

    def setTabEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setTabEnabled(int, bool) """
        pass

    def setTabIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QTabBar.setTabIcon(int, QIcon) """
        pass

    def setTabsClosable(self, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setTabsClosable(bool) """
        pass

    def setTabText(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTabBar.setTabText(int, QString) """
        pass

    def setTabTextColor(self, p_int, QColor): # real signature unknown; restored from __doc__
        """ QTabBar.setTabTextColor(int, QColor) """
        pass

    def setTabToolTip(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTabBar.setTabToolTip(int, QString) """
        pass

    def setTabWhatsThis(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTabBar.setTabWhatsThis(int, QString) """
        pass

    def setUsesScrollButtons(self, bool): # real signature unknown; restored from __doc__
        """ QTabBar.setUsesScrollButtons(bool) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QTabBar.shape() -> QTabBar.Shape """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QTabBar.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QTabBar.sizeHint() -> QSize """
        pass

    def tabAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QTabBar.tabAt(QPoint) -> int """
        return 0

    def tabButton(self, p_int, QTabBar_ButtonPosition): # real signature unknown; restored from __doc__
        """ QTabBar.tabButton(int, QTabBar.ButtonPosition) -> QWidget """
        return QWidget

    def tabCloseRequested(self, *args, **kwargs): # real signature unknown
        """ QTabBar.tabCloseRequested[int] [signal] """
        pass

    def tabData(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabData(int) -> QVariant """
        pass

    def tabIcon(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabIcon(int) -> QIcon """
        return QIcon

    def tabInserted(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabInserted(int) """
        pass

    def tabLayoutChange(self): # real signature unknown; restored from __doc__
        """ QTabBar.tabLayoutChange() """
        pass

    def tabMoved(self, *args, **kwargs): # real signature unknown
        """ QTabBar.tabMoved[int, int] [signal] """
        pass

    def tabRect(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabRect(int) -> QRect """
        pass

    def tabRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabRemoved(int) """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ QTabBar.tabsClosable() -> bool """
        return False

    def tabSizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabSizeHint(int) -> QSize """
        pass

    def tabText(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabText(int) -> QString """
        pass

    def tabTextColor(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabTextColor(int) -> QColor """
        return QColor

    def tabToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabToolTip(int) -> QString """
        pass

    def tabWhatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ QTabBar.tabWhatsThis(int) -> QString """
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ QTabBar.usesScrollButtons() -> bool """
        return False

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QTabBar.wheelEvent(QWheelEvent) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    LeftSide = 0
    RightSide = 1
    RoundedEast = 3
    RoundedNorth = 0
    RoundedSouth = 1
    RoundedWest = 2
    SelectLeftTab = 0
    SelectPreviousTab = 2
    SelectRightTab = 1
    TriangularEast = 7
    TriangularNorth = 4
    TriangularSouth = 5
    TriangularWest = 6


