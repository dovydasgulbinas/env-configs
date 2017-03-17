# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QTabWidget(QWidget):
    """ QTabWidget(QWidget parent=None) """
    def addTab(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTabWidget.addTab(QWidget, QString) -> int
        QTabWidget.addTab(QWidget, QIcon, QString) -> int
        """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QTabWidget.changeEvent(QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QTabWidget.clear() """
        pass

    def cornerWidget(self, Qt_Corner_corner=None): # real signature unknown; restored from __doc__
        """ QTabWidget.cornerWidget(Qt.Corner corner=Qt.TopRightCorner) -> QWidget """
        return QWidget

    def count(self): # real signature unknown; restored from __doc__
        """ QTabWidget.count() -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QTabWidget.currentChanged[int] [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QTabWidget.currentIndex() -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ QTabWidget.currentWidget() -> QWidget """
        return QWidget

    def documentMode(self): # real signature unknown; restored from __doc__
        """ QTabWidget.documentMode() -> bool """
        return False

    def elideMode(self): # real signature unknown; restored from __doc__
        """ QTabWidget.elideMode() -> Qt.TextElideMode """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QTabWidget.event(QEvent) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.heightForWidth(int) -> int """
        return 0

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QTabWidget.iconSize() -> QSize """
        pass

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QTabWidget.indexOf(QWidget) -> int """
        return 0

    def initStyleOption(self, QStyleOptionTabWidgetFrame): # real signature unknown; restored from __doc__
        """ QTabWidget.initStyleOption(QStyleOptionTabWidgetFrame) """
        pass

    def insertTab(self, p_int, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTabWidget.insertTab(int, QWidget, QString) -> int
        QTabWidget.insertTab(int, QWidget, QIcon, QString) -> int
        """
        return 0

    def isMovable(self): # real signature unknown; restored from __doc__
        """ QTabWidget.isMovable() -> bool """
        return False

    def isTabEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.isTabEnabled(int) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QTabWidget.keyPressEvent(QKeyEvent) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QTabWidget.minimumSizeHint() -> QSize """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QTabWidget.paintEvent(QPaintEvent) """
        pass

    def removeTab(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.removeTab(int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QTabWidget.resizeEvent(QResizeEvent) """
        pass

    def setCornerWidget(self, QWidget, Qt_Corner_corner=None): # real signature unknown; restored from __doc__
        """ QTabWidget.setCornerWidget(QWidget, Qt.Corner corner=Qt.TopRightCorner) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.setCurrentIndex(int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QTabWidget.setCurrentWidget(QWidget) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ QTabWidget.setDocumentMode(bool) """
        pass

    def setElideMode(self, Qt_TextElideMode): # real signature unknown; restored from __doc__
        """ QTabWidget.setElideMode(Qt.TextElideMode) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QTabWidget.setIconSize(QSize) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ QTabWidget.setMovable(bool) """
        pass

    def setTabBar(self, QTabBar): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabBar(QTabBar) """
        pass

    def setTabEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabEnabled(int, bool) """
        pass

    def setTabIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabIcon(int, QIcon) """
        pass

    def setTabPosition(self, QTabWidget_TabPosition): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabPosition(QTabWidget.TabPosition) """
        pass

    def setTabsClosable(self, bool): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabsClosable(bool) """
        pass

    def setTabShape(self, QTabWidget_TabShape): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabShape(QTabWidget.TabShape) """
        pass

    def setTabText(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabText(int, QString) """
        pass

    def setTabToolTip(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabToolTip(int, QString) """
        pass

    def setTabWhatsThis(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QTabWidget.setTabWhatsThis(int, QString) """
        pass

    def setUsesScrollButtons(self, bool): # real signature unknown; restored from __doc__
        """ QTabWidget.setUsesScrollButtons(bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QTabWidget.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QTabWidget.sizeHint() -> QSize """
        pass

    def tabBar(self): # real signature unknown; restored from __doc__
        """ QTabWidget.tabBar() -> QTabBar """
        return QTabBar

    def tabCloseRequested(self, *args, **kwargs): # real signature unknown
        """ QTabWidget.tabCloseRequested[int] [signal] """
        pass

    def tabIcon(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.tabIcon(int) -> QIcon """
        return QIcon

    def tabInserted(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.tabInserted(int) """
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ QTabWidget.tabPosition() -> QTabWidget.TabPosition """
        pass

    def tabRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.tabRemoved(int) """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ QTabWidget.tabsClosable() -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ QTabWidget.tabShape() -> QTabWidget.TabShape """
        pass

    def tabText(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.tabText(int) -> QString """
        pass

    def tabToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.tabToolTip(int) -> QString """
        pass

    def tabWhatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.tabWhatsThis(int) -> QString """
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ QTabWidget.usesScrollButtons() -> bool """
        return False

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ QTabWidget.widget(int) -> QWidget """
        return QWidget

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    East = 3
    North = 0
    Rounded = 0
    South = 1
    Triangular = 1
    West = 2


