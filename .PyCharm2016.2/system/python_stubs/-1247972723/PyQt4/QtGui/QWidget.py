# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QPaintDevice import QPaintDevice

class QWidget(__PyQt4_QtCore.QObject, QPaintDevice):
    """ QWidget(QWidget parent=None, Qt.WindowFlags flags=0) """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ QWidget.acceptDrops() -> bool """
        return False

    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ QWidget.accessibleDescription() -> QString """
        pass

    def accessibleName(self): # real signature unknown; restored from __doc__
        """ QWidget.accessibleName() -> QString """
        pass

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ QWidget.actionEvent(QActionEvent) """
        pass

    def actions(self): # real signature unknown; restored from __doc__
        """ QWidget.actions() -> list-of-QAction """
        pass

    def activateWindow(self): # real signature unknown; restored from __doc__
        """ QWidget.activateWindow() """
        pass

    def addAction(self, QAction): # real signature unknown; restored from __doc__
        """ QWidget.addAction(QAction) """
        pass

    def addActions(self, list_of_QAction): # real signature unknown; restored from __doc__
        """ QWidget.addActions(list-of-QAction) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ QWidget.adjustSize() """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ QWidget.autoFillBackground() -> bool """
        return False

    def backgroundRole(self): # real signature unknown; restored from __doc__
        """ QWidget.backgroundRole() -> QPalette.ColorRole """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ QWidget.baseSize() -> QSize """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QWidget.changeEvent(QEvent) """
        pass

    def childAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.childAt(QPoint) -> QWidget
        QWidget.childAt(int, int) -> QWidget
        """
        return QWidget

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ QWidget.childrenRect() -> QRect """
        pass

    def childrenRegion(self): # real signature unknown; restored from __doc__
        """ QWidget.childrenRegion() -> QRegion """
        return QRegion

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ QWidget.clearFocus() """
        pass

    def clearMask(self): # real signature unknown; restored from __doc__
        """ QWidget.clearMask() """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QWidget.close() -> bool """
        return False

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QWidget.closeEvent(QCloseEvent) """
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ QWidget.contentsMargins() -> QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ QWidget.contentsRect() -> QRect """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QWidget.contextMenuEvent(QContextMenuEvent) """
        pass

    def contextMenuPolicy(self): # real signature unknown; restored from __doc__
        """ QWidget.contextMenuPolicy() -> Qt.ContextMenuPolicy """
        pass

    def create(self, int_window=0, bool_initializeWindow=True, bool_destroyOldWindow=True): # real signature unknown; restored from __doc__
        """ QWidget.create(int window=0, bool initializeWindow=True, bool destroyOldWindow=True) """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ QWidget.cursor() -> QCursor """
        return QCursor

    def customContextMenuRequested(self, *args, **kwargs): # real signature unknown
        """ QWidget.customContextMenuRequested[QPoint] [signal] """
        pass

    def destroy(self, bool_destroyWindow=True, bool_destroySubWindows=True): # real signature unknown; restored from __doc__
        """ QWidget.destroy(bool destroyWindow=True, bool destroySubWindows=True) """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ QWidget.devType() -> int """
        return 0

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QWidget.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QWidget.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QWidget.dragMoveEvent(QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QWidget.dropEvent(QDropEvent) """
        pass

    def effectiveWinId(self): # real signature unknown; restored from __doc__
        """ QWidget.effectiveWinId() -> int """
        return 0

    def enabledChange(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.enabledChange(bool) """
        pass

    def ensurePolished(self): # real signature unknown; restored from __doc__
        """ QWidget.ensurePolished() """
        pass

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QWidget.enterEvent(QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWidget.event(QEvent) -> bool """
        return False

    def find(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.find(int) -> QWidget """
        return QWidget

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QWidget.focusInEvent(QFocusEvent) """
        pass

    def focusNextChild(self): # real signature unknown; restored from __doc__
        """ QWidget.focusNextChild() -> bool """
        return False

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QWidget.focusOutEvent(QFocusEvent) """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ QWidget.focusPolicy() -> Qt.FocusPolicy """
        pass

    def focusPreviousChild(self): # real signature unknown; restored from __doc__
        """ QWidget.focusPreviousChild() -> bool """
        return False

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ QWidget.focusProxy() -> QWidget """
        return QWidget

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ QWidget.focusWidget() -> QWidget """
        return QWidget

    def font(self): # real signature unknown; restored from __doc__
        """ QWidget.font() -> QFont """
        return QFont

    def fontChange(self, QFont): # real signature unknown; restored from __doc__
        """ QWidget.fontChange(QFont) """
        pass

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ QWidget.fontInfo() -> QFontInfo """
        return QFontInfo

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ QWidget.fontMetrics() -> QFontMetrics """
        return QFontMetrics

    def foregroundRole(self): # real signature unknown; restored from __doc__
        """ QWidget.foregroundRole() -> QPalette.ColorRole """
        pass

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ QWidget.frameGeometry() -> QRect """
        pass

    def frameSize(self): # real signature unknown; restored from __doc__
        """ QWidget.frameSize() -> QSize """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ QWidget.geometry() -> QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ QWidget.getContentsMargins() -> (int, int, int, int) """
        pass

    def grabGesture(self, Qt_GestureType, Qt_GestureFlags_flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWidget.grabGesture(Qt.GestureType, Qt.GestureFlags flags=Qt.GestureFlags(0)) """
        pass

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ QWidget.grabKeyboard() """
        pass

    def grabMouse(self, QCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.grabMouse()
        QWidget.grabMouse(QCursor)
        """
        pass

    def grabShortcut(self, QKeySequence, Qt_ShortcutContext_context=None): # real signature unknown; restored from __doc__
        """ QWidget.grabShortcut(QKeySequence, Qt.ShortcutContext context=Qt.WindowShortcut) -> int """
        return 0

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ QWidget.graphicsEffect() -> QGraphicsEffect """
        return QGraphicsEffect

    def graphicsProxyWidget(self): # real signature unknown; restored from __doc__
        """ QWidget.graphicsProxyWidget() -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def handle(self): # real signature unknown; restored from __doc__
        """ QWidget.handle() -> int """
        return 0

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ QWidget.hasFocus() -> bool """
        return False

    def hasMouseTracking(self): # real signature unknown; restored from __doc__
        """ QWidget.hasMouseTracking() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ QWidget.height() -> int """
        return 0

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.heightForWidth(int) -> int """
        return 0

    def hide(self): # real signature unknown; restored from __doc__
        """ QWidget.hide() """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QWidget.hideEvent(QHideEvent) """
        pass

    def inputContext(self): # real signature unknown; restored from __doc__
        """ QWidget.inputContext() -> QInputContext """
        return QInputContext

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QWidget.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ QWidget.inputMethodHints() -> Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QWidget.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def insertAction(self, QAction, QAction_1): # real signature unknown; restored from __doc__
        """ QWidget.insertAction(QAction, QAction) """
        pass

    def insertActions(self, QAction, list_of_QAction): # real signature unknown; restored from __doc__
        """ QWidget.insertActions(QAction, list-of-QAction) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ QWidget.isActiveWindow() -> bool """
        return False

    def isAncestorOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidget.isAncestorOf(QWidget) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QWidget.isEnabled() -> bool """
        return False

    def isEnabledTo(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidget.isEnabledTo(QWidget) -> bool """
        return False

    def isEnabledToTLW(self): # real signature unknown; restored from __doc__
        """ QWidget.isEnabledToTLW() -> bool """
        return False

    def isFullScreen(self): # real signature unknown; restored from __doc__
        """ QWidget.isFullScreen() -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ QWidget.isHidden() -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ QWidget.isLeftToRight() -> bool """
        return False

    def isMaximized(self): # real signature unknown; restored from __doc__
        """ QWidget.isMaximized() -> bool """
        return False

    def isMinimized(self): # real signature unknown; restored from __doc__
        """ QWidget.isMinimized() -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ QWidget.isModal() -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ QWidget.isRightToLeft() -> bool """
        return False

    def isTopLevel(self): # real signature unknown; restored from __doc__
        """ QWidget.isTopLevel() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ QWidget.isVisible() -> bool """
        return False

    def isVisibleTo(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidget.isVisibleTo(QWidget) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ QWidget.isWindow() -> bool """
        return False

    def isWindowModified(self): # real signature unknown; restored from __doc__
        """ QWidget.isWindowModified() -> bool """
        return False

    def keyboardGrabber(self): # real signature unknown; restored from __doc__
        """ QWidget.keyboardGrabber() -> QWidget """
        return QWidget

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QWidget.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QWidget.keyReleaseEvent(QKeyEvent) """
        pass

    def languageChange(self): # real signature unknown; restored from __doc__
        """ QWidget.languageChange() """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ QWidget.layout() -> QLayout """
        return QLayout

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ QWidget.layoutDirection() -> Qt.LayoutDirection """
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QWidget.leaveEvent(QEvent) """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ QWidget.locale() -> QLocale """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ QWidget.lower() """
        pass

    def mapFrom(self, QWidget, QPoint): # real signature unknown; restored from __doc__
        """ QWidget.mapFrom(QWidget, QPoint) -> QPoint """
        pass

    def mapFromGlobal(self, QPoint): # real signature unknown; restored from __doc__
        """ QWidget.mapFromGlobal(QPoint) -> QPoint """
        pass

    def mapFromParent(self, QPoint): # real signature unknown; restored from __doc__
        """ QWidget.mapFromParent(QPoint) -> QPoint """
        pass

    def mapTo(self, QWidget, QPoint): # real signature unknown; restored from __doc__
        """ QWidget.mapTo(QWidget, QPoint) -> QPoint """
        pass

    def mapToGlobal(self, QPoint): # real signature unknown; restored from __doc__
        """ QWidget.mapToGlobal(QPoint) -> QPoint """
        pass

    def mapToParent(self, QPoint): # real signature unknown; restored from __doc__
        """ QWidget.mapToParent(QPoint) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ QWidget.mask() -> QRegion """
        return QRegion

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ QWidget.maximumHeight() -> int """
        return 0

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ QWidget.maximumSize() -> QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ QWidget.maximumWidth() -> int """
        return 0

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QWidget.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ QWidget.minimumHeight() -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ QWidget.minimumSize() -> QSize """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QWidget.minimumSizeHint() -> QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ QWidget.minimumWidth() -> int """
        return 0

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWidget.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseGrabber(self): # real signature unknown; restored from __doc__
        """ QWidget.mouseGrabber() -> QWidget """
        return QWidget

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWidget.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWidget.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWidget.mouseReleaseEvent(QMouseEvent) """
        pass

    def move(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.move(QPoint)
        QWidget.move(int, int)
        """
        pass

    def moveEvent(self, QMoveEvent): # real signature unknown; restored from __doc__
        """ QWidget.moveEvent(QMoveEvent) """
        pass

    def nativeParentWidget(self): # real signature unknown; restored from __doc__
        """ QWidget.nativeParentWidget() -> QWidget """
        return QWidget

    def nextInFocusChain(self): # real signature unknown; restored from __doc__
        """ QWidget.nextInFocusChain() -> QWidget """
        return QWidget

    def normalGeometry(self): # real signature unknown; restored from __doc__
        """ QWidget.normalGeometry() -> QRect """
        pass

    def overrideWindowFlags(self, Qt_WindowFlags): # real signature unknown; restored from __doc__
        """ QWidget.overrideWindowFlags(Qt.WindowFlags) """
        pass

    def overrideWindowState(self, Qt_WindowStates): # real signature unknown; restored from __doc__
        """ QWidget.overrideWindowState(Qt.WindowStates) """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QWidget.paintEngine() -> QPaintEngine """
        return QPaintEngine

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QWidget.paintEvent(QPaintEvent) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ QWidget.palette() -> QPalette """
        return QPalette

    def paletteChange(self, QPalette): # real signature unknown; restored from __doc__
        """ QWidget.paletteChange(QPalette) """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ QWidget.parentWidget() -> QWidget """
        return QWidget

    def pos(self): # real signature unknown; restored from __doc__
        """ QWidget.pos() -> QPoint """
        pass

    def previousInFocusChain(self): # real signature unknown; restored from __doc__
        """ QWidget.previousInFocusChain() -> QWidget """
        return QWidget

    def raise_(self): # real signature unknown; restored from __doc__
        """ QWidget.raise_() """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ QWidget.rect() -> QRect """
        pass

    def releaseKeyboard(self): # real signature unknown; restored from __doc__
        """ QWidget.releaseKeyboard() """
        pass

    def releaseMouse(self): # real signature unknown; restored from __doc__
        """ QWidget.releaseMouse() """
        pass

    def releaseShortcut(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.releaseShortcut(int) """
        pass

    def removeAction(self, QAction): # real signature unknown; restored from __doc__
        """ QWidget.removeAction(QAction) """
        pass

    def render(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.render(QPaintDevice, QPoint targetOffset=QPoint(), QRegion sourceRegion=QRegion(), QWidget.RenderFlags flags=QWidget.DrawWindowBackground|QWidget.DrawChildren)
        QWidget.render(QPainter, QPoint targetOffset=QPoint(), QRegion sourceRegion=QRegion(), QWidget.RenderFlags flags=QWidget.DrawWindowBackground|QWidget.DrawChildren)
        """
        pass

    def repaint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.repaint()
        QWidget.repaint(int, int, int, int)
        QWidget.repaint(QRect)
        QWidget.repaint(QRegion)
        """
        pass

    def resetInputContext(self): # real signature unknown; restored from __doc__
        """ QWidget.resetInputContext() """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.resize(QSize)
        QWidget.resize(int, int)
        """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QWidget.resizeEvent(QResizeEvent) """
        pass

    def restoreGeometry(self, QByteArray): # real signature unknown; restored from __doc__
        """ QWidget.restoreGeometry(QByteArray) -> bool """
        return False

    def saveGeometry(self): # real signature unknown; restored from __doc__
        """ QWidget.saveGeometry() -> QByteArray """
        pass

    def scroll(self, p_int, p_int_1, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.scroll(int, int)
        QWidget.scroll(int, int, QRect)
        """
        pass

    def setAcceptDrops(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setAcceptDrops(bool) """
        pass

    def setAccessibleDescription(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setAccessibleDescription(QString) """
        pass

    def setAccessibleName(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setAccessibleName(QString) """
        pass

    def setAttribute(self, Qt_WidgetAttribute, bool_on=True): # real signature unknown; restored from __doc__
        """ QWidget.setAttribute(Qt.WidgetAttribute, bool on=True) """
        pass

    def setAutoFillBackground(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setAutoFillBackground(bool) """
        pass

    def setBackgroundRole(self, QPalette_ColorRole): # real signature unknown; restored from __doc__
        """ QWidget.setBackgroundRole(QPalette.ColorRole) """
        pass

    def setBaseSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setBaseSize(int, int)
        QWidget.setBaseSize(QSize)
        """
        pass

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setContentsMargins(int, int, int, int)
        QWidget.setContentsMargins(QMargins)
        """
        pass

    def setContextMenuPolicy(self, Qt_ContextMenuPolicy): # real signature unknown; restored from __doc__
        """ QWidget.setContextMenuPolicy(Qt.ContextMenuPolicy) """
        pass

    def setCursor(self, QCursor): # real signature unknown; restored from __doc__
        """ QWidget.setCursor(QCursor) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setDisabled(bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setEnabled(bool) """
        pass

    def setFixedHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.setFixedHeight(int) """
        pass

    def setFixedSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setFixedSize(QSize)
        QWidget.setFixedSize(int, int)
        """
        pass

    def setFixedWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.setFixedWidth(int) """
        pass

    def setFocus(self, Qt_FocusReason=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setFocus()
        QWidget.setFocus(Qt.FocusReason)
        """
        pass

    def setFocusPolicy(self, Qt_FocusPolicy): # real signature unknown; restored from __doc__
        """ QWidget.setFocusPolicy(Qt.FocusPolicy) """
        pass

    def setFocusProxy(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidget.setFocusProxy(QWidget) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QWidget.setFont(QFont) """
        pass

    def setForegroundRole(self, QPalette_ColorRole): # real signature unknown; restored from __doc__
        """ QWidget.setForegroundRole(QPalette.ColorRole) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setGeometry(QRect)
        QWidget.setGeometry(int, int, int, int)
        """
        pass

    def setGraphicsEffect(self, QGraphicsEffect): # real signature unknown; restored from __doc__
        """ QWidget.setGraphicsEffect(QGraphicsEffect) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setHidden(bool) """
        pass

    def setInputContext(self, QInputContext): # real signature unknown; restored from __doc__
        """ QWidget.setInputContext(QInputContext) """
        pass

    def setInputMethodHints(self, Qt_InputMethodHints): # real signature unknown; restored from __doc__
        """ QWidget.setInputMethodHints(Qt.InputMethodHints) """
        pass

    def setLayout(self, QLayout): # real signature unknown; restored from __doc__
        """ QWidget.setLayout(QLayout) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ QWidget.setLayoutDirection(Qt.LayoutDirection) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ QWidget.setLocale(QLocale) """
        pass

    def setMask(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setMask(QBitmap)
        QWidget.setMask(QRegion)
        """
        pass

    def setMaximumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.setMaximumHeight(int) """
        pass

    def setMaximumSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setMaximumSize(int, int)
        QWidget.setMaximumSize(QSize)
        """
        pass

    def setMaximumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.setMaximumWidth(int) """
        pass

    def setMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.setMinimumHeight(int) """
        pass

    def setMinimumSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setMinimumSize(int, int)
        QWidget.setMinimumSize(QSize)
        """
        pass

    def setMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QWidget.setMinimumWidth(int) """
        pass

    def setMouseTracking(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setMouseTracking(bool) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ QWidget.setPalette(QPalette) """
        pass

    def setParent(self, QWidget, Qt_WindowFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setParent(QWidget)
        QWidget.setParent(QWidget, Qt.WindowFlags)
        """
        pass

    def setShortcutAutoRepeat(self, p_int, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QWidget.setShortcutAutoRepeat(int, bool enabled=True) """
        pass

    def setShortcutEnabled(self, p_int, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QWidget.setShortcutEnabled(int, bool enabled=True) """
        pass

    def setShown(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setShown(bool) """
        pass

    def setSizeIncrement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setSizeIncrement(int, int)
        QWidget.setSizeIncrement(QSize)
        """
        pass

    def setSizePolicy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.setSizePolicy(QSizePolicy)
        QWidget.setSizePolicy(QSizePolicy.Policy, QSizePolicy.Policy)
        """
        pass

    def setStatusTip(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setStatusTip(QString) """
        pass

    def setStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ QWidget.setStyle(QStyle) """
        pass

    def setStyleSheet(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setStyleSheet(QString) """
        pass

    def setTabOrder(self, QWidget, QWidget_1): # real signature unknown; restored from __doc__
        """ QWidget.setTabOrder(QWidget, QWidget) """
        pass

    def setToolTip(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setToolTip(QString) """
        pass

    def setUpdatesEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setUpdatesEnabled(bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setVisible(bool) """
        pass

    def setWhatsThis(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setWhatsThis(QString) """
        pass

    def setWindowFilePath(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setWindowFilePath(QString) """
        pass

    def setWindowFlags(self, Qt_WindowFlags): # real signature unknown; restored from __doc__
        """ QWidget.setWindowFlags(Qt.WindowFlags) """
        pass

    def setWindowIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QWidget.setWindowIcon(QIcon) """
        pass

    def setWindowIconText(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setWindowIconText(QString) """
        pass

    def setWindowModality(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ QWidget.setWindowModality(Qt.WindowModality) """
        pass

    def setWindowModified(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.setWindowModified(bool) """
        pass

    def setWindowOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ QWidget.setWindowOpacity(float) """
        pass

    def setWindowRole(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setWindowRole(QString) """
        pass

    def setWindowState(self, Qt_WindowStates): # real signature unknown; restored from __doc__
        """ QWidget.setWindowState(Qt.WindowStates) """
        pass

    def setWindowTitle(self, QString): # real signature unknown; restored from __doc__
        """ QWidget.setWindowTitle(QString) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ QWidget.show() """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QWidget.showEvent(QShowEvent) """
        pass

    def showFullScreen(self): # real signature unknown; restored from __doc__
        """ QWidget.showFullScreen() """
        pass

    def showMaximized(self): # real signature unknown; restored from __doc__
        """ QWidget.showMaximized() """
        pass

    def showMinimized(self): # real signature unknown; restored from __doc__
        """ QWidget.showMinimized() """
        pass

    def showNormal(self): # real signature unknown; restored from __doc__
        """ QWidget.showNormal() """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QWidget.size() -> QSize """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QWidget.sizeHint() -> QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ QWidget.sizeIncrement() -> QSize """
        pass

    def sizePolicy(self): # real signature unknown; restored from __doc__
        """ QWidget.sizePolicy() -> QSizePolicy """
        return QSizePolicy

    def stackUnder(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidget.stackUnder(QWidget) """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ QWidget.statusTip() -> QString """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QWidget.style() -> QStyle """
        return QStyle

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ QWidget.styleSheet() -> QString """
        pass

    def tabletEvent(self, QTabletEvent): # real signature unknown; restored from __doc__
        """ QWidget.tabletEvent(QTabletEvent) """
        pass

    def testAttribute(self, Qt_WidgetAttribute): # real signature unknown; restored from __doc__
        """ QWidget.testAttribute(Qt.WidgetAttribute) -> bool """
        return False

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QWidget.toolTip() -> QString """
        pass

    def topLevelWidget(self): # real signature unknown; restored from __doc__
        """ QWidget.topLevelWidget() -> QWidget """
        return QWidget

    def underMouse(self): # real signature unknown; restored from __doc__
        """ QWidget.underMouse() -> bool """
        return False

    def ungrabGesture(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ QWidget.ungrabGesture(Qt.GestureType) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ QWidget.unsetCursor() """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ QWidget.unsetLayoutDirection() """
        pass

    def unsetLocale(self): # real signature unknown; restored from __doc__
        """ QWidget.unsetLocale() """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWidget.update()
        QWidget.update(QRect)
        QWidget.update(QRegion)
        QWidget.update(int, int, int, int)
        """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ QWidget.updateGeometry() """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ QWidget.updateMicroFocus() """
        pass

    def updatesEnabled(self): # real signature unknown; restored from __doc__
        """ QWidget.updatesEnabled() -> bool """
        return False

    def visibleRegion(self): # real signature unknown; restored from __doc__
        """ QWidget.visibleRegion() -> QRegion """
        return QRegion

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QWidget.whatsThis() -> QString """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QWidget.wheelEvent(QWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ QWidget.width() -> int """
        return 0

    def window(self): # real signature unknown; restored from __doc__
        """ QWidget.window() -> QWidget """
        return QWidget

    def windowActivationChange(self, bool): # real signature unknown; restored from __doc__
        """ QWidget.windowActivationChange(bool) """
        pass

    def windowFilePath(self): # real signature unknown; restored from __doc__
        """ QWidget.windowFilePath() -> QString """
        pass

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ QWidget.windowFlags() -> Qt.WindowFlags """
        pass

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ QWidget.windowIcon() -> QIcon """
        return QIcon

    def windowIconText(self): # real signature unknown; restored from __doc__
        """ QWidget.windowIconText() -> QString """
        pass

    def windowModality(self): # real signature unknown; restored from __doc__
        """ QWidget.windowModality() -> Qt.WindowModality """
        pass

    def windowOpacity(self): # real signature unknown; restored from __doc__
        """ QWidget.windowOpacity() -> float """
        return 0.0

    def windowRole(self): # real signature unknown; restored from __doc__
        """ QWidget.windowRole() -> QString """
        pass

    def windowState(self): # real signature unknown; restored from __doc__
        """ QWidget.windowState() -> Qt.WindowStates """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ QWidget.windowTitle() -> QString """
        pass

    def windowType(self): # real signature unknown; restored from __doc__
        """ QWidget.windowType() -> Qt.WindowType """
        pass

    def winId(self): # real signature unknown; restored from __doc__
        """ QWidget.winId() -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ QWidget.x() -> int """
        return 0

    def x11Info(self): # real signature unknown; restored from __doc__
        """ QWidget.x11Info() -> QX11Info """
        return QX11Info

    def x11PictureHandle(self): # real signature unknown; restored from __doc__
        """ QWidget.x11PictureHandle() -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ QWidget.y() -> int """
        return 0

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    DrawChildren = 2
    DrawWindowBackground = 1
    IgnoreMask = 4


