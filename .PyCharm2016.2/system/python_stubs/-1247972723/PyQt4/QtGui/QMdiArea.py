# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QAbstractScrollArea import QAbstractScrollArea

class QMdiArea(QAbstractScrollArea):
    """ QMdiArea(QWidget parent=None) """
    def activateNextSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activateNextSubWindow() """
        pass

    def activatePreviousSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activatePreviousSubWindow() """
        pass

    def activationOrder(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activationOrder() -> QMdiArea.WindowOrder """
        pass

    def activeSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.activeSubWindow() -> QMdiSubWindow """
        return QMdiSubWindow

    def addSubWindow(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QMdiArea.addSubWindow(QWidget, Qt.WindowFlags flags=0) -> QMdiSubWindow """
        return QMdiSubWindow

    def background(self): # real signature unknown; restored from __doc__
        """ QMdiArea.background() -> QBrush """
        return QBrush

    def cascadeSubWindows(self): # real signature unknown; restored from __doc__
        """ QMdiArea.cascadeSubWindows() """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.childEvent(QChildEvent) """
        pass

    def closeActiveSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.closeActiveSubWindow() """
        pass

    def closeAllSubWindows(self): # real signature unknown; restored from __doc__
        """ QMdiArea.closeAllSubWindows() """
        pass

    def currentSubWindow(self): # real signature unknown; restored from __doc__
        """ QMdiArea.currentSubWindow() -> QMdiSubWindow """
        return QMdiSubWindow

    def documentMode(self): # real signature unknown; restored from __doc__
        """ QMdiArea.documentMode() -> bool """
        return False

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.eventFilter(QObject, QEvent) -> bool """
        return False

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QMdiArea.minimumSizeHint() -> QSize """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.paintEvent(QPaintEvent) """
        pass

    def removeSubWindow(self, QWidget): # real signature unknown; restored from __doc__
        """ QMdiArea.removeSubWindow(QWidget) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.resizeEvent(QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QMdiArea.scrollContentsBy(int, int) """
        pass

    def setActivationOrder(self, QMdiArea_WindowOrder): # real signature unknown; restored from __doc__
        """ QMdiArea.setActivationOrder(QMdiArea.WindowOrder) """
        pass

    def setActiveSubWindow(self, QMdiSubWindow): # real signature unknown; restored from __doc__
        """ QMdiArea.setActiveSubWindow(QMdiSubWindow) """
        pass

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QMdiArea.setBackground(QBrush) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ QMdiArea.setDocumentMode(bool) """
        pass

    def setOption(self, QMdiArea_AreaOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QMdiArea.setOption(QMdiArea.AreaOption, bool on=True) """
        pass

    def setTabPosition(self, QTabWidget_TabPosition): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabPosition(QTabWidget.TabPosition) """
        pass

    def setTabsClosable(self, bool): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabsClosable(bool) """
        pass

    def setTabShape(self, QTabWidget_TabShape): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabShape(QTabWidget.TabShape) """
        pass

    def setTabsMovable(self, bool): # real signature unknown; restored from __doc__
        """ QMdiArea.setTabsMovable(bool) """
        pass

    def setupViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ QMdiArea.setupViewport(QWidget) """
        pass

    def setViewMode(self, QMdiArea_ViewMode): # real signature unknown; restored from __doc__
        """ QMdiArea.setViewMode(QMdiArea.ViewMode) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMdiArea.sizeHint() -> QSize """
        pass

    def subWindowActivated(self, *args, **kwargs): # real signature unknown
        """ QMdiArea.subWindowActivated[QMdiSubWindow] [signal] """
        pass

    def subWindowList(self, QMdiArea_WindowOrder_order=None): # real signature unknown; restored from __doc__
        """ QMdiArea.subWindowList(QMdiArea.WindowOrder order=QMdiArea.CreationOrder) -> list-of-QMdiSubWindow """
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabPosition() -> QTabWidget.TabPosition """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabsClosable() -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabShape() -> QTabWidget.TabShape """
        pass

    def tabsMovable(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tabsMovable() -> bool """
        return False

    def testOption(self, QMdiArea_AreaOption): # real signature unknown; restored from __doc__
        """ QMdiArea.testOption(QMdiArea.AreaOption) -> bool """
        return False

    def tileSubWindows(self): # real signature unknown; restored from __doc__
        """ QMdiArea.tileSubWindows() """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.timerEvent(QTimerEvent) """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QMdiArea.viewMode() -> QMdiArea.ViewMode """
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMdiArea.viewportEvent(QEvent) -> bool """
        return False

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    ActivationHistoryOrder = 2
    CreationOrder = 0
    DontMaximizeSubWindowOnActivation = 1
    StackingOrder = 1
    SubWindowView = 0
    TabbedView = 1


