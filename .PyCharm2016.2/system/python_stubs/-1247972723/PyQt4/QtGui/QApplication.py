# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QApplication(__PyQt4_QtCore.QCoreApplication):
    """
    QApplication(list-of-str)
    QApplication(list-of-str, bool)
    QApplication(list-of-str, QApplication.Type)
    QApplication(Display, int visual=0, int colormap=0)
    QApplication(Display, list-of-str, int visual=0, int cmap=0)
    """
    def aboutQt(self): # real signature unknown; restored from __doc__
        """ QApplication.aboutQt() """
        pass

    def activeModalWidget(self): # real signature unknown; restored from __doc__
        """ QApplication.activeModalWidget() -> QWidget """
        return QWidget

    def activePopupWidget(self): # real signature unknown; restored from __doc__
        """ QApplication.activePopupWidget() -> QWidget """
        return QWidget

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ QApplication.activeWindow() -> QWidget """
        return QWidget

    def alert(self, QWidget, int_msecs=0): # real signature unknown; restored from __doc__
        """ QApplication.alert(QWidget, int msecs=0) """
        pass

    def allWidgets(self): # real signature unknown; restored from __doc__
        """ QApplication.allWidgets() -> list-of-QWidget """
        pass

    def autoSipEnabled(self): # real signature unknown; restored from __doc__
        """ QApplication.autoSipEnabled() -> bool """
        return False

    def beep(self): # real signature unknown; restored from __doc__
        """ QApplication.beep() """
        pass

    def changeOverrideCursor(self, QCursor): # real signature unknown; restored from __doc__
        """ QApplication.changeOverrideCursor(QCursor) """
        pass

    def clipboard(self): # real signature unknown; restored from __doc__
        """ QApplication.clipboard() -> QClipboard """
        return QClipboard

    def closeAllWindows(self): # real signature unknown; restored from __doc__
        """ QApplication.closeAllWindows() """
        pass

    def colorSpec(self): # real signature unknown; restored from __doc__
        """ QApplication.colorSpec() -> int """
        return 0

    def commitData(self, QSessionManager): # real signature unknown; restored from __doc__
        """ QApplication.commitData(QSessionManager) """
        pass

    def commitDataRequest(self, *args, **kwargs): # real signature unknown
        """ QApplication.commitDataRequest[QSessionManager] [signal] """
        pass

    def cursorFlashTime(self): # real signature unknown; restored from __doc__
        """ QApplication.cursorFlashTime() -> int """
        return 0

    def desktop(self): # real signature unknown; restored from __doc__
        """ QApplication.desktop() -> QDesktopWidget """
        return QDesktopWidget

    def desktopSettingsAware(self): # real signature unknown; restored from __doc__
        """ QApplication.desktopSettingsAware() -> bool """
        return False

    def doubleClickInterval(self): # real signature unknown; restored from __doc__
        """ QApplication.doubleClickInterval() -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QApplication.event(QEvent) -> bool """
        return False

    def exec_(self): # real signature unknown; restored from __doc__
        """ QApplication.exec_() -> int """
        return 0

    def focusChanged(self, *args, **kwargs): # real signature unknown
        """ QApplication.focusChanged[QWidget, QWidget] [signal] """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ QApplication.focusWidget() -> QWidget """
        return QWidget

    def font(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QApplication.font() -> QFont
        QApplication.font(QWidget) -> QFont
        QApplication.font(str) -> QFont
        """
        return QFont

    def fontDatabaseChanged(self, *args, **kwargs): # real signature unknown
        """ QApplication.fontDatabaseChanged [signal] """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ QApplication.fontMetrics() -> QFontMetrics """
        return QFontMetrics

    def globalStrut(self): # real signature unknown; restored from __doc__
        """ QApplication.globalStrut() -> QSize """
        pass

    def inputContext(self): # real signature unknown; restored from __doc__
        """ QApplication.inputContext() -> QInputContext """
        return QInputContext

    def isEffectEnabled(self, Qt_UIEffect): # real signature unknown; restored from __doc__
        """ QApplication.isEffectEnabled(Qt.UIEffect) -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ QApplication.isLeftToRight() -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ QApplication.isRightToLeft() -> bool """
        return False

    def isSessionRestored(self): # real signature unknown; restored from __doc__
        """ QApplication.isSessionRestored() -> bool """
        return False

    def keyboardInputDirection(self): # real signature unknown; restored from __doc__
        """ QApplication.keyboardInputDirection() -> Qt.LayoutDirection """
        pass

    def keyboardInputInterval(self): # real signature unknown; restored from __doc__
        """ QApplication.keyboardInputInterval() -> int """
        return 0

    def keyboardInputLocale(self): # real signature unknown; restored from __doc__
        """ QApplication.keyboardInputLocale() -> QLocale """
        pass

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ QApplication.keyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def lastWindowClosed(self, *args, **kwargs): # real signature unknown
        """ QApplication.lastWindowClosed [signal] """
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ QApplication.layoutDirection() -> Qt.LayoutDirection """
        pass

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ QApplication.mouseButtons() -> Qt.MouseButtons """
        pass

    def notify(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QApplication.notify(QObject, QEvent) -> bool """
        return False

    def overrideCursor(self): # real signature unknown; restored from __doc__
        """ QApplication.overrideCursor() -> QCursor """
        return QCursor

    def palette(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QApplication.palette() -> QPalette
        QApplication.palette(QWidget) -> QPalette
        QApplication.palette(str) -> QPalette
        """
        return QPalette

    def queryKeyboardModifiers(self): # real signature unknown; restored from __doc__
        """ QApplication.queryKeyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def quitOnLastWindowClosed(self): # real signature unknown; restored from __doc__
        """ QApplication.quitOnLastWindowClosed() -> bool """
        return False

    def restoreOverrideCursor(self): # real signature unknown; restored from __doc__
        """ QApplication.restoreOverrideCursor() """
        pass

    def saveState(self, QSessionManager): # real signature unknown; restored from __doc__
        """ QApplication.saveState(QSessionManager) """
        pass

    def saveStateRequest(self, *args, **kwargs): # real signature unknown
        """ QApplication.saveStateRequest[QSessionManager] [signal] """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ QApplication.sessionId() -> QString """
        pass

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ QApplication.sessionKey() -> QString """
        pass

    def setActiveWindow(self, QWidget): # real signature unknown; restored from __doc__
        """ QApplication.setActiveWindow(QWidget) """
        pass

    def setAutoSipEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QApplication.setAutoSipEnabled(bool) """
        pass

    def setColorSpec(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setColorSpec(int) """
        pass

    def setCursorFlashTime(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setCursorFlashTime(int) """
        pass

    def setDesktopSettingsAware(self, bool): # real signature unknown; restored from __doc__
        """ QApplication.setDesktopSettingsAware(bool) """
        pass

    def setDoubleClickInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setDoubleClickInterval(int) """
        pass

    def setEffectEnabled(self, Qt_UIEffect, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QApplication.setEffectEnabled(Qt.UIEffect, bool enabled=True) """
        pass

    def setFont(self, QFont, str_className=None): # real signature unknown; restored from __doc__
        """ QApplication.setFont(QFont, str className=None) """
        pass

    def setGlobalStrut(self, QSize): # real signature unknown; restored from __doc__
        """ QApplication.setGlobalStrut(QSize) """
        pass

    def setGraphicsSystem(self, QString): # real signature unknown; restored from __doc__
        """ QApplication.setGraphicsSystem(QString) """
        pass

    def setInputContext(self, QInputContext): # real signature unknown; restored from __doc__
        """ QApplication.setInputContext(QInputContext) """
        pass

    def setKeyboardInputInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setKeyboardInputInterval(int) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ QApplication.setLayoutDirection(Qt.LayoutDirection) """
        pass

    def setOverrideCursor(self, QCursor): # real signature unknown; restored from __doc__
        """ QApplication.setOverrideCursor(QCursor) """
        pass

    def setPalette(self, QPalette, str_className=None): # real signature unknown; restored from __doc__
        """ QApplication.setPalette(QPalette, str className=None) """
        pass

    def setQuitOnLastWindowClosed(self, bool): # real signature unknown; restored from __doc__
        """ QApplication.setQuitOnLastWindowClosed(bool) """
        pass

    def setStartDragDistance(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setStartDragDistance(int) """
        pass

    def setStartDragTime(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setStartDragTime(int) """
        pass

    def setStyle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QApplication.setStyle(QStyle)
        QApplication.setStyle(QString) -> QStyle
        """
        return QStyle

    def setStyleSheet(self, QString): # real signature unknown; restored from __doc__
        """ QApplication.setStyleSheet(QString) """
        pass

    def setWheelScrollLines(self, p_int): # real signature unknown; restored from __doc__
        """ QApplication.setWheelScrollLines(int) """
        pass

    def setWindowIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QApplication.setWindowIcon(QIcon) """
        pass

    def startDragDistance(self): # real signature unknown; restored from __doc__
        """ QApplication.startDragDistance() -> int """
        return 0

    def startDragTime(self): # real signature unknown; restored from __doc__
        """ QApplication.startDragTime() -> int """
        return 0

    def style(self): # real signature unknown; restored from __doc__
        """ QApplication.style() -> QStyle """
        return QStyle

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ QApplication.styleSheet() -> QString """
        pass

    def syncX(self): # real signature unknown; restored from __doc__
        """ QApplication.syncX() """
        pass

    def topLevelAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QApplication.topLevelAt(QPoint) -> QWidget
        QApplication.topLevelAt(int, int) -> QWidget
        """
        return QWidget

    def topLevelWidgets(self): # real signature unknown; restored from __doc__
        """ QApplication.topLevelWidgets() -> list-of-QWidget """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QApplication.type() -> QApplication.Type """
        pass

    def wheelScrollLines(self): # real signature unknown; restored from __doc__
        """ QApplication.wheelScrollLines() -> int """
        return 0

    def widgetAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QApplication.widgetAt(QPoint) -> QWidget
        QApplication.widgetAt(int, int) -> QWidget
        """
        return QWidget

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ QApplication.windowIcon() -> QIcon """
        return QIcon

    def x11EventFilter(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QApplication.x11EventFilter(sip.voidptr) -> bool """
        return False

    def x11ProcessEvent(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QApplication.x11ProcessEvent(sip.voidptr) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CustomColor = 1
    GuiClient = 1
    GuiServer = 2
    ManyColor = 2
    NormalColor = 0
    Tty = 0


