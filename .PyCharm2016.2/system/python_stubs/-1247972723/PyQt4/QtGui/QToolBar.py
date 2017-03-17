# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QToolBar(QWidget):
    """
    QToolBar(QString, QWidget parent=None)
    QToolBar(QWidget parent=None)
    """
    def actionAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QToolBar.actionAt(QPoint) -> QAction
        QToolBar.actionAt(int, int) -> QAction
        """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ QToolBar.actionEvent(QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ QToolBar.actionGeometry(QAction) -> QRect """
        pass

    def actionTriggered(self, *args, **kwargs): # real signature unknown
        """ QToolBar.actionTriggered[QAction] [signal] """
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QToolBar.addAction(QAction)
        QToolBar.addAction(QString) -> QAction
        QToolBar.addAction(QIcon, QString) -> QAction
        QToolBar.addAction(QString, QObject, SLOT()) -> QAction
        QToolBar.addAction(QString, callable) -> QAction
        QToolBar.addAction(QIcon, QString, QObject, SLOT()) -> QAction
        QToolBar.addAction(QIcon, QString, callable) -> QAction
        """
        return QAction

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ QToolBar.addSeparator() -> QAction """
        return QAction

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QToolBar.addWidget(QWidget) -> QAction """
        return QAction

    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ QToolBar.allowedAreas() -> Qt.ToolBarAreas """
        pass

    def allowedAreasChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.allowedAreasChanged[Qt.ToolBarAreas] [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QToolBar.changeEvent(QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ QToolBar.childEvent(QChildEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QToolBar.clear() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QToolBar.event(QEvent) -> bool """
        return False

    def iconSize(self): # real signature unknown; restored from __doc__
        """ QToolBar.iconSize() -> QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.iconSizeChanged[QSize] [signal] """
        pass

    def initStyleOption(self, QStyleOptionToolBar): # real signature unknown; restored from __doc__
        """ QToolBar.initStyleOption(QStyleOptionToolBar) """
        pass

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ QToolBar.insertSeparator(QAction) -> QAction """
        return QAction

    def insertWidget(self, QAction, QWidget): # real signature unknown; restored from __doc__
        """ QToolBar.insertWidget(QAction, QWidget) -> QAction """
        return QAction

    def isAreaAllowed(self, Qt_ToolBarArea): # real signature unknown; restored from __doc__
        """ QToolBar.isAreaAllowed(Qt.ToolBarArea) -> bool """
        return False

    def isFloatable(self): # real signature unknown; restored from __doc__
        """ QToolBar.isFloatable() -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ QToolBar.isFloating() -> bool """
        return False

    def isMovable(self): # real signature unknown; restored from __doc__
        """ QToolBar.isMovable() -> bool """
        return False

    def movableChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.movableChanged[bool] [signal] """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ QToolBar.orientation() -> Qt.Orientation """
        pass

    def orientationChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.orientationChanged[Qt.Orientation] [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QToolBar.paintEvent(QPaintEvent) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QToolBar.resizeEvent(QResizeEvent) """
        pass

    def setAllowedAreas(self, Qt_ToolBarAreas): # real signature unknown; restored from __doc__
        """ QToolBar.setAllowedAreas(Qt.ToolBarAreas) """
        pass

    def setFloatable(self, bool): # real signature unknown; restored from __doc__
        """ QToolBar.setFloatable(bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ QToolBar.setIconSize(QSize) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ QToolBar.setMovable(bool) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QToolBar.setOrientation(Qt.Orientation) """
        pass

    def setToolButtonStyle(self, Qt_ToolButtonStyle): # real signature unknown; restored from __doc__
        """ QToolBar.setToolButtonStyle(Qt.ToolButtonStyle) """
        pass

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ QToolBar.toggleViewAction() -> QAction """
        return QAction

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ QToolBar.toolButtonStyle() -> Qt.ToolButtonStyle """
        pass

    def toolButtonStyleChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.toolButtonStyleChanged[Qt.ToolButtonStyle] [signal] """
        pass

    def topLevelChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.topLevelChanged[bool] [signal] """
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBar.visibilityChanged[bool] [signal] """
        pass

    def widgetForAction(self, QAction): # real signature unknown; restored from __doc__
        """ QToolBar.widgetForAction(QAction) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


