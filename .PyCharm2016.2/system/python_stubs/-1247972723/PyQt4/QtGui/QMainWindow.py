# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QMainWindow(QWidget):
    """ QMainWindow(QWidget parent=None, Qt.WindowFlags flags=0) """
    def addDockWidget(self, Qt_DockWidgetArea, QDockWidget, Qt_Orientation=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMainWindow.addDockWidget(Qt.DockWidgetArea, QDockWidget)
        QMainWindow.addDockWidget(Qt.DockWidgetArea, QDockWidget, Qt.Orientation)
        """
        pass

    def addToolBar(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMainWindow.addToolBar(Qt.ToolBarArea, QToolBar)
        QMainWindow.addToolBar(QToolBar)
        QMainWindow.addToolBar(QString) -> QToolBar
        """
        return QToolBar

    def addToolBarBreak(self, Qt_ToolBarArea_area=None): # real signature unknown; restored from __doc__
        """ QMainWindow.addToolBarBreak(Qt.ToolBarArea area=Qt.TopToolBarArea) """
        pass

    def centralWidget(self): # real signature unknown; restored from __doc__
        """ QMainWindow.centralWidget() -> QWidget """
        return QWidget

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QMainWindow.contextMenuEvent(QContextMenuEvent) """
        pass

    def corner(self, Qt_Corner): # real signature unknown; restored from __doc__
        """ QMainWindow.corner(Qt.Corner) -> Qt.DockWidgetArea """
        pass

    def createPopupMenu(self): # real signature unknown; restored from __doc__
        """ QMainWindow.createPopupMenu() -> QMenu """
        return QMenu

    def dockOptions(self): # real signature unknown; restored from __doc__
        """ QMainWindow.dockOptions() -> QMainWindow.DockOptions """
        pass

    def dockWidgetArea(self, QDockWidget): # real signature unknown; restored from __doc__
        """ QMainWindow.dockWidgetArea(QDockWidget) -> Qt.DockWidgetArea """
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ QMainWindow.documentMode() -> bool """
        return False

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QMainWindow.event(QEvent) -> bool """
        return False

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QMainWindow.iconSize() -> QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
        """ QMainWindow.iconSizeChanged[QSize] [signal] """
        pass

    def insertToolBar(self, QToolBar, QToolBar_1): # real signature unknown; restored from __doc__
        """ QMainWindow.insertToolBar(QToolBar, QToolBar) """
        pass

    def insertToolBarBreak(self, QToolBar): # real signature unknown; restored from __doc__
        """ QMainWindow.insertToolBarBreak(QToolBar) """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ QMainWindow.isAnimated() -> bool """
        return False

    def isDockNestingEnabled(self): # real signature unknown; restored from __doc__
        """ QMainWindow.isDockNestingEnabled() -> bool """
        return False

    def isSeparator(self, QPoint): # real signature unknown; restored from __doc__
        """ QMainWindow.isSeparator(QPoint) -> bool """
        return False

    def menuBar(self): # real signature unknown; restored from __doc__
        """ QMainWindow.menuBar() -> QMenuBar """
        return QMenuBar

    def menuWidget(self): # real signature unknown; restored from __doc__
        """ QMainWindow.menuWidget() -> QWidget """
        return QWidget

    def removeDockWidget(self, QDockWidget): # real signature unknown; restored from __doc__
        """ QMainWindow.removeDockWidget(QDockWidget) """
        pass

    def removeToolBar(self, QToolBar): # real signature unknown; restored from __doc__
        """ QMainWindow.removeToolBar(QToolBar) """
        pass

    def removeToolBarBreak(self, QToolBar): # real signature unknown; restored from __doc__
        """ QMainWindow.removeToolBarBreak(QToolBar) """
        pass

    def restoreDockWidget(self, QDockWidget): # real signature unknown; restored from __doc__
        """ QMainWindow.restoreDockWidget(QDockWidget) -> bool """
        return False

    def restoreState(self, QByteArray, int_version=0): # real signature unknown; restored from __doc__
        """ QMainWindow.restoreState(QByteArray, int version=0) -> bool """
        return False

    def saveState(self, int_version=0): # real signature unknown; restored from __doc__
        """ QMainWindow.saveState(int version=0) -> QByteArray """
        pass

    def setAnimated(self, bool): # real signature unknown; restored from __doc__
        """ QMainWindow.setAnimated(bool) """
        pass

    def setCentralWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QMainWindow.setCentralWidget(QWidget) """
        pass

    def setCorner(self, Qt_Corner, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ QMainWindow.setCorner(Qt.Corner, Qt.DockWidgetArea) """
        pass

    def setDockNestingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QMainWindow.setDockNestingEnabled(bool) """
        pass

    def setDockOptions(self, QMainWindow_DockOptions): # real signature unknown; restored from __doc__
        """ QMainWindow.setDockOptions(QMainWindow.DockOptions) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ QMainWindow.setDocumentMode(bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QMainWindow.setIconSize(QSize) """
        pass

    def setMenuBar(self, QMenuBar): # real signature unknown; restored from __doc__
        """ QMainWindow.setMenuBar(QMenuBar) """
        pass

    def setMenuWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QMainWindow.setMenuWidget(QWidget) """
        pass

    def setStatusBar(self, QStatusBar): # real signature unknown; restored from __doc__
        """ QMainWindow.setStatusBar(QStatusBar) """
        pass

    def setTabPosition(self, Qt_DockWidgetAreas, QTabWidget_TabPosition): # real signature unknown; restored from __doc__
        """ QMainWindow.setTabPosition(Qt.DockWidgetAreas, QTabWidget.TabPosition) """
        pass

    def setTabShape(self, QTabWidget_TabShape): # real signature unknown; restored from __doc__
        """ QMainWindow.setTabShape(QTabWidget.TabShape) """
        pass

    def setToolButtonStyle(self, Qt_ToolButtonStyle): # real signature unknown; restored from __doc__
        """ QMainWindow.setToolButtonStyle(Qt.ToolButtonStyle) """
        pass

    def setUnifiedTitleAndToolBarOnMac(self, bool): # real signature unknown; restored from __doc__
        """ QMainWindow.setUnifiedTitleAndToolBarOnMac(bool) """
        pass

    def splitDockWidget(self, QDockWidget, QDockWidget_1, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QMainWindow.splitDockWidget(QDockWidget, QDockWidget, Qt.Orientation) """
        pass

    def statusBar(self): # real signature unknown; restored from __doc__
        """ QMainWindow.statusBar() -> QStatusBar """
        return QStatusBar

    def tabifiedDockWidgets(self, QDockWidget): # real signature unknown; restored from __doc__
        """ QMainWindow.tabifiedDockWidgets(QDockWidget) -> list-of-QDockWidget """
        pass

    def tabifyDockWidget(self, QDockWidget, QDockWidget_1): # real signature unknown; restored from __doc__
        """ QMainWindow.tabifyDockWidget(QDockWidget, QDockWidget) """
        pass

    def tabPosition(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ QMainWindow.tabPosition(Qt.DockWidgetArea) -> QTabWidget.TabPosition """
        pass

    def tabShape(self): # real signature unknown; restored from __doc__
        """ QMainWindow.tabShape() -> QTabWidget.TabShape """
        pass

    def toolBarArea(self, QToolBar): # real signature unknown; restored from __doc__
        """ QMainWindow.toolBarArea(QToolBar) -> Qt.ToolBarArea """
        pass

    def toolBarBreak(self, QToolBar): # real signature unknown; restored from __doc__
        """ QMainWindow.toolBarBreak(QToolBar) -> bool """
        return False

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ QMainWindow.toolButtonStyle() -> Qt.ToolButtonStyle """
        pass

    def toolButtonStyleChanged(self, *args, **kwargs): # real signature unknown
        """ QMainWindow.toolButtonStyleChanged[Qt.ToolButtonStyle] [signal] """
        pass

    def unifiedTitleAndToolBarOnMac(self): # real signature unknown; restored from __doc__
        """ QMainWindow.unifiedTitleAndToolBarOnMac() -> bool """
        return False

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    AllowNestedDocks = 2
    AllowTabbedDocks = 4
    AnimatedDocks = 1
    ForceTabbedDocks = 8
    VerticalTabs = 16


