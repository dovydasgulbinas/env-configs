# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python2.7/dist-packages/PyQt4/QtGui.so
# by generator 1.143
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGraphicsItem(): # skipped bases: <type 'sip.wrapper'>
    """ QGraphicsItem(QGraphicsItem parent=None, QGraphicsScene scene=None) """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.acceptDrops() -> bool """
        return False

    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.acceptedMouseButtons() -> Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.acceptHoverEvents() -> bool """
        return False

    def acceptsHoverEvents(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.acceptsHoverEvents() -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.acceptTouchEvents() -> bool """
        return False

    def advance(self, p_int): # real signature unknown; restored from __doc__
        """ QGraphicsItem.advance(int) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.boundingRect() -> QRectF """
        pass

    def boundingRegion(self, QTransform): # real signature unknown; restored from __doc__
        """ QGraphicsItem.boundingRegion(QTransform) -> QRegion """
        return QRegion

    def boundingRegionGranularity(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.boundingRegionGranularity() -> float """
        return 0.0

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.cacheMode() -> QGraphicsItem.CacheMode """
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.childItems() -> list-of-QGraphicsItem """
        pass

    def childrenBoundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.childrenBoundingRect() -> QRectF """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.clearFocus() """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.clipPath() -> QPainterPath """
        return QPainterPath

    def collidesWithItem(self, QGraphicsItem, Qt_ItemSelectionMode_mode=None): # real signature unknown; restored from __doc__
        """ QGraphicsItem.collidesWithItem(QGraphicsItem, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> bool """
        return False

    def collidesWithPath(self, QPainterPath, Qt_ItemSelectionMode_mode=None): # real signature unknown; restored from __doc__
        """ QGraphicsItem.collidesWithPath(QPainterPath, Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> bool """
        return False

    def collidingItems(self, Qt_ItemSelectionMode_mode=None): # real signature unknown; restored from __doc__
        """ QGraphicsItem.collidingItems(Qt.ItemSelectionMode mode=Qt.IntersectsItemShape) -> list-of-QGraphicsItem """
        pass

    def commonAncestorItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.commonAncestorItem(QGraphicsItem) -> QGraphicsItem """
        return QGraphicsItem

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsItem.contains(QPointF) -> bool """
        return False

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.contextMenuEvent(QGraphicsSceneContextMenuEvent) """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.cursor() -> QCursor """
        return QCursor

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ QGraphicsItem.data(int) -> QVariant """
        pass

    def deviceTransform(self, QTransform): # real signature unknown; restored from __doc__
        """ QGraphicsItem.deviceTransform(QTransform) -> QTransform """
        return QTransform

    def dragEnterEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.dragEnterEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.dragLeaveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.dragMoveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dropEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.dropEvent(QGraphicsSceneDragDropEvent) """
        pass

    def effectiveOpacity(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.effectiveOpacity() -> float """
        return 0.0

    def ensureVisible(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.ensureVisible(QRectF rect=QRectF(), int xMargin=50, int yMargin=50)
        QGraphicsItem.ensureVisible(float, float, float, float, int xMargin=50, int yMargin=50)
        """
        pass

    def filtersChildEvents(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.filtersChildEvents() -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.flags() -> QGraphicsItem.GraphicsItemFlags """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.focusInEvent(QFocusEvent) """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.focusItem() -> QGraphicsItem """
        return QGraphicsItem

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.focusOutEvent(QFocusEvent) """
        pass

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.focusProxy() -> QGraphicsItem """
        return QGraphicsItem

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.grabKeyboard() """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.grabMouse() """
        pass

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.graphicsEffect() -> QGraphicsEffect """
        return QGraphicsEffect

    def group(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.group() -> QGraphicsItemGroup """
        return QGraphicsItemGroup

    def handlesChildEvents(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.handlesChildEvents() -> bool """
        return False

    def hasCursor(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.hasCursor() -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.hasFocus() -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.hide() """
        pass

    def hoverEnterEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.hoverEnterEvent(QGraphicsSceneHoverEvent) """
        pass

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.hoverLeaveEvent(QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.hoverMoveEvent(QGraphicsSceneHoverEvent) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.inputMethodHints() -> Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QGraphicsItem.inputMethodQuery(Qt.InputMethodQuery) -> QVariant """
        pass

    def installSceneEventFilter(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.installSceneEventFilter(QGraphicsItem) """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isActive() -> bool """
        return False

    def isAncestorOf(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isAncestorOf(QGraphicsItem) -> bool """
        return False

    def isBlockedByModalPanel(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isBlockedByModalPanel() -> (bool, QGraphicsItem) """
        pass

    def isClipped(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isClipped() -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isEnabled() -> bool """
        return False

    def isObscured(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.isObscured() -> bool
        QGraphicsItem.isObscured(QRectF) -> bool
        QGraphicsItem.isObscured(float, float, float, float) -> bool
        """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def isPanel(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isPanel() -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isSelected() -> bool """
        return False

    def isUnderMouse(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isUnderMouse() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isVisible() -> bool """
        return False

    def isVisibleTo(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isVisibleTo(QGraphicsItem) -> bool """
        return False

    def isWidget(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isWidget() -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.isWindow() -> bool """
        return False

    def itemChange(self, QGraphicsItem_GraphicsItemChange, QVariant): # real signature unknown; restored from __doc__
        """ QGraphicsItem.itemChange(QGraphicsItem.GraphicsItemChange, QVariant) -> QVariant """
        pass

    def itemTransform(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.itemTransform(QGraphicsItem) -> (QTransform, bool) """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.keyReleaseEvent(QKeyEvent) """
        pass

    def mapFromItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapFromItem(QGraphicsItem, QPointF) -> QPointF
        QGraphicsItem.mapFromItem(QGraphicsItem, QRectF) -> QPolygonF
        QGraphicsItem.mapFromItem(QGraphicsItem, QPolygonF) -> QPolygonF
        QGraphicsItem.mapFromItem(QGraphicsItem, QPainterPath) -> QPainterPath
        QGraphicsItem.mapFromItem(QGraphicsItem, float, float) -> QPointF
        QGraphicsItem.mapFromItem(QGraphicsItem, float, float, float, float) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def mapFromParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapFromParent(QPointF) -> QPointF
        QGraphicsItem.mapFromParent(QRectF) -> QPolygonF
        QGraphicsItem.mapFromParent(QPolygonF) -> QPolygonF
        QGraphicsItem.mapFromParent(QPainterPath) -> QPainterPath
        QGraphicsItem.mapFromParent(float, float) -> QPointF
        QGraphicsItem.mapFromParent(float, float, float, float) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def mapFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapFromScene(QPointF) -> QPointF
        QGraphicsItem.mapFromScene(QRectF) -> QPolygonF
        QGraphicsItem.mapFromScene(QPolygonF) -> QPolygonF
        QGraphicsItem.mapFromScene(QPainterPath) -> QPainterPath
        QGraphicsItem.mapFromScene(float, float) -> QPointF
        QGraphicsItem.mapFromScene(float, float, float, float) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def mapRectFromItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapRectFromItem(QGraphicsItem, QRectF) -> QRectF
        QGraphicsItem.mapRectFromItem(QGraphicsItem, float, float, float, float) -> QRectF
        """
        pass

    def mapRectFromParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapRectFromParent(QRectF) -> QRectF
        QGraphicsItem.mapRectFromParent(float, float, float, float) -> QRectF
        """
        pass

    def mapRectFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapRectFromScene(QRectF) -> QRectF
        QGraphicsItem.mapRectFromScene(float, float, float, float) -> QRectF
        """
        pass

    def mapRectToItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapRectToItem(QGraphicsItem, QRectF) -> QRectF
        QGraphicsItem.mapRectToItem(QGraphicsItem, float, float, float, float) -> QRectF
        """
        pass

    def mapRectToParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapRectToParent(QRectF) -> QRectF
        QGraphicsItem.mapRectToParent(float, float, float, float) -> QRectF
        """
        pass

    def mapRectToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapRectToScene(QRectF) -> QRectF
        QGraphicsItem.mapRectToScene(float, float, float, float) -> QRectF
        """
        pass

    def mapToItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapToItem(QGraphicsItem, QPointF) -> QPointF
        QGraphicsItem.mapToItem(QGraphicsItem, QRectF) -> QPolygonF
        QGraphicsItem.mapToItem(QGraphicsItem, QPolygonF) -> QPolygonF
        QGraphicsItem.mapToItem(QGraphicsItem, QPainterPath) -> QPainterPath
        QGraphicsItem.mapToItem(QGraphicsItem, float, float) -> QPointF
        QGraphicsItem.mapToItem(QGraphicsItem, float, float, float, float) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def mapToParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapToParent(QPointF) -> QPointF
        QGraphicsItem.mapToParent(QRectF) -> QPolygonF
        QGraphicsItem.mapToParent(QPolygonF) -> QPolygonF
        QGraphicsItem.mapToParent(QPainterPath) -> QPainterPath
        QGraphicsItem.mapToParent(float, float) -> QPointF
        QGraphicsItem.mapToParent(float, float, float, float) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def mapToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.mapToScene(QPointF) -> QPointF
        QGraphicsItem.mapToScene(QRectF) -> QPolygonF
        QGraphicsItem.mapToScene(QPolygonF) -> QPolygonF
        QGraphicsItem.mapToScene(QPainterPath) -> QPainterPath
        QGraphicsItem.mapToScene(float, float) -> QPointF
        QGraphicsItem.mapToScene(float, float, float, float) -> QPolygonF
        """
        return QPolygonF or QPainterPath

    def matrix(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.matrix() -> QMatrix """
        return QMatrix

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.mouseDoubleClickEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.mouseMoveEvent(QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.mousePressEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.mouseReleaseEvent(QGraphicsSceneMouseEvent) """
        pass

    def moveBy(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QGraphicsItem.moveBy(float, float) """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.opacity() -> float """
        return 0.0

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def panel(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.panel() -> QGraphicsItem """
        return QGraphicsItem

    def panelModality(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.panelModality() -> QGraphicsItem.PanelModality """
        pass

    def parentItem(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.parentItem() -> QGraphicsItem """
        return QGraphicsItem

    def parentObject(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.parentObject() -> QGraphicsObject """
        return QGraphicsObject

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.parentWidget() -> QGraphicsWidget """
        return QGraphicsWidget

    def pos(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.pos() -> QPointF """
        pass

    def prepareGeometryChange(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.prepareGeometryChange() """
        pass

    def removeSceneEventFilter(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.removeSceneEventFilter(QGraphicsItem) """
        pass

    def resetMatrix(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.resetMatrix() """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.resetTransform() """
        pass

    def rotate(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.rotate(float) """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.rotation() -> float """
        return 0.0

    def scale(self, p_float=None, p_float_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.scale(float, float)
        QGraphicsItem.scale() -> float
        """
        return 0.0

    def scene(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.scene() -> QGraphicsScene """
        return QGraphicsScene

    def sceneBoundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.sceneBoundingRect() -> QRectF """
        pass

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.sceneEvent(QEvent) -> bool """
        return False

    def sceneEventFilter(self, QGraphicsItem, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.sceneEventFilter(QGraphicsItem, QEvent) -> bool """
        return False

    def sceneMatrix(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.sceneMatrix() -> QMatrix """
        return QMatrix

    def scenePos(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.scenePos() -> QPointF """
        pass

    def sceneTransform(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.sceneTransform() -> QTransform """
        return QTransform

    def scroll(self, p_float, p_float_1, QRectF_rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsItem.scroll(float, float, QRectF rect=QRectF()) """
        pass

    def setAcceptDrops(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setAcceptDrops(bool) """
        pass

    def setAcceptedMouseButtons(self, Qt_MouseButtons): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setAcceptedMouseButtons(Qt.MouseButtons) """
        pass

    def setAcceptHoverEvents(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setAcceptHoverEvents(bool) """
        pass

    def setAcceptsHoverEvents(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setAcceptsHoverEvents(bool) """
        pass

    def setAcceptTouchEvents(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setAcceptTouchEvents(bool) """
        pass

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setActive(bool) """
        pass

    def setBoundingRegionGranularity(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setBoundingRegionGranularity(float) """
        pass

    def setCacheMode(self, QGraphicsItem_CacheMode, QSize_logicalCacheSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsItem.setCacheMode(QGraphicsItem.CacheMode, QSize logicalCacheSize=QSize()) """
        pass

    def setCursor(self, QCursor): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setCursor(QCursor) """
        pass

    def setData(self, p_int, QVariant): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setData(int, QVariant) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setEnabled(bool) """
        pass

    def setFiltersChildEvents(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setFiltersChildEvents(bool) """
        pass

    def setFlag(self, QGraphicsItem_GraphicsItemFlag, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setFlag(QGraphicsItem.GraphicsItemFlag, bool enabled=True) """
        pass

    def setFlags(self, QGraphicsItem_GraphicsItemFlags): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setFlags(QGraphicsItem.GraphicsItemFlags) """
        pass

    def setFocus(self, Qt_FocusReason_focusReason=None): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setFocus(Qt.FocusReason focusReason=Qt.OtherFocusReason) """
        pass

    def setFocusProxy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setFocusProxy(QGraphicsItem) """
        pass

    def setGraphicsEffect(self, QGraphicsEffect): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setGraphicsEffect(QGraphicsEffect) """
        pass

    def setGroup(self, QGraphicsItemGroup): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setGroup(QGraphicsItemGroup) """
        pass

    def setHandlesChildEvents(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setHandlesChildEvents(bool) """
        pass

    def setInputMethodHints(self, Qt_InputMethodHints): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setInputMethodHints(Qt.InputMethodHints) """
        pass

    def setMatrix(self, QMatrix, bool_combine=False): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setMatrix(QMatrix, bool combine=False) """
        pass

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setOpacity(float) """
        pass

    def setPanelModality(self, QGraphicsItem_PanelModality): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setPanelModality(QGraphicsItem.PanelModality) """
        pass

    def setParentItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setParentItem(QGraphicsItem) """
        pass

    def setPos(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.setPos(QPointF)
        QGraphicsItem.setPos(float, float)
        """
        pass

    def setRotation(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setRotation(float) """
        pass

    def setScale(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setScale(float) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setSelected(bool) """
        pass

    def setToolTip(self, QString): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setToolTip(QString) """
        pass

    def setTransform(self, QTransform, bool_combine=False): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setTransform(QTransform, bool combine=False) """
        pass

    def setTransformations(self, list_of_QGraphicsTransform): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setTransformations(list-of-QGraphicsTransform) """
        pass

    def setTransformOriginPoint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.setTransformOriginPoint(QPointF)
        QGraphicsItem.setTransformOriginPoint(float, float)
        """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setVisible(bool) """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setX(float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setY(float) """
        pass

    def setZValue(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsItem.setZValue(float) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.shape() -> QPainterPath """
        return QPainterPath

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QGraphicsItem.shear(float, float) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.show() """
        pass

    def stackBefore(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsItem.stackBefore(QGraphicsItem) """
        pass

    def toGraphicsObject(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.toGraphicsObject() -> QGraphicsObject """
        return QGraphicsObject

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.toolTip() -> QString """
        pass

    def topLevelItem(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.topLevelItem() -> QGraphicsItem """
        return QGraphicsItem

    def topLevelWidget(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.topLevelWidget() -> QGraphicsWidget """
        return QGraphicsWidget

    def transform(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.transform() -> QTransform """
        return QTransform

    def transformations(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.transformations() -> list-of-QGraphicsTransform """
        pass

    def transformOriginPoint(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.transformOriginPoint() -> QPointF """
        pass

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QGraphicsItem.translate(float, float) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.type() -> int """
        return 0

    def ungrabKeyboard(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.ungrabKeyboard() """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.ungrabMouse() """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.unsetCursor() """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsItem.update(QRectF rect=QRectF())
        QGraphicsItem.update(float, float, float, float)
        """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.updateMicroFocus() """
        pass

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ QGraphicsItem.wheelEvent(QGraphicsSceneWheelEvent) """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.window() -> QGraphicsWidget """
        return QGraphicsWidget

    def x(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.x() -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.y() -> float """
        return 0.0

    def zValue(self): # real signature unknown; restored from __doc__
        """ QGraphicsItem.zValue() -> float """
        return 0.0

    def __init__(self, QGraphicsItem_parent=None, QGraphicsScene_scene=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceCoordinateCache = 2
    ItemAcceptsInputMethod = 4096
    ItemChildAddedChange = 6
    ItemChildRemovedChange = 7
    ItemClipsChildrenToShape = 16
    ItemClipsToShape = 8
    ItemCoordinateCache = 1
    ItemCursorChange = 17
    ItemCursorHasChanged = 18
    ItemDoesntPropagateOpacityToChildren = 128
    ItemEnabledChange = 3
    ItemEnabledHasChanged = 13
    ItemFlagsChange = 21
    ItemFlagsHaveChanged = 22
    ItemHasNoContents = 1024
    ItemIgnoresParentOpacity = 64
    ItemIgnoresTransformations = 32
    ItemIsFocusable = 4
    ItemIsMovable = 1
    ItemIsPanel = 16384
    ItemIsSelectable = 2
    ItemMatrixChange = 1
    ItemNegativeZStacksBehindParent = 8192
    ItemOpacityChange = 25
    ItemOpacityHasChanged = 26
    ItemParentChange = 5
    ItemParentHasChanged = 15
    ItemPositionChange = 0
    ItemPositionHasChanged = 9
    ItemRotationChange = 28
    ItemRotationHasChanged = 29
    ItemScaleChange = 30
    ItemScaleHasChanged = 31
    ItemSceneChange = 11
    ItemSceneHasChanged = 16
    ItemScenePositionHasChanged = 27
    ItemSelectedChange = 4
    ItemSelectedHasChanged = 14
    ItemSendsGeometryChanges = 2048
    ItemSendsScenePositionChanges = 65536
    ItemStacksBehindParent = 256
    ItemToolTipChange = 19
    ItemToolTipHasChanged = 20
    ItemTransformChange = 8
    ItemTransformHasChanged = 10
    ItemTransformOriginPointChange = 32
    ItemTransformOriginPointHasChanged = 33
    ItemUsesExtendedStyleOption = 512
    ItemVisibleChange = 2
    ItemVisibleHasChanged = 12
    ItemZValueChange = 23
    ItemZValueHasChanged = 24
    NoCache = 0
    NonModal = 0
    PanelModal = 1
    SceneModal = 2
    UserType = 65536


