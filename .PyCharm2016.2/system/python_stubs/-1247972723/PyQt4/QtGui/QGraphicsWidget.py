# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QGraphicsObject import QGraphicsObject

from QGraphicsLayoutItem import QGraphicsLayoutItem

class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    """ QGraphicsWidget(QGraphicsItem parent=None, Qt.WindowFlags flags=0) """
    def actions(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.actions() -> list-of-QAction """
        pass

    def addAction(self, QAction): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.addAction(QAction) """
        pass

    def addActions(self, list_of_QAction): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.addActions(list-of-QAction) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.adjustSize() """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.autoFillBackground() -> bool """
        return False

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.boundingRect() -> QRectF """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.changeEvent(QEvent) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.close() -> bool """
        return False

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.closeEvent(QCloseEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.event(QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.focusOutEvent(QFocusEvent) """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.focusPolicy() -> Qt.FocusPolicy """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.focusWidget() -> QGraphicsWidget """
        return QGraphicsWidget

    def font(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.font() -> QFont """
        return QFont

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWidget.geometryChanged [signal] """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.getContentsMargins() -> (float, float, float, float) """
        pass

    def getWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.getWindowFrameMargins() -> (float, float, float, float) """
        pass

    def grabKeyboardEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.grabKeyboardEvent(QEvent) """
        pass

    def grabMouseEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.grabMouseEvent(QEvent) """
        pass

    def grabShortcut(self, QKeySequence, Qt_ShortcutContext_context=None): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.grabShortcut(QKeySequence, Qt.ShortcutContext context=Qt.WindowShortcut) -> int """
        return 0

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.hideEvent(QHideEvent) """
        pass

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.hoverLeaveEvent(QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.hoverMoveEvent(QGraphicsSceneHoverEvent) """
        pass

    def initStyleOption(self, QStyleOption): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.initStyleOption(QStyleOption) """
        pass

    def insertAction(self, QAction, QAction_1): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.insertAction(QAction, QAction) """
        pass

    def insertActions(self, QAction, list_of_QAction): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.insertActions(QAction, list-of-QAction) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.isActiveWindow() -> bool """
        return False

    def itemChange(self, QGraphicsItem_GraphicsItemChange, QVariant): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.itemChange(QGraphicsItem.GraphicsItemChange, QVariant) -> QVariant """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.layout() -> QGraphicsLayout """
        return QGraphicsLayout

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.layoutDirection() -> Qt.LayoutDirection """
        pass

    def moveEvent(self, QGraphicsSceneMoveEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.moveEvent(QGraphicsSceneMoveEvent) """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def paintWindowFrame(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.paintWindowFrame(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.palette() -> QPalette """
        return QPalette

    def polishEvent(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.polishEvent() """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.rect() -> QRectF """
        pass

    def releaseShortcut(self, p_int): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.releaseShortcut(int) """
        pass

    def removeAction(self, QAction): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.removeAction(QAction) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsWidget.resize(QSizeF)
        QGraphicsWidget.resize(float, float)
        """
        pass

    def resizeEvent(self, QGraphicsSceneResizeEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.resizeEvent(QGraphicsSceneResizeEvent) """
        pass

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.sceneEvent(QEvent) -> bool """
        return False

    def setAttribute(self, Qt_WidgetAttribute, bool_on=True): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setAttribute(Qt.WidgetAttribute, bool on=True) """
        pass

    def setAutoFillBackground(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setAutoFillBackground(bool) """
        pass

    def setContentsMargins(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setContentsMargins(float, float, float, float) """
        pass

    def setFocusPolicy(self, Qt_FocusPolicy): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setFocusPolicy(Qt.FocusPolicy) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setFont(QFont) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsWidget.setGeometry(QRectF)
        QGraphicsWidget.setGeometry(float, float, float, float)
        """
        pass

    def setLayout(self, QGraphicsLayout): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setLayout(QGraphicsLayout) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setLayoutDirection(Qt.LayoutDirection) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setPalette(QPalette) """
        pass

    def setShortcutAutoRepeat(self, p_int, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setShortcutAutoRepeat(int, bool enabled=True) """
        pass

    def setShortcutEnabled(self, p_int, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setShortcutEnabled(int, bool enabled=True) """
        pass

    def setStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setStyle(QStyle) """
        pass

    def setTabOrder(self, QGraphicsWidget, QGraphicsWidget_1): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setTabOrder(QGraphicsWidget, QGraphicsWidget) """
        pass

    def setWindowFlags(self, Qt_WindowFlags): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setWindowFlags(Qt.WindowFlags) """
        pass

    def setWindowFrameMargins(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setWindowFrameMargins(float, float, float, float) """
        pass

    def setWindowTitle(self, QString): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.setWindowTitle(QString) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.shape() -> QPainterPath """
        return QPainterPath

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.showEvent(QShowEvent) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.size() -> QSizeF """
        pass

    def sizeHint(self, Qt_SizeHint, QSizeF_constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsWidget.sizeHint(Qt.SizeHint, QSizeF constraint=QSizeF()) -> QSizeF """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.style() -> QStyle """
        return QStyle

    def testAttribute(self, Qt_WidgetAttribute): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.testAttribute(Qt.WidgetAttribute) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.type() -> int """
        return 0

    def ungrabKeyboardEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.ungrabKeyboardEvent(QEvent) """
        pass

    def ungrabMouseEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.ungrabMouseEvent(QEvent) """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.unsetLayoutDirection() """
        pass

    def unsetWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.unsetWindowFrameMargins() """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.updateGeometry() """
        pass

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowFlags() -> Qt.WindowFlags """
        pass

    def windowFrameEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowFrameEvent(QEvent) -> bool """
        return False

    def windowFrameGeometry(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowFrameGeometry() -> QRectF """
        pass

    def windowFrameRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowFrameRect() -> QRectF """
        pass

    def windowFrameSectionAt(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowFrameSectionAt(QPointF) -> Qt.WindowFrameSection """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowTitle() -> QString """
        pass

    def windowType(self): # real signature unknown; restored from __doc__
        """ QGraphicsWidget.windowType() -> Qt.WindowType """
        pass

    def __init__(self, QGraphicsItem_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass


