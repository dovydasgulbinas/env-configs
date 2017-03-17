# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGraphicsScene(__PyQt4_QtCore.QObject):
    """
    QGraphicsScene(QObject parent=None)
    QGraphicsScene(QRectF, QObject parent=None)
    QGraphicsScene(float, float, float, float, QObject parent=None)
    """
    def activePanel(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.activePanel() -> QGraphicsItem """
        return QGraphicsItem

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.activeWindow() -> QGraphicsWidget """
        return QGraphicsWidget

    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.addEllipse(QRectF, QPen pen=QPen(), QBrush brush=QBrush()) -> QGraphicsEllipseItem
        QGraphicsScene.addEllipse(float, float, float, float, QPen pen=QPen(), QBrush brush=QBrush()) -> QGraphicsEllipseItem
        """
        pass

    def addItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsScene.addItem(QGraphicsItem) """
        pass

    def addLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.addLine(QLineF, QPen pen=QPen()) -> QGraphicsLineItem
        QGraphicsScene.addLine(float, float, float, float, QPen pen=QPen()) -> QGraphicsLineItem
        """
        pass

    def addPath(self, QPainterPath, QPen_pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsScene.addPath(QPainterPath, QPen pen=QPen(), QBrush brush=QBrush()) -> QGraphicsPathItem """
        pass

    def addPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QGraphicsScene.addPixmap(QPixmap) -> QGraphicsPixmapItem """
        return QGraphicsPixmapItem

    def addPolygon(self, QPolygonF, QPen_pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsScene.addPolygon(QPolygonF, QPen pen=QPen(), QBrush brush=QBrush()) -> QGraphicsPolygonItem """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.addRect(QRectF, QPen pen=QPen(), QBrush brush=QBrush()) -> QGraphicsRectItem
        QGraphicsScene.addRect(float, float, float, float, QPen pen=QPen(), QBrush brush=QBrush()) -> QGraphicsRectItem
        """
        pass

    def addSimpleText(self, QString, QFont_font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsScene.addSimpleText(QString, QFont font=QFont()) -> QGraphicsSimpleTextItem """
        pass

    def addText(self, QString, QFont_font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsScene.addText(QString, QFont font=QFont()) -> QGraphicsTextItem """
        pass

    def addWidget(self, QWidget, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QGraphicsScene.addWidget(QWidget, Qt.WindowFlags flags=0) -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def advance(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.advance() """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.backgroundBrush() -> QBrush """
        return QBrush

    def bspTreeDepth(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.bspTreeDepth() -> int """
        return 0

    def changed(self, *args, **kwargs): # real signature unknown
        """ QGraphicsScene.changed[list-of-QRectF] [signal] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.clear() """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.clearFocus() """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.clearSelection() """
        pass

    def collidingItems(self, QGraphicsItem, Qt_ItemSelectionMode_mode=None): # real signature unknown; restored from __doc__
        """ QGraphicsScene.collidingItems(QGraphicsItem, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem """
        pass

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.contextMenuEvent(QGraphicsSceneContextMenuEvent) """
        pass

    def createItemGroup(self, list_of_QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsScene.createItemGroup(list-of-QGraphicsItem) -> QGraphicsItemGroup """
        return QGraphicsItemGroup

    def destroyItemGroup(self, QGraphicsItemGroup): # real signature unknown; restored from __doc__
        """ QGraphicsScene.destroyItemGroup(QGraphicsItemGroup) """
        pass

    def dragEnterEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.dragEnterEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.dragLeaveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.dragMoveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def drawBackground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsScene.drawBackground(QPainter, QRectF) """
        pass

    def drawForeground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsScene.drawForeground(QPainter, QRectF) """
        pass

    def drawItems(self, QPainter, list_of_QGraphicsItem, list_of_QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsScene.drawItems(QPainter, list-of-QGraphicsItem, list-of-QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def dropEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.dropEvent(QGraphicsSceneDragDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.eventFilter(QObject, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.focusInEvent(QFocusEvent) """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.focusItem() -> QGraphicsItem """
        return QGraphicsItem

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsScene.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.focusOutEvent(QFocusEvent) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.font() -> QFont """
        return QFont

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.foregroundBrush() -> QBrush """
        return QBrush

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.hasFocus() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.height() -> float """
        return 0.0

    def helpEvent(self, QGraphicsSceneHelpEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.helpEvent(QGraphicsSceneHelpEvent) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QGraphicsScene.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def invalidate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.invalidate(QRectF rect=QRectF(), QGraphicsScene.SceneLayers layers=QGraphicsScene.AllLayers)
        QGraphicsScene.invalidate(float, float, float, float, QGraphicsScene.SceneLayers layers=QGraphicsScene.AllLayers)
        """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.isActive() -> bool """
        return False

    def isSortCacheEnabled(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.isSortCacheEnabled() -> bool """
        return False

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.itemAt(QPointF) -> QGraphicsItem
        QGraphicsScene.itemAt(float, float) -> QGraphicsItem
        QGraphicsScene.itemAt(QPointF, QTransform) -> QGraphicsItem
        QGraphicsScene.itemAt(float, float, QTransform) -> QGraphicsItem
        """
        return QGraphicsItem

    def itemIndexMethod(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.itemIndexMethod() -> QGraphicsScene.ItemIndexMethod """
        pass

    def items(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.items() -> list-of-QGraphicsItem
        QGraphicsScene.items(Qt.SortOrder) -> list-of-QGraphicsItem
        QGraphicsScene.items(QPointF) -> list-of-QGraphicsItem
        QGraphicsScene.items(QPointF, Qt.ItemSelectionMode, Qt.SortOrder, QTransform deviceTransform=QTransform()) -> list-of-QGraphicsItem
        QGraphicsScene.items(QRectF, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsScene.items(QRectF, Qt.ItemSelectionMode, Qt.SortOrder, QTransform deviceTransform=QTransform()) -> list-of-QGraphicsItem
        QGraphicsScene.items(QPolygonF, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsScene.items(QPolygonF, Qt.ItemSelectionMode, Qt.SortOrder, QTransform deviceTransform=QTransform()) -> list-of-QGraphicsItem
        QGraphicsScene.items(QPainterPath, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsScene.items(QPainterPath, Qt.ItemSelectionMode, Qt.SortOrder, QTransform deviceTransform=QTransform()) -> list-of-QGraphicsItem
        QGraphicsScene.items(float, float, float, float, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem
        QGraphicsScene.items(float, float, float, float, Qt.ItemSelectionMode, Qt.SortOrder, QTransform deviceTransform=QTransform()) -> list-of-QGraphicsItem
        """
        pass

    def itemsBoundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.itemsBoundingRect() -> QRectF """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.keyReleaseEvent(QKeyEvent) """
        pass

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.mouseDoubleClickEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseGrabberItem(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.mouseGrabberItem() -> QGraphicsItem """
        return QGraphicsItem

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.mouseMoveEvent(QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.mousePressEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.mouseReleaseEvent(QGraphicsSceneMouseEvent) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.palette() -> QPalette """
        return QPalette

    def removeItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsScene.removeItem(QGraphicsItem) """
        pass

    def render(self, QPainter, QRectF_target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsScene.render(QPainter, QRectF target=QRectF(), QRectF source=QRectF(), Qt.AspectRatioMode mode=Qt.KeepAspectRatio) """
        pass

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.sceneRect() -> QRectF """
        pass

    def sceneRectChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsScene.sceneRectChanged[QRectF] [signal] """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.selectedItems() -> list-of-QGraphicsItem """
        pass

    def selectionArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.selectionArea() -> QPainterPath """
        return QPainterPath

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsScene.selectionChanged [signal] """
        pass

    def sendEvent(self, QGraphicsItem, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.sendEvent(QGraphicsItem, QEvent) -> bool """
        return False

    def setActivePanel(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setActivePanel(QGraphicsItem) """
        pass

    def setActiveWindow(self, QGraphicsWidget): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setActiveWindow(QGraphicsWidget) """
        pass

    def setBackgroundBrush(self, QBrush): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setBackgroundBrush(QBrush) """
        pass

    def setBspTreeDepth(self, p_int): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setBspTreeDepth(int) """
        pass

    def setFocus(self, Qt_FocusReason_focusReason=None): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setFocus(Qt.FocusReason focusReason=Qt.OtherFocusReason) """
        pass

    def setFocusItem(self, QGraphicsItem, Qt_FocusReason_focusReason=None): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setFocusItem(QGraphicsItem, Qt.FocusReason focusReason=Qt.OtherFocusReason) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setFont(QFont) """
        pass

    def setForegroundBrush(self, QBrush): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setForegroundBrush(QBrush) """
        pass

    def setItemIndexMethod(self, QGraphicsScene_ItemIndexMethod): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setItemIndexMethod(QGraphicsScene.ItemIndexMethod) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setPalette(QPalette) """
        pass

    def setSceneRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.setSceneRect(QRectF)
        QGraphicsScene.setSceneRect(float, float, float, float)
        """
        pass

    def setSelectionArea(self, QPainterPath, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.setSelectionArea(QPainterPath, QTransform)
        QGraphicsScene.setSelectionArea(QPainterPath)
        QGraphicsScene.setSelectionArea(QPainterPath, Qt.ItemSelectionMode)
        QGraphicsScene.setSelectionArea(QPainterPath, Qt.ItemSelectionMode, QTransform)
        """
        pass

    def setSortCacheEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setSortCacheEnabled(bool) """
        pass

    def setStickyFocus(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setStickyFocus(bool) """
        pass

    def setStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ QGraphicsScene.setStyle(QStyle) """
        pass

    def stickyFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.stickyFocus() -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.style() -> QStyle """
        return QStyle

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsScene.update(QRectF rect=QRectF())
        QGraphicsScene.update(float, float, float, float)
        """
        pass

    def views(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.views() -> list-of-QGraphicsView """
        pass

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ QGraphicsScene.wheelEvent(QGraphicsSceneWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ QGraphicsScene.width() -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllLayers = 65535
    BackgroundLayer = 2
    BspTreeIndex = 0
    ForegroundLayer = 4
    ItemLayer = 1
    NoIndex = -1


