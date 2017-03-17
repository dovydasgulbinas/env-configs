# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QWidget import QWidget

class QMenu(QWidget):
    """
    QMenu(QWidget parent=None)
    QMenu(QString, QWidget parent=None)
    """
    def aboutToHide(self, *args, **kwargs): # real signature unknown
        """ QMenu.aboutToHide [signal] """
        pass

    def aboutToShow(self, *args, **kwargs): # real signature unknown
        """ QMenu.aboutToShow [signal] """
        pass

    def actionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QMenu.actionAt(QPoint) -> QAction """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ QMenu.actionEvent(QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.actionGeometry(QAction) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ QMenu.activeAction() -> QAction """
        return QAction

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenu.addAction(QAction)
        QMenu.addAction(QString) -> QAction
        QMenu.addAction(QIcon, QString) -> QAction
        QMenu.addAction(QString, QObject, SLOT(), QKeySequence shortcut=0) -> QAction
        QMenu.addAction(QString, callable, QKeySequence shortcut=0) -> QAction
        QMenu.addAction(QIcon, QString, QObject, SLOT(), QKeySequence shortcut=0) -> QAction
        QMenu.addAction(QIcon, QString, callable, QKeySequence shortcut=0) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenu.addMenu(QMenu) -> QAction
        QMenu.addMenu(QString) -> QMenu
        QMenu.addMenu(QIcon, QString) -> QMenu
        """
        return QAction or QMenu

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ QMenu.addSeparator() -> QAction """
        return QAction

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.changeEvent(QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QMenu.clear() """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QMenu.columnCount() -> int """
        return 0

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ QMenu.defaultAction() -> QAction """
        return QAction

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.enterEvent(QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.event(QEvent) -> bool """
        return False

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMenu.exec_() -> QAction
        QMenu.exec_(QPoint, QAction action=None) -> QAction
        QMenu.exec_(list-of-QAction, QPoint, QAction action=None) -> QAction
        QMenu.exec_(list-of-QAction, QPoint, QAction, QWidget) -> QAction
        """
        return QAction

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QMenu.focusNextPrevChild(bool) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QMenu.hideEvent(QHideEvent) """
        pass

    def hideTearOffMenu(self): # real signature unknown; restored from __doc__
        """ QMenu.hideTearOffMenu() """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        """ QMenu.hovered[QAction] [signal] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QMenu.icon() -> QIcon """
        return QIcon

    def initStyleOption(self, QStyleOptionMenuItem, QAction): # real signature unknown; restored from __doc__
        """ QMenu.initStyleOption(QStyleOptionMenuItem, QAction) """
        pass

    def insertMenu(self, QAction, QMenu): # real signature unknown; restored from __doc__
        """ QMenu.insertMenu(QAction, QMenu) -> QAction """
        return QAction

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.insertSeparator(QAction) -> QAction """
        return QAction

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QMenu.isEmpty() -> bool """
        return False

    def isTearOffEnabled(self): # real signature unknown; restored from __doc__
        """ QMenu.isTearOffEnabled() -> bool """
        return False

    def isTearOffMenuVisible(self): # real signature unknown; restored from __doc__
        """ QMenu.isTearOffMenuVisible() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QMenu.keyPressEvent(QKeyEvent) """
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMenu.leaveEvent(QEvent) """
        pass

    def menuAction(self): # real signature unknown; restored from __doc__
        """ QMenu.menuAction() -> QAction """
        return QAction

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenu.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenu.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QMenu.mouseReleaseEvent(QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QMenu.paintEvent(QPaintEvent) """
        pass

    def popup(self, QPoint, QAction_action=None): # real signature unknown; restored from __doc__
        """ QMenu.popup(QPoint, QAction action=None) """
        pass

    def separatorsCollapsible(self): # real signature unknown; restored from __doc__
        """ QMenu.separatorsCollapsible() -> bool """
        return False

    def setActiveAction(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.setActiveAction(QAction) """
        pass

    def setDefaultAction(self, QAction): # real signature unknown; restored from __doc__
        """ QMenu.setDefaultAction(QAction) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QMenu.setIcon(QIcon) """
        pass

    def setNoReplayFor(self, QWidget): # real signature unknown; restored from __doc__
        """ QMenu.setNoReplayFor(QWidget) """
        pass

    def setSeparatorsCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ QMenu.setSeparatorsCollapsible(bool) """
        pass

    def setTearOffEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QMenu.setTearOffEnabled(bool) """
        pass

    def setTitle(self, QString): # real signature unknown; restored from __doc__
        """ QMenu.setTitle(QString) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMenu.sizeHint() -> QSize """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QMenu.timerEvent(QTimerEvent) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QMenu.title() -> QString """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        """ QMenu.triggered[QAction] [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QMenu.wheelEvent(QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


